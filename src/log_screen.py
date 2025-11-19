from tkinter import *
import csv, os
from datetime import date
from src.utils import calculate_formula_calories


SPRINGBOK_GREEN = "#006341"
SPRINGBOK_GOLD = "#FFB81C"

class LogScreen:
    def __init__(self, root):
        self.root = root
        self.window = Toplevel(self.root)
        self.window.title("Log Workout")
        self.window.geometry("400x400")
        self.window.configure(bg=SPRINGBOK_GREEN)

        Label(
            self.window,
            text="Log Workout",
            font=("Arial", 18, "bold"),
            fg=SPRINGBOK_GOLD,
            bg=SPRINGBOK_GREEN
        ).pack(pady=10)

        # --- Date field ---
        Label(self.window, text="Date", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN).pack()
        self.date_var = StringVar(value=date.today().isoformat())
        Entry(self.window, textvariable=self.date_var, state="readonly").pack(pady=5)

        # --- Activity type ---
        Label(self.window, text="Activity", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN).pack()
        self.activity_var = StringVar(value="Running")
        OptionMenu(self.window, self.activity_var, "Running", "Cycling", "Walking", "Strength").pack()

        # --- Duration ---
        Label(self.window, text="Duration (minutes)", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN).pack()
        self.duration_entry = Entry(self.window)
        self.duration_entry.pack(pady=5)

        # --- Load weight from profile ---
        self.weight = self.load_weight()

        Button(
            self.window,
            text="Save Workout",
            bg=SPRINGBOK_GOLD,
            fg=SPRINGBOK_GREEN,
            font=("Arial", 12, "bold"),
            command=self.save_workout
        ).pack(pady=10)

        self.status_label = Label(self.window, text="", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN)
        self.status_label.pack()

    def load_weight(self):
        """Reads the weight from data/profile.csv"""
        try:
            with open("data/profile.csv", newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    return float(row["Weight"])
        except Exception:
            return 70.0  # default if file missing

    def calculate_calories(self, activity, duration, weight):
        """Simple calorie formula"""
        MET = {
            "Running": 9.8,
            "Cycling": 7.5,
            "Walking": 3.8,
            "Strength": 6.0
        }
        hours = duration / 60
        return MET.get(activity, 5.0) * weight * hours

    def save_workout(self):
        activity = self.activity_var.get()
        try:
            duration = float(self.duration_entry.get())
        except ValueError:
            self.status_label.config(text="Enter a valid duration.")
            return

        calories = self.calculate_calories(activity, duration, self.weight)

        file_path = "data/workouts.csv"
        file_exists = os.path.exists(file_path)
        with open(file_path, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Date", "Activity", "Duration", "Weight", "CaloriesBurned"])
            writer.writerow([self.date_var.get(), activity, duration, self.weight, round(calories, 1)])

        self.status_label.config(text=f"Workout saved! {round(calories)} kcal burned ✅")
        self.duration_entry.delete(0, END)
