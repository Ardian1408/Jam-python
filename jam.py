import tkinter as tk
from tkinter import filedialog
import time
from PIL import ImageTk, Image

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

def change_background():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        try:
            image = Image.open(file_path)
            resized_image = image.resize((800, 400), Image.ANTIALIAS)
            background_image = ImageTk.PhotoImage(resized_image)
            background_label.config(image=background_image)
            background_label.image = background_image
        except:
            tk.messagebox.showerror("Error", "Failed to open the selected image.")

# Membuat jendela utama
window = tk.Tk()
window.title("Jam Digital")

# Mengatur latar belakang
default_image = Image.open("default_background.png")
resized_default_image = default_image.resize((800, 400), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(resized_default_image)
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Tombol untuk mengubah latar belakang
change_background_button = tk.Button(window, text="Change Background", command=change_background)
change_background_button.pack(pady=10)

# Membuat label untuk menampilkan jam
clock_label = tk.Label(window, font=("Arial", 80))
clock_label.pack(padx=50, pady=50)

# Memanggil fungsi update_clock() untuk pertama kali
update_clock()

# Menjalankan program utama
window.mainloop()
