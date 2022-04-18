from tkinter import *
root=Tk()
root.configure(background="black")

def send():
    send="User-> "+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=="hi"):
        txt.insert(END,"\n"+"         simran-hlo😇")
        
    elif (e.get()=="how are you?"):
        txt.insert(END,"\n"+"         simran->I'm fine,and you?")

    elif (e.get()=="i am also good"):
        txt.insert(END,"\n"+"         simran->what are you doing\?")
        
    elif (e.get()=="oh"):
        txt.insert(END,"\n"+"         simran->hm😀 ") 

    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="SEND",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Chatbot")
root.mainloop() 

