import Tkinter
import urllib

from PIL import Image , ImageTk

canvas_width = 300
canvas_height =300

master = Tkinter.Tk()

canvas = Tkinter.Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()
im = urllib.urlopen('http://images.performgroup.com/di/library/GOAL/b0/fc/lionel-messi_3zemoxd9wn0z1bo2elz1frf4d.jpg?t=-219236414&w=620&h=430').read()

im = im.convert('RGB')
im.save('Apple.pgm')
img = Tkinter.PhotoImage(file="Apple.pgm")
canvas.create_image(20,20, image=img)

master.mainloop()