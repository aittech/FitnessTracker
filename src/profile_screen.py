from tkinter import *
import csv, os

SPRINGBOK_GREEN = "#006341"
SPRINGBOK_GOLD = "#FFB81C"

class ProfileScreen:
    def __init__(self, root):
        self.root = root
        self.window = Toplevel(self.root)
        self.window.title("User Profile")
        self.window.geometry("400x400")
        self.window.configure(bg=SPRINGBOK_GREEN)

        # Heading
        Label(
            self.window,
            text="User Profile",
            font=("Arial", 18, "bold"),
            fg=SPRINGBOK_GOLD,
            bg=SPRINGBOK_GREEN
        ).pack(pady=10)

        # Input fields
        self.name_entry = self.add_field("Name")
        self.age_entry = self.add_field("Age")
        self.height_entry = self.add_field("Height (cm)")
        self.weight_entry = self.add_field("Weight (kg)")

        Label(
            self.window,
            text="Goal",
            fg=SPRINGBOK_GOLD,
            bg=SPRINGBOK_GREEN
        ).pack()
        self.goal_var = StringVar(value="Lose Weight")
        OptionMenu(self.window, self.goal_var, "Lose Weight", "Build Muscle", "Stay Fit").pack()

        self.load_profile()

        Button(
            self.window,
            text="Save Profile",
            bg=SPRINGBOK_GOLD,
            fg=SPRINGBOK_GREEN,
            font=("Arial", 12, "bold"),
            command=self.save_profile
        ).pack(pady=10)

        self.status_label = Label(self.window, text="", fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN)
        self.status_label.pack()

    def add_field(self, label_text):
        Label(self.window, text=label_text, fg=SPRINGBOK_GOLD, bg=SPRINGBOK_GREEN).pack()
        entry = Entry(self.window, fg=SPRINGBOK_GREEN, bg="white", width=25)
        entry.pack(pady=2)
        return entry

    def save_profile(self):
        file_path = "data/profile.csv"
        with open(file_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Age", "Height", "Weight", "Goal"])
            writer.writeheader()
            writer.writerow({
                "Name": self.name_entry.get(),
                "Age": self.age_entry.get(),
                "Height": self.height_entry.get(),
                "Weight": self.weight_entry.get(),
                "Goal": self.goal_var.get()
            })
        self.status_label.config(text="Profile saved successfully!")

    def load_profile(self):
        file_path = "data/profile.csv"
        if os.path.exists(file_path):
            with open(file_path, newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.name_entry.insert(0, row["Name"])
                    self.age_entry.insert(0, row["Age"])
                    self.height_entry.insert(0, row["Height"])
                    self.weight_entry.insert(0, row["Weight"])
                    self.goal_var.set(row["Goal"])
                    break
