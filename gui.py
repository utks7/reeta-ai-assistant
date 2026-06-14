import tkinter as tk
from tkinter import scrolledtext


class ReetaGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("REETA AI OS")
        self.root.geometry("700x500")

        # -----------------------------
        # Title
        # -----------------------------
        title = tk.Label(
            self.root,
            text="REETA AI OS",
            font=("Arial", 18, "bold")
        )

        title.pack(pady=10)

        # -----------------------------
        # Status
        # -----------------------------
        self.status_label = tk.Label(
            self.root,
            text="🟢 Status: Online",
            font=("Arial", 10)
        )

        self.status_label.pack()

        # -----------------------------
        # Chat Area
        # -----------------------------
        self.chat_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            width=80,
            height=20
        )

        self.chat_area.pack(
            padx=10,
            pady=10
        )

        # -----------------------------
        # Input Frame
        # -----------------------------
        input_frame = tk.Frame(self.root)

        input_frame.pack(pady=5)

        self.entry = tk.Entry(
            input_frame,
            width=60
        )

        self.entry.pack(
            side=tk.LEFT,
            padx=5
        )

        self.send_button = tk.Button(
            input_frame,
            text="Send"
        )

        self.send_button.pack(
            side=tk.LEFT
        )

    # -----------------------------
    # Chat Methods
    # -----------------------------

    def add_message(self, sender, message):

        self.chat_area.insert(
            tk.END,
            f"{sender}: {message}\n\n"
        )

        self.chat_area.see(tk.END)

    def add_user_message(self, message):

        self.add_message(
            "You",
            message
        )

    def add_reeta_message(self, message):

        self.add_message(
            "Reeta",
            message
        )

    # -----------------------------
    # Status
    # -----------------------------

    def set_status(self, text):

        self.status_label.config(
            text=text
        )

    # -----------------------------
    # Start GUI
    # -----------------------------

    def run(self):

        self.root.mainloop()