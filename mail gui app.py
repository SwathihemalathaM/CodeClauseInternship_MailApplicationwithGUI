from tkinter import *
from tkinter import messagebox
import smtplib 


root = Tk()
root.title('GUI Email Application')
root.geometry('300x400')
root.resizable(False,False)
root.config(background='pink')



def send():
    Email = temp_Email.get()
    Password = temp_Password.get()
    SenderId = temp_SenderId.get()
    Subject = temp_Subject.get()
    Body = temp_Body.get()

    if Email or Password or SenderId or Subject or Body:
        message = 'Subject: {}\n\t{}'.format(Subject,Body)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(Email,Password)
        server.sendmail(Email,SenderId,message)
        messagebox.Message(root,text='Email has been sent')



def reset():
    Email_entry.delete(0,END)
    Password_entry.delete(0,END)
    Sender_entry.delete(0,END)
    Subject_entry.delete(0,END)
    Body_entry.delete(0,END)


Label(root,text='Email App', font=('verdana',20),fg='blue',bg='pink').grid(row=0,padx=15, columnspan=2)
Label(root,text='fill the following details', font=('calibri',12),background='pink').grid(row=1,padx=2,pady=10, columnspan=2)
Label(root,text='Email ID',font=('Arial',12),bg='pink').grid(row=2,padx=2)
Label(root,text='Password',font=('Arial',12),bg='pink').grid(row=3,padx=2)
Label(root,text='Sender ID',font=('Arial',12),bg='pink').grid(row=4,padx=2)
Label(root,text='Subject',font=('Arial',12),bg='pink').grid(row=5,padx=2)
Label(root,text='Body',font=('Arial',12),bg='pink').grid(row=6,padx=2)


temp_Email = StringVar()
temp_Password = StringVar()
temp_SenderId = StringVar()
temp_Subject = StringVar()
temp_Body = StringVar()


Email_entry = Entry(root, textvariable=temp_Email)
Email_entry.grid(row=2, column=1,ipadx=25)
Password_entry = Entry(root, textvariable=temp_Password, show='*')
Password_entry.grid(row=3, column=1,ipadx=25)
Sender_entry = Entry(root, textvariable=temp_SenderId)
Sender_entry.grid(row=4, column=1,ipadx=25)
Subject_entry = Entry(root, textvariable=temp_Subject)
Subject_entry.grid(row=5, column=1,ipadx=25)
Body_entry = Entry(root, textvariable=temp_Body)
Body_entry.grid(row=6, column=1,ipadx=25)

Button(root,text='SEND', command=send).grid(row=7,column=1,padx=40,pady=20,ipadx=10)
Button(root,text='RESET', command=reset).grid(row=8,column=1,padx=40,ipadx=15)




root.mainloop()