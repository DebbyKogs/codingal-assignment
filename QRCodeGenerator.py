#import qrcode
#class QRCodeGenerator:
    #def __init__(self):
       ## qr = qrcode.QRCode()
        #qr.add_data(data)
        #qr.make()
        #img = qr.make_image()
        #fileName = input("enter file name:")
        #img.save(fileName+".png")
#ob1 = QRCodeGenerator()
#ob1.createQRImage()

file = open("note.txt","r")

content = file.read()

print(content)