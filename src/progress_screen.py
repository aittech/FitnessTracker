from tkinter import *
import csv, os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

SPRINGBOK_GREEN = "#006341"
SPRINGBOK_GOLD = "#FFB81C"

class ProgressScreen:
    def __init__(self, root):
        self.root = root
        self.window = Toplevel(self.root)
        self.window.title("Progress Summary")
        self.window.geometry("700x600")
        self.window.configure(bg=SPRINGBOK_GREEN)

        Label(
            self.window,
            text="🏉 Progress Summary",
            font=("Arial", 18, "bold"),
            fg=SPRINGBOK_GOLD,
            bg=SPRINGBOK_GREEN
        ).pack(pady=10)

        self.text_area = Text(self.window, width=75, height=12, bg="white", fg=SPRINGBOK_GREEN)
        self.text_area.pack(pady=5)

        Button(
            self.window,
            text="Refresh",
            bg=SPRINGBOK_GOLD,
            fg=SPRINGBOK_GREEN,
            font=("Arial", 12, "bold"),
            command=self.display_progress
        ).pack(pady=10)

        self.status_label = Label(self.window, text="", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN)
        self.status_label.pack()

        # Placeholder for chart canvas
        self.chart_canvas = None

        self.display_progress()

    def display_progress(self):
        file_path = "data/workouts.csv"
        if not os.path.exists(file_path):
            self.text_area.delete("1.0", END)
            self.text_area.insert(END, "No workout data found. Log your first workout!")
            self.status_label.config(text="")
            if self.chart_canvas:
                self.chart_canvas.get_tk_widget().destroy()
            return

        total_workouts = 0
        total_calories = 0.0
        activities = []
        calories_list = []

        with open(file_path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_workouts += 1
                calories = float(row["CaloriesBurned"])
                total_calories += calories
                activities.append(f"{row['Date']} - {row['Activity']}")
                calories_list.append(calories)

        # --- Text summary ---
        self.text_area.delete("1.0", END)
        for i in range(len(activities)):
            self.text_area.insert(
                END, f"{activities[i]} — {round(calories_list[i])} kcal\n"
            )

        self.status_label.config(
            text=f"Total Workouts: {total_workouts} | Total Calories Burned: {round(total_calories)} kcal"
        )

        # --- Plot chart ---
        self.show_chart(activities, calories_list)

    def show_chart(self, activities, calories_list):
        # Destroy existing chart (to refresh)
        if self.chart_canvas:
            self.chart_canvas.get_tk_widget().destroy()

        fig, ax = plt.subplots(figsize=(6, 3))
        bars = ax.bar(activities, calories_list, color=SPRINGBOK_GOLD)
        ax.set_title("Calories Burned per Workout", fontsize=12, color=SPRINGBOK_GOLD, pad=10)
        ax.set_xlabel("Workout", fontsize=10)
        ax.set_ylabel("Calories (kcal)", fontsize=10)
        ax.set_facecolor(SPRINGBOK_GREEN)
        ax.tick_params(axis='x', labelrotation=45)
        ax.spines['bottom'].set_color(SPRINGBOK_GOLD)
        ax.spines['left'].set_color(SPRINGBOK_GOLD)
        ax.tick_params(colors=SPRINGBOK_GOLD)

        fig.patch.set_facecolor(SPRINGBOK_GREEN)
        plt.tight_layout()

        # Embed into Tkinter
        self.chart_canvas = FigureCanvasTkAgg(fig, master=self.window)
        self.chart_canvas.draw()
        self.chart_canvas.get_tk_widget().pack(pady=10)
