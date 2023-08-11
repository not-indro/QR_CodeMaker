import qrcode
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


class QrCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Maker by Astraa")
        self.root.geometry('600x450')

        self.create_widgets()

    def create_qr_code(self):
        data = self.text_entry.get()
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            qr_image = qr.make_image(
                fill_color="black", back_color="white").convert('RGB')
            qr_image.save("qr_code.png")

            self.convert_button['state'] = tk.DISABLED
            self.show_qr_code()

        else:
            messagebox.showerror(
                "Error", "Please enter text/link before converting.")

    def show_qr_code(self):
        qr_image = Image.open("qr_code.png")
        resized_image = qr_image.resize((200, 200))
        self.qr_code_photo = ImageTk.PhotoImage(resized_image)
        self.qr_code_label.config(image=self.qr_code_photo)

    def reset(self):
        self.text_entry.delete(0, tk.END)
        self.qr_code_label.config(image="")
        self.convert_button['state'] = tk.NORMAL

    def create_widgets(self):
        title_label = tk.Label(
            self.root, text='QR Code Generator', font=("bold", 24))
        title_label.place(x=180, y=20)

        description_label = tk.Label(
            self.root, text='Enter your Text/Link and click "Convert" to generate a QR Code:', font=("Helvetica", 12))
        description_label.place(x=70, y=80)

        self.text_entry = ttk.Entry(self.root, width=60)
        self.text_entry.place(x=70, y=120)

        self.convert_button = ttk.Button(
            self.root, text='Convert', command=self.create_qr_code)
        self.convert_button.place(x=70, y=160)

        reset_button = ttk.Button(self.root, text='Reset', command=self.reset)
        reset_button.place(x=180, y=160)

        self.qr_code_label = tk.Label(self.root)
        self.qr_code_label.place(x=350, y=80)


if __name__ == "__main__":
    root = tk.Tk()
    app = QrCodeGeneratorApp(root)
    root.mainloop()
