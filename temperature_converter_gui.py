import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        value = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            fahrenheit = (value * 9/5) + 32
            kelvin = value + 273.15
            result_label.config(
                text=f"{value}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")
        elif unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
            kelvin = celsius + 273.15
            result_label.config(
                text=f"{value}°F = {celsius:.2f}°C = {kelvin:.2f}K")
        elif unit == "Kelvin":
            celsius = value - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result_label.config(
                text=f"{value}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")
        else:
            messagebox.showerror("Invalid Unit", "Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")
root.config(bg="#e8f0fe")

heading = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"), bg="#e8f0fe")
heading.pack(pady=10)

entry_temp = tk.Entry(root, font=("Arial", 14))
entry_temp.pack(pady=5)

unit_var = tk.StringVar(value="Celsius")
unit_menu = tk.OptionMenu(root, unit_var, "Celsius", "Fahrenheit", "Kelvin")
unit_menu.config(font=("Arial", 12))
unit_menu.pack(pady=5)

convert_button = tk.Button(root, text="Convert", font=("Arial", 12), command=convert_temperature)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#e8f0fe")
result_label.pack(pady=10)

root.mainloop()
