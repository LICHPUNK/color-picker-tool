import pyautogui
import tkinter as tk
from pynput import mouse
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog


class ColorPicker:
    def __init__(self, master):
        # Initializing GUI
        self.master = master
        master.title("Color Picker")
        master.geometry("200x100")

        # Color Label
        self.color_label = tk.Label(master, text="Click anywhere on the screen to get the color information.")
        self.color_label.pack()

        # Color Sample
        self.color_canvas = tk.Canvas(master, width=50, height=50)
        self.color_canvas.pack()

        # Quit Button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

        # Mouse Click Listener
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    # Click Method
    def on_click(self, x, y, button, pressed):
        # If left click is true...
        if pressed:
            # Retrieve color data at mouse position with Pyautogui
            color = pyautogui.pixel(x, y)
            # Pass the color data to show_color() method
            self.show_color(color)
            # Convert color data (RGB) to hexadecimal format to be copied
            hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            # Pass hexadecimal color data to copy_to_clipboard() method
            self.copy_to_clipboard(hex_color)

    # Color Update Method
    def show_color(self, color):
        # Convert color data (RGB) to hexadecimal format
        hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
        # Update GUI Color Sample
        self.color_canvas.configure(bg=hex_color)
        # Update GUI Color Label
        self.color_label.configure(text=hex_color)

    def copy_to_clipboard(self, value):
        # Clear existing clipboard
        self.master.clipboard_clear()
        # Append new color data to clipboard
        self.master.clipboard_append(value)


# Main
if __name__ == '__main__':
    root = tk.Tk()
    color_picker = ColorPicker(root)
    root.mainloop()
