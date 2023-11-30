import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import customtkinter as ctk
from CTkColorPicker import *


class QRCodeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Set the color theme
        ctk.set_default_color_theme("green")
        # Set window properties
        self.title("QR Code Generator and Reader")
        self.geometry("600x400")

        # Default colors for QR code
        self.fill_color = "black"
        self.back_color = "white"

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Entry for user to input data
        qr_label = ctk.CTkLabel(self, text="Enter data to encode in the QR code:")
        qr_label.pack(pady=10)

        self.qr_data_entry = ctk.CTkEntry(self)
        self.qr_data_entry.pack(pady=5)

        # Buttons for QR code operations
        generate_button = ctk.CTkButton(
            self, text="Generate QR Code", command=self.generate_qr_code
        )
        generate_button.pack(pady=5)

        read_button = ctk.CTkButton(
            self, text="Read QR Code", command=self.read_qr_code
        )
        read_button.pack(pady=5)

        # Buttons for choosing colors
        fill_color_button = ctk.CTkButton(
            self, text="Choose Fill Color", command=self.choose_fill_color
        )
        fill_color_button.pack(pady=5)

        back_color_button = ctk.CTkButton(
            self, text="Choose Background Color", command=self.choose_back_color
        )
        back_color_button.pack(pady=5)

        # Label to display QR code status
        self.qr_status_label = ctk.CTkLabel(self, text="", font=("Arial", 12))
        self.qr_status_label.pack(pady=10)

    def generate_qr_code(self):
        # Get user input data
        qr_data = self.qr_data_entry.get()

        if not qr_data:
            # Display an error message if no data is entered
            self.qr_status_label.configure(text="Please enter data to encode.")
            return

        # Create and save QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG Files", "*.png")]
        )

        if file_path:
            img.save(file_path)
            self.qr_status_label.configure(text=f"QR Code saved to {file_path}")

    def read_qr_code(self):
        # Read QR code from an image file
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
        )

        if not file_path:
            # Display an error message if no image is selected
            self.qr_status_label.configure(text="No image selected.")
            return

        try:
            img = Image.open(file_path)
            decoded_objects = decode(img)

            if decoded_objects:
                # Display decoded QR code data
                data = decoded_objects[0].data.decode("utf-8")
                self.qr_status_label.configure(text=f"Decoded QR Code: {data}")
            else:
                self.qr_status_label.configure(text="No QR Code found in the image.")

        except Exception as e:
            # Display error message if decoding fails
            self.qr_status_label.configure(text=f"Error decoding QR Code: {str(e)}")

    def choose_fill_color(self):
        # Open color picker for choosing fill color
        color_picker = AskColor(initial_color=self.fill_color)
        color = color_picker.get()
        if color:
            self.fill_color = color

    def choose_back_color(self):
        # Open color picker for choosing background color
        color_picker = AskColor(initial_color=self.back_color)
        color = color_picker.get()
        if color:
            self.back_color = color


# Run the application
if __name__ == "__main__":
    app = QRCodeApp()
    app.mainloop()
