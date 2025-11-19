from tkinter import *
from src.profile_screen import ProfileScreen
from src.log_screen import LogScreen
from src.progress_screen import ProgressScreen
from src.bmi_screen import BMIScreen



SPRINGBOK_GREEN = "#006341"
SPRINGBOK_GOLD = "#FFB81C"

def main_menu():
    root = Tk()
    root.title("Fitness Tracker")
    root.geometry("600x500")
    root.configure(bg=SPRINGBOK_GREEN)

    Label(
        root,
        text="🏉 Fitness Tracker",
        font=("Arial", 24, "bold"),
        fg=SPRINGBOK_GOLD,
        bg=SPRINGBOK_GREEN
    ).pack(pady=40)

    profile_window = {"open": False}  # keeps track of window status

    def open_profile():
        if not profile_window["open"]:
            profile_window["open"] = True
            window = ProfileScreen(root)
            # when user closes it, mark as closed again
            window.window.protocol("WM_DELETE_WINDOW", lambda: close_profile(window))
        else:
            print("Profile window is already open.")

    def close_profile(window):
        profile_window["open"] = False
        window.window.destroy()

    Button(
        root,
        text="Open Profile",
        width=20,
        height=2,
        bg=SPRINGBOK_GOLD,
        fg=SPRINGBOK_GREEN,
        font=("Arial", 12, "bold"),
        command=open_profile
    ).pack(pady=10)
    
    Button(
    root,
    text="Log Workout",
    width=20,
    height=2,
    bg=SPRINGBOK_GOLD,
    fg=SPRINGBOK_GREEN,
    font=("Arial", 12, "bold"),
    command=lambda: LogScreen(root)
).pack(pady=10)
    
    Button(
    root,
    text="View Progress",
    width=20,
    height=2,
    bg=SPRINGBOK_GOLD,
    fg=SPRINGBOK_GREEN,
    font=("Arial", 12, "bold"),
    command=lambda: ProgressScreen(root)
).pack(pady=10)
    
    Button(
    root,
    text="BMI Calculator",
    width=20,
    height=2,
    bg=SPRINGBOK_GOLD,
    fg=SPRINGBOK_GREEN,
    font=("Arial", 12, "bold"),
    command=lambda: BMIScreen(root)
).pack(pady=10)


    Button(
        root,
        text="Exit",
        width=20,
        height=2,
        bg=SPRINGBOK_GOLD,
        fg=SPRINGBOK_GREEN,
        font=("Arial", 12, "bold"),
        command=root.destroy
    ).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
