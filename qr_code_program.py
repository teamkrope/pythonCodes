import qrcode
from PIL import Image
import tkinter as tk

def create_qr():
    link = link_entry.get()
    img_name = img_name_entry.get()
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=4)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(f'{img_name}.png')
    status_label.config(text="QR code created successfully.")

# create the main window
root = tk.Tk()
root.title("QR Code Generator")

# create input field for link
link_label = tk.Label(root, text="Enter the link:")
link_label.pack()
link_entry = tk.Entry(root)
link_entry.pack()

# create input field for image name
img_name_label = tk.Label(root, text="Enter the image name:")
img_name_label.pack()
img_name_entry = tk.Entry(root)
img_name_entry.pack()

# create button to generate QR code
create_button = tk.Button(root, text="Create QR code", command=create_qr)
create_button.pack()

# create label to show status
status_label = tk.Label(root, text="")
status_label.pack()

# start the main loop
root.mainloop()
