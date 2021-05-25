import qrcode
import image

qr = qrcode.QRCode(
    # version 15 means this is the qrcode version: high the number then bigger is the code image genrated and the complicated the image is.
    version=15,
    # box size 10 here means the size of the box where the image will be displayed
    box_size=10,
    # this border will provide white spacing for all the 4 sides of the image.
    border=5,
)

# in this data either u can put any link where u wish this qr code to work or can normally write any text between the quotes
data = "Generating QrCode"

qr.add_data(data)  # this addes the data to the qr modules
qr.make(fit=True)  # this enquires that the dimension of the qr code is in use
img = qr.make_image(
    fill="black", back_color="green"
)  # this specify the foreground and the background color of the qrcode (black and white)
img.save(
    "test1.png"
)  # this function stores the image in the .png format to the current directory
