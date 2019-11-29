from tkinter import *
import time
import os
from PIL import Image

def set_main_window_size(window):
    windowWidth  = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown  = int(window.winfo_screenheight()/2 - windowHeight/2)
 
    # Positions the window in the center of the page.
    window.geometry("+{}+{}".format(positionRight, positionDown))

def set_app_background(window):
    pass

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == len(frames):
        ind = 0
    label.configure(image=frame)
    window.after(n_frames, update, ind)
    
def start_app_main_window(window):
    set_main_window_size(window)
    window.after(0, update, 0)
    window.after(0, update, 0)
    window.title("Welcome")
    
window = Tk()

gif = Image.open("48c8c036d1083c8d638ceb9deda33864.gif")
n_frames = gif.n_frames
frames = [PhotoImage(file='48c8c036d1083c8d638ceb9deda33864.gif', format = 'gif -index %i' %(i)) for i in range(n_frames)]

start_app_main_window(window)
label = Label(window)
label.pack()
window.mainloop()