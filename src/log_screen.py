from tkinter import *
import csv, os
from datetime import date
from src.ml_model import train_calorie_models, predict_calories

SPRINGBOK_GREEN = "#006341"
SPRINGBOK_GOLD = "#FFB81C"

class LogScreen:
    def __init__(self, root):
        self.root = root
        self.window = Toplevel(self.root)
        self.window.title("Log Workout")
        self.window.geometry("400x450")
        self.window.configure(bg=SPRINGBOK_GREEN)

        Label(
            self.window,
            text="🏋️‍♂️ Log Workout",
            font=("Arial", 18, "bold"),
            fg=SPRINGBOK_GOLD,
            bg=SPRINGBOK_GREEN
        ).pack(pady=10)

        # --- Date field ---
        Label(self.window, text="Date", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN).pack()
        self.date_var = StringVar(value=date.today().isoformat())
        Entry(self.window, textvariable=self.date_var).pack(pady=5)

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

        Button(
            self.window,
            text="View ML Accuracy",
            bg=SPRINGBOK_GOLD,
            fg=SPRINGBOK_GREEN,
            font=("Arial", 12, "bold"),
            command=self.show_accuracy
        ).pack(pady=5)

        self.status_label = Label(self.window, text="", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN)
        self.status_label.pack()

        self.ml_label = Label(self.window, text="", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN, font=("Arial", 10, "italic"))
        self.ml_label.pack(pady=5)

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
        """Simple calorie formula (MET-based)"""
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
            return  # ✅ must be indented under except!

        # --- Train ML models for all activity types ---
        from src.ml_model import train_calorie_models, predict_calories
        models = train_calorie_models()

        if models:
            calories = predict_calories(models, duration, self.weight, activity)
            self.ml_label.config(text="🤖 ML model active for " + activity)
        else:
            calories = self.calculate_calories(activity, duration, self.weight)
            self.ml_label.config(text="Using formula-based calculation")

        # --- Save the workout data ---
        file_path = "data/workouts.csv"
        file_exists = os.path.exists(file_path)
        with open(file_path, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Date", "Activity", "Duration", "Weight", "CaloriesBurned"])
            writer.writerow([self.date_var.get(), activity, duration, self.weight, round(calories, 1)])

        # --- Feedback to user ---
        self.status_label.config(text=f"Workout saved! {round(calories)} kcal burned ✅")
        self.duration_entry.delete(0, END)

    def show_accuracy(self):
        from src.ml_model import get_model_accuracy
        acc = get_model_accuracy()
        if acc is None:
            self.status_label.config(text="Need at least 5 workouts to calculate accuracy.")
        else:
            self.status_label.config(text=f"🤖 ML Model Accuracy: {acc}%")
