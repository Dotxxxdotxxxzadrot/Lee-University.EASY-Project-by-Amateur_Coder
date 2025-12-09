import tkinter as tk
from tkinter import font as tkfont


class FancyTimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Timer")

        # Basic UI
        self.label = tk.Label(master, text="Enter seconds:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=10, font=("Arial", 12))
        self.entry.insert(0, "10")  # default
        self.entry.pack(pady=5)

        self.status_label = tk.Label(master, text="", font=("Arial", 10))
        self.status_label.pack(pady=5)

        self.start_button = tk.Button(master, text="Start timer", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.remaining_label = tk.Label(master, text="", font=("Arial", 14))
        self.remaining_label.pack(pady=10)

        self.remaining = 0

    def start_timer(self):
        try:
            seconds = int(self.entry.get())
            if seconds <= 0:
                raise ValueError
        except ValueError:
            self.status_label.config(text="Enter a positive integer")
            return

        self.remaining = seconds
        self.status_label.config(text="Timer running…")
        self.start_button.config(state="disabled")
        self.countdown()

    def countdown(self):
        if self.remaining > 0:
            self.remaining_label.config(text=f"{self.remaining} s left")
            self.remaining -= 1
            self.master.after(1000, self.countdown)
        else:
            self.remaining_label.config(text="Done")
            self.status_label.config(text="")
            self.start_button.config(state="normal")
            self.open_fancy_window()

    def open_fancy_window(self):
        popup = tk.Toplevel(self.master)
        popup.title("Time’s up")

        # Bigger custom font
        big_font = tkfont.Font(family="Segoe UI", size=24, weight="bold")

        popup.geometry("500x300")
        popup.configure(bg="#101820")  # dark background

        msg = tk.Label(
            popup,
            text="Time is up\nBack to the work of legends",
            font=big_font,
            fg="#FEE715",    # strong yellow
            bg="#101820",
            justify="center"
        )
        msg.pack(expand=True)

        # Small subtitle
        sub = tk.Label(
            popup,
            text="You just leveled up the boring timer into something a bit more dramatic",
            font=("Segoe UI", 11),
            fg="#F5F5F5",
            bg="#101820",
            wraplength=460,
            justify="center"
        )
        sub.pack(pady=10)

        # Start a simple background color pulse
        colors = ["#101820", "#1b2735", "#222f3e"]
        self.pulse_index = 0

        def pulse_bg():
            nonlocal colors
            popup.configure(bg=colors[self.pulse_index])
            msg.configure(bg=colors[self.pulse_index])
            sub.configure(bg=colors[self.pulse_index])
            self.pulse_index = (self.pulse_index + 1) % len(colors)
            popup.after(700, pulse_bg)

        pulse_bg()


if __name__ == "__main__":
    root = tk.Tk()
    app = FancyTimerApp(root)
    root.mainloop()