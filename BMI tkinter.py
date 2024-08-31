import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = (weight * 703) / (height * height)
        bmi = round(bmi, 2)
        name = name_entry.get()
        
        if bmi < 18.5:
            result = f"{name}, your BMI is {bmi}. You are underweight."
        elif 18.5 <= bmi <= 24.9:
            result = f"{name}, your BMI is {bmi}. You are normal weight."
        elif 25 <= bmi < 29.9:
            result = f"{name}, your BMI is {bmi}. You are overweight. You need to exercise more and stop sitting and writing so many python tutorials."
        elif 30 <= bmi < 34.9:
            result = f"{name}, your BMI is {bmi}. You are obese."
        elif 35 <= bmi < 39.9:
            result = f"{name}, your BMI is {bmi}. You are severely obese."
        else:
            result = f"{name}, your BMI is {bmi}. You are morbidly obese."
        
        messagebox.showinfo("BMI Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

def center_window(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Set window size and center it
root.geometry("400x250")
center_window(root)

# Set background color
root.configure(bg="#ADD8E6")  # Light blue background

# Create and place the labels and entry widgets
tk.Label(root, text="Enter your name:", bg="#ADD8E6", fg="#000000", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your weight (in pounds):", bg="#ADD8E6", fg="#000000", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your height (in inches):", bg="#ADD8E6", fg="#000000", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the Calculate button with style
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="#FFFFFF", font=("Arial", 12, "bold"))
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
