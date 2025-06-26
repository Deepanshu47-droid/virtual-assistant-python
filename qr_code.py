import qrcode as qr

def qr_gen():
    img=qr.make(input("Enter link or message : "))
    img.save('qr_'+input(" Enter name of qr :")+".png")
if __name__=='__main__':
    qr_gen()