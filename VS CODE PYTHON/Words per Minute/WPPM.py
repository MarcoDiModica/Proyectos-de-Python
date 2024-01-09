import tkinter as tk
from tkinter import messagebox
import time
import json

class WPMCalculatorApp:
    def __init__(self, root):
        self.start_time = None
        self.root = root
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack()
        self.show_scores_button = tk.Button(root, text="Show Scores", command=self.show_scores)
        self.show_scores_button.pack()
        self.load_scores()

    def load_scores(self):
        try:
            with open('scores.json', 'r') as f:
                self.scores = json.load(f)
        except FileNotFoundError:
            self.scores = []

        self.scores.sort(reverse=True)

    def show_scores(self):
        self.scores_window = tk.Toplevel(self.root)
        for i, score in enumerate(self.scores, start=1):
            row = tk.Frame(self.scores_window)
            row.pack()
            tk.Label(row, text=f"Score {i}: {score['wpm']} WPM, Total Words: {score['total_words']}, Errors: {score['errors']}").pack(side=tk.LEFT)
            tk.Button(row, text="Delete", command=lambda i=i: self.delete_score(i)).pack(side=tk.RIGHT)

    def delete_score(self, index):
        del self.scores[index - 1]
        with open('scores.json', 'w') as f:
            json.dump(self.scores, f)
        self.scores_window.destroy()
        self.show_scores()

    def start(self):
        self.start_button.pack_forget()
        self.text_widget = tk.Text(self.root, wrap=tk.WORD)
        self.text_widget.pack()
        self.text_widget.bind('<Key>', self.on_key_press)
        self.root.after(20000, self.show_wpm)  # 20 seconds

    def on_key_press(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_wpm(self):
        elapsed_time = time.time() - self.start_time
        text = self.text_widget.get("1.0", 'end-1c')
        num_words = len(text.split())
        words_per_minute = num_words / (elapsed_time / 60)
        errors = text.count('*')  # Assuming * is used to indicate an error
        return words_per_minute, num_words, errors

    def show_wpm(self):
        wpm, total_words, errors = self.calculate_wpm()
        self.scores.append({'wpm': wpm, 'total_words': total_words, 'errors': errors})
        self.scores.sort(key=lambda x: x['wpm'], reverse=True)

        with open('scores.json', 'w') as f:
            json.dump(self.scores, f)

        self.text_widget.pack_forget()

        result_label = tk.Label(self.root, text=f"You typed {wpm:.2f} words per minute. Total words: {total_words}. Errors: {errors}.")
        result_label.pack()

        retry_button = tk.Button(self.root, text="Retry", command=self.retry)
        retry_button.pack()

        menu_button = tk.Button(self.root, text="Menu", command=self.menu)
        menu_button.pack()

    def retry(self):
        self.root.destroy()
        root = tk.Tk()
        app = WPMCalculatorApp(root)
        app.start()
        root.mainloop()

    def menu(self):
        self.root.destroy()
        root = tk.Tk()
        app = WPMCalculatorApp(root)
        root.mainloop()

root = tk.Tk()
app = WPMCalculatorApp(root)
root.mainloop()