import pygame
import tkinter as tk
from tkinter import filedialog
import time
from PIL import Image, ImageTk

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

def drag_start(event):
    # Menyimpan posisi awal saat penyeretan dimulai
    canvas.data = {'x': event.x, 'y': event.y}

def drag_move(event):
    # Menghitung perubahan posisi saat penyeretan berlangsung
    dx = event.x - canvas.data['x']
    dy = event.y - canvas.data['y']

    # Memindahkan tampilan jam sesuai dengan perubahan posisi
    canvas.move(clock_text, dx, dy)

    # Memperbarui posisi awal untuk iterasi berikutnya
    canvas.data['x'] = event.x
    canvas.data['y'] = event.y

def resize(event):
    # Mengubah ukuran tampilan jam sesuai dengan ukuran persegi panjang
    canvas.itemconfigure(clock_text, font=('Arial', event.width // 10))

def change_background():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        try:
            pygame.init()
            screen = pygame.display.set_mode((800, 400))
            background = pygame.image.load(file_path)

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONUP:
                        width, height = background.get_size()
                        image = Image.open(file_path)
                        resized_image = image.resize((width, height), Image.ANTIALIAS)
                        background_image = ImageTk.PhotoImage(resized_image)
                        background_label.config(image=background_image)
                        background_label.image = background_image
                        running = False

                screen.blit(background, (0, 0))
                pygame.display.flip()

            pygame.quit()
        except:
            tk.messagebox.showerror("Error", "Failed to open the selected image.")

def change_clock_position():
    new_x = int(input("Masukkan koordinat X baru: "))
    new_y = int(input("Masukkan koordinat Y baru: "))
    clock_label.place(x=new_x, y=new_y)  # Mengubah posisi tampilan jam

# Membuat jendela utama
window = tk.Tk()
window.title("Jam Digital")

# Membuat canvas
canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

# Membuat persegi panjang sebagai kontrol untuk mengubah ukuran jam
resize_rect = canvas.create_rectangle(500, 300, 600, 400, fill='gray', tags='resize')
canvas.tag_bind('resize', '<B1-Motion>', resize)

# Membuat label untuk menampilkan jam
clock_text = canvas.create_text(300, 200, text='', font=('Arial', 60), anchor='center')

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

# Tombol untuk mengubah posisi tampilan jam
change_position_button = tk.Button(window, text="Change Clock Position", command=change_clock_position)
change_position_button.pack()

# Memanggil fungsi update_clock() untuk pertama kali
update_clock()

# Menjalankan program utama
window.mainloop()
