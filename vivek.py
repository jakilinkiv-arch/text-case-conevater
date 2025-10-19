import tkinter as tk
from tkinter import ttk

def to_upper():
    text = input_text.get("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text.upper())

def to_lower():
    text = input_text.get("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text.lower())

def to_title():
    text = input_text.get("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text.title())

root = tk.Tk()
root.title("Text Case Converter")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input text box
ttk.Label(frame, text="Input:").grid(row=0, column=0, sticky=tk.W)
input_text = tk.Text(frame, width=40, height=5)
input_text.grid(row=1, column=0, columnspan=3, pady=5)

# Buttons
ttk.Button(frame, text="UPPERCASE", command=to_upper).grid(row=2, column=0, padx=5)
ttk.Button(frame, text="lowercase", command=to_lower).grid(row=2, column=1, padx=5)
ttk.Button(frame, text="Title Case", command=to_title).grid(row=2, column=2, padx=5)

# Output text box
ttk.Label(frame, text="Output:").grid(row=3, column=0, sticky=tk.W)
output_text = tk.Text(frame, width=40, height=5)
output_text.grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()