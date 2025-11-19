from tkinter import *
from src.profile_screen import ProfileScreen
from src.log_screen import LogScreen
from src.bmi_screen import BMIScreen
from src.progress_screen import ProgressScreen

SPRINGBOK_GREEN = "#006341"
SPRINGBOK_GOLD = "#FFB81C"

def main_menu():
    root = Tk()
    root.title("🏋️‍♂️ Fitness Tracker App")
    root.geometry("400x420")
    root.configure(bg=SPRINGBOK_GREEN)

    Label(
        root,
        text="Fitness Tracker",
        font=("Arial", 22, "bold"),
        bg=SPRINGBOK_GREEN,
        fg=SPRINGBOK_GOLD
    ).pack(pady=20)

    Button(root, text="Open Profile", bg=SPRINGBOK_GOLD, fg=SPRINGBOK_GREEN,
           font=("Arial", 14, "bold"), width=20, command=lambda: ProfileScreen(root)).pack(pady=10)

    Button(root, text="Log Workout", bg=SPRINGBOK_GOLD, fg=SPRINGBOK_GREEN,
           font=("Arial", 14, "bold"), width=20, command=lambda: LogScreen(root)).pack(pady=10)

    Button(root, text="BMI Calculator", bg=SPRINGBOK_GOLD, fg=SPRINGBOK_GREEN,
           font=("Arial", 14, "bold"), width=20, command=lambda: BMIScreen(root)).pack(pady=10)

    Button(root, text="View Progress", bg=SPRINGBOK_GOLD, fg=SPRINGBOK_GREEN,
           font=("Arial", 14, "bold"), width=20, command=lambda: ProgressScreen(root)).pack(pady=10)

    Button(root, text="Exit", bg=SPRINGBOK_GOLD, fg=SPRINGBOK_GREEN,
           font=("Arial", 14, "bold"), width=20, command=root.destroy).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
