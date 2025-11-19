from tkinter import *
import csv, os

SPRINGBOK_GREEN = "#006341"
SPRINGBOK_GOLD = "#FFB81C"

class BMIScreen:
    def __init__(self, root):
        self.root = root
        self.window = Toplevel(self.root)
        self.window.title("BMI Calculator")
        self.window.geometry("400x400")
        self.window.configure(bg=SPRINGBOK_GREEN)

        Label(
            self.window,
            text="🏉 BMI Calculator",
            font=("Arial", 18, "bold"),
            fg=SPRINGBOK_GOLD,
            bg=SPRINGBOK_GREEN
        ).pack(pady=10)

        Label(
            self.window,
            text="Enter your Height (cm):",
            fg=SPRINGBOK_GOLD,
            bg=SPRINGBOK_GREEN
        ).pack()
        self.height_entry = Entry(self.window)
        self.height_entry.pack(pady=5)

        Label(
            self.window,
            text="Enter your Weight (kg):",
            fg=SPRINGBOK_GOLD,
            bg=SPRINGBOK_GREEN
        ).pack()
        self.weight_entry = Entry(self.window)
        self.weight_entry.pack(pady=5)

        Button(
            self.window,
            text="Calculate BMI",
            bg=SPRINGBOK_GOLD,
            fg=SPRINGBOK_GREEN,
            font=("Arial", 12, "bold"),
            command=self.calculate_bmi
        ).pack(pady=15)

        self.result_label = Label(self.window, text="", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN)
        self.result_label.pack()

        Button(
            self.window,
            text="Load from Profile",
            bg=SPRINGBOK_GOLD,
            fg=SPRINGBOK_GREEN,
            font=("Arial", 10, "bold"),
            command=self.load_profile_data
        ).pack(pady=5)

    def calculate_bmi(self):
        try:
            height_cm = float(self.height_entry.get())
            weight_kg = float(self.weight_entry.get())
            height_m = height_cm / 100
            bmi = weight_kg / (height_m ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            self.result_label.config(
                text=f"BMI: {bmi:.1f} — {category}"
            )
        except ValueError:
            self.result_label.config(text="Please enter valid numbers.")

    def load_profile_data(self):
        """Auto-fill height & weight from profile.csv"""
        if not os.path.exists("data/profile.csv"):
            self.result_label.config(text="Profile not found.")
            return

        with open("data/profile.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "Height" in row and "Weight" in row:
                    self.height_entry.delete(0, END)
                    self.weight_entry.delete(0, END)
                    self.height_entry.insert(0, row["Height"])
                    self.weight_entry.insert(0, row["Weight"])
                    self.result_label.config(text="Loaded from profile ✅")
                    return
        self.result_label.config(text="Height/Weight not found in profile.")
        