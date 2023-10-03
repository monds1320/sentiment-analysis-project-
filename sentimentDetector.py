import tkinter as tk
from tkinter import messagebox

# Load positive and negative words from text files
def load_words(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file]
    return words

positive_words = load_words('positive_words.txt')
negative_words = load_words('negative_words.txt')

# Simple sentiment analysis function
def analyze_sentiment(text):
    words = text.lower().split()
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    neutral_count = len(words) - positive_count - negative_count

    total_count = len(words)
    positive_percentage = (positive_count / total_count) * 100
    negative_percentage = (negative_count / total_count) * 100
    neutral_percentage = (neutral_count / total_count) * 100

    return positive_percentage, negative_percentage, neutral_percentage

# Tkinter GUI
def analyze_button_click():
    input_text = input_textbox.get("1.0", "end-1c")
    positive_percent, negative_percent, neutral_percent = analyze_sentiment(input_text)
    result_message = (
        f"Positive: {positive_percent:.2f}%\n"
        f"Negative: {negative_percent:.2f}%\n"
        f"Neutral: {neutral_percent:.2f}%"
    )
    messagebox.showinfo("Sentiment Analysis", result_message)

# Create the main window
root = tk.Tk()
root.title("Sentiment Detector")

# Create input textbox
input_textbox = tk.Text(root, height=10, width=40)
input_textbox.pack(padx=10, pady=10)

# Create analyze button
analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_button_click)
analyze_button.pack()

# Start the GUI event loop
root.mainloop()
