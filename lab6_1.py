import tkinter
from tkinter.filedialog import askopenfile
from tkinter import messagebox

from PIL import ImageFilter, Image, ImageOps

class Window1(tkinter.Frame):
    def __init__(self, parent):


        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tkinter.BOTH, expand=1)
        self.config(bg="#A43820")
        self.create_widgets()
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.file_path = tkinter.StringVar(value="None")

    def create_widgets(self):

        self.lb1 = tkinter.Label(self, text = "Оберіть зображення", bg="#A43820", fg = "white")
        self.btn1 = tkinter.Button(self, text = "Обрати зображення", command = self.image_choose)
        self.btn2 = tkinter.Button(self, text="Відкрити зображення у форматі 8біт", command=self.image_8bit)
        self.btn3 = tkinter.Button(self, text="Відкрити зображення з фільтром DETAIL", command=self.detailfilter_image)
        self.btn4 = tkinter.Button(self, text="Відкрити відзеркалене зображення",command=self.rotated_image)

        self.lb1.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.btn1.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.btn2.grid(row=1, column=1, sticky=tkinter.NSEW)
        self.btn3.grid(row=2, column=0, sticky=tkinter.NSEW)
        self.btn4.grid(row=2, column=1, sticky=tkinter.NSEW)



    def image_choose(self):
        f = askopenfile(mode='rb', defaultextension=".jpg",
                        filetypes=(("Image files", "*.jpg"), ("All files", "*. *")))

        if f is not None:
            full_path = f.name
            self.file_path = f.name

    def image_8bit(self):
        if self.file_path is not None:
            try:
                with Image.open(self.file_path) as img:
                    img.load()
                    img_8bit = img.convert('L')
                    img_8bit.show()
            except Exception as e:
                messagebox.showerror("Помилка", f"Файл неможливо відкрити")
        else:
            messagebox.showerror("Помилка", "Файл не обрано")

    def detailfilter_image(self):
        if self.file_path is not None:
            try:
                with Image.open(self.file_path) as img:
                    img1 = img.filter(ImageFilter.DETAIL)
                    width, height = img.size
                    img.paste((255, 0, 0), (width - 117, 9, width - 9, 86))
                    img.paste(img1, (width - 113, 10))
                    img1.show()

            except Exception as e:
                messagebox.showerror("Помилка", f"Файл неможливо відкрити")
        else:
            messagebox.showerror("Помилка", "Файл не обрано")

    def rotated_image(self):
        if self.file_path is not None:
            try:
                with Image.open(self.file_path) as img:
                    mirrored_img = ImageOps.mirror(img)
                    mirrored_img.show()

            except Exception as e:
                messagebox.showerror("Помилка", f"Файл неможливо відкрити")
        else:
            messagebox.showerror("Помилка", "Файл не обрано")







