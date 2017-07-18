import Tkinter


master=Tkinter.Tk()
print 'hello'
def test(i):
    Tkinter.Label(master,text='hello'+i).grid(row=0,column=0)

but =Tkinter.Button(master,text='show',command=lambda :test('my') ).grid(row=1,column=1)

master.mainloop()


