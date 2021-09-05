import cv2
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


window_height = 300
window_width = 400

canvas = tk.Tk()
canvas.geometry("400x300")
canvas.title("PNG Converter")
canvas.iconbitmap('images/icon.ico')
canvas.configure(bg='gray')
canvas.resizable(False, False)
screen_width = canvas.winfo_screenwidth()
screen_height = canvas.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
canvas.geometry("{}x{}+{}+{}".format(window_width,
                window_height, x_cordinate, y_cordinate))


canvas.filename = ""


def jpeg_maker(input_path, target_format):
    if input_path == "":
        return

    output_path = os.path.splitext(input_path)[0] + target_format
    print(output_path)
    image = cv2.imread(input_path)
    cv2.imwrite(output_path, image, [
        int(cv2.IMWRITE_JPEG_QUALITY), 100])
    messagebox.showinfo(
        "Information", "File Conversion Successful! Output placed in Source folder")


def open_directory():
    canvas.filename = filedialog.askopenfilename(initialdir="C:/Users/Infinity/Documents", title="Select A File",
                                                 filetypes=(("PNG Files", "*.png"), ("all files", "*.*")))
    jpeg_maker(canvas.filename, '.jpg')


browse_button = tk.Button(canvas, text="Browse File",
                          command=open_directory, font=("SAN_SERIF", 20, "bold"))
browse_button.pack(pady=100)


canvas.mainloop()
