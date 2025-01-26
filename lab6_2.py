import tkinter
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import numpy as np

import cv2

class Window2(tkinter.Frame):
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
        self.btn1 = tkinter.Button(self, text="Обрати зображення", command=self.choose_image)
        self.btn2 = tkinter.Button(self, text = "Відкрити зображення з режимом YUV", command =self.yuv_image)
        self.btn3 = tkinter.Button(self, text = "Відкрити зображення з проективним перетворенням ", command = self.proective_transform)
        self.btn4 = tkinter.Button(self, text="Відкрити зображення з виділенням меж zerocross ",command=self.moved_image)

        self.lb1.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.btn1.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.btn2.grid(row=1, column=1, sticky=tkinter.NSEW)
        self.btn3.grid(row=1, column=2, sticky=tkinter.NSEW)
        self.btn4.grid(row=2, column=0, sticky=tkinter.NSEW)


    def choose_image(self):
        f = askopenfile(mode='rb', defaultextension=".jpg",
                        filetypes=(("Image files", "* .jpg"), ("All files", "*. *")))

        if f is not None:
            self.file_path = f.name

    def yuv_image(self):
        if self.file_path != "None":
            try:
                img = cv2.imread(self.file_path)
                yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
                cv2.imshow("yuv_image", yuv_img)
                cv2.waitKey(0)
                cv2.destroyWindow("yuv_image")
            except Exception as e:
                messagebox.showerror("Помилка", f"Файл неможливо відкрити")
        else:
            messagebox.showerror("Помилка", "Файл не обрано")

    def proective_transform(self):
        if self.file_path != "None":
            try:
                img = cv2.imread(self.file_path)
                height, width = img.shape[:2]
                src_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
                dst_points = np.float32([[50, 50],[width - 50, 100],[0, height - 100], [width, height]])
                matrix = cv2.getPerspectiveTransform(src_points, dst_points)
                transformed_img = cv2.warpPerspective(img, matrix, (width, height))

                cv2.imshow("Проективне перетворення", transformed_img)
                cv2.waitKey(0)
                cv2.destroyWindow("Проективне перетворення")
            except Exception as e:
                messagebox.showerror("Помилка", f"Файл неможливо відкрити")
        else:
            messagebox.showerror("Помилка", "Файл не обрано")

    def moved_image(self):
        if self.file_path != "None":
             try:
                image = cv2.imread(self.file_path, cv2.IMREAD_GRAYSCALE)
                blurred = cv2.GaussianBlur(image, (5, 5), 0)
                laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
                laplacian_normalized = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)
                zero_cross = np.zeros_like(laplacian_normalized, dtype=np.uint8)
                for i in range(1, laplacian.shape[0] - 1):
                    for j in range(1, laplacian.shape[1] - 1):
                        patch = laplacian[i - 1:i + 2, j - 1:j + 2]
                        if np.min(patch) < 0 and np.max(patch) > 0:
                            zero_cross[i, j] = 255
                cv2.imshow("Zero Crossing", zero_cross)
                cv2.waitKey(0)
                cv2.destroyWindow("Zero Crossing")
             except Exception as e:
                messagebox.showerror("Помилка", f"Файл неможливо відкрити")
        else:
            messagebox.showerror("Помилка", "Файл не обрано")












