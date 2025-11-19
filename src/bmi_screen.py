from tkinter import *

SPRINGBOK_GREEN = "#006341"
SPRINGBOK_GOLD = "#FFB81C"

class BMIScreen:
    def __init__(self, root):
        self.root = root
        self.window = Toplevel(self.root)
        self.window.title("BMI Calculator")
        self.window.geometry("400x400")
        self.window.configure(bg=SPRINGBOK_GREEN)

        Label(self.window, text="💪 BMI Calculator", font=("Arial", 18, "bold"),
              fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN).pack(pady=20)

        Label(self.window, text="Height (cm):", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN).pack()
        self.height_entry = Entry(self.window)
        self.height_entry.pack(pady=5)

        Label(self.window, text="Weight (kg):", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN).pack()
        self.weight_entry = Entry(self.window)
        self.weight_entry.pack(pady=5)

        Button(self.window, text="Calculate BMI", bg=SPRINGBOK_GOLD, fg=SPRINGBOK_GREEN,
               font=("Arial", 12, "bold"), command=self.calculate_bmi).pack(pady=10)

        self.result_label = Label(self.window, text="", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN)
        self.result_label.pack(pady=10)

    def calculate_bmi(self):
        try:
            height_m = float(self.height_entry.get()) / 100
            weight = float(self.weight_entry.get())
            bmi = weight / (height_m ** 2)
            category = self.get_bmi_category(bmi)
            self.result_label.config(text=f"BMI: {bmi:.1f} ({category})")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers.")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
