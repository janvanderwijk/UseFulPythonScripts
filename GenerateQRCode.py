
import qrcode
from tkinter import *
from tkinter import messagebox
def reset():
    webEntry.delete(0,END)
    webEntry.config(bg='white')
    QR.config(image='',text='',width=20,height=20)
   
def QRCode():
    website = webEntry.get()
    try:
        web = website.split('.')
        if website.startswith('www.') or website.endswith('.com'):
            fileName = web[1]+'.jpg'
        else:
            fileName = web[0]+'.jpg'
    except:
        fileName = website
#============Now generate and save qr code================
    if len(website)<1:
        messagebox.showwarning('Warning!','Enter your website or mobile no. first.\n\t in entry box')
        webEntry.config(bg='red2')
        QR.config(text='There is an error occured in Generating QR Code',image='',
                  width=40,height=40,fg='red')
    else:
        img = qrcode.make(website)
        img.save(fileName)
        root.photo = PhotoImage(file=fileName)
        QR.config(image=root.photo,text='QR Code Generated Successfully!',
                  fg='green',compound=TOP,width=300,height=300)
        messagebox.showinfo('Saved','QR code saved as " '+fileName+' " successfully!\n\tin current location')

#===============  GUI Design ================================   
root = Tk()
root.title('QR Code Generator')
root.config(bg='plum1')
root.geometry('520x550')
root.resizable(0,0)
try:
    root.wm_iconbitmap('cid.ico')
except:
    pass
appName = Label(root,text='QR CODE GENERATOR',bg='black',fg='blue',
                font=('forte',25,'underline','bold','italic'))
appName.pack(side=TOP,fill=BOTH)
website = Label(root,text="Enter Website/Mobile Name:",font=('impact',10))
website.place(x=10,y=72)
webEntry = Entry(root,fg='blue',bd=3,width=40)
webEntry.place(x=170,y=70)
getQRCode = Button(root,text='get QR Code',bg='green',fg='white',activebackground='blue',
                   width=30,activeforeground='yellow',command=QRCode)
getQRCode.place(x=180,y=100)
'''
showImage= Button(root,text='Show QR Code in Photos App',fg='green',activebackground='blue',
                  width=30,command=showQR)
showImage.place(x=180,y=140)
'''
resetApp= Button(root,text='Reset',bg='black',fg='white',
                 width=15,bd=3,command=reset)
resetApp.place(x=435,y=500)
QR = Label(root,image='',bg='plum1')
QR.place(x=100,y=170)
        
copyri8 = Label(root,text='bit.ly/github_janvanderwijk [2020]',
                bg='plum1',fg='red3',font=('arial',10,'bold'))
copyri8.pack(side=BOTTOM)
root.mainloop()