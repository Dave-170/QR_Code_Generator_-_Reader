QR Code Generator and Reader

This Python application utilizes the tkinter library to create a user-friendly GUI for generating and reading QR codes. The application allows users to input data, generate QR codes, and read QR codes from image files. Additionally, users can customize the fill and background colours of the generated QR codes.

Dependencies

    tkinter
    qrcode
    Pillow (PIL)
    pyzbar
    customtkinter
    CTkColorPicker

Make sure to install these dependencies before running the application.

Usage

    Run the script to launch the QR Code Generator and Reader application.
    Enter the data you want to encode into the QR code in the provided entry field.
    Click the "Generate QR Code" button to create a QR code with the specified data.
    Optionally, you can customize the fill and background colours by using the "Choose Fill Color" and "Choose Background Color" buttons.
    To read a QR code, click the "Read QR Code" button and select an image file containing the QR code.

Features

    Generate QR Code: Create QR codes with specified data.
    Read QR Code: Decode QR codes from image files.
    Colour Customization: Choose custom fill and background colours for QR codes.

Note

Ensure that all dependencies are installed.
some QR codes can not be read based on the colours used so be careful using some colours. 

Feel free to customize and enhance the code according to your preferences and project requirements.
