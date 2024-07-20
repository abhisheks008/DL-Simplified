from tkinter import *
from PIL import ImageTk, Image
import subprocess
root = Tk()
def hide_window():
 root.destroy()
root.protocol("WM_DELETE_WINDOW", hide_window) # Hide window when close button is clicked
root.maxsize(width=800, height=600)
root.title("Face Recognition System")
root.geometry("800x600")
#image = Image.open("C:/Users/Lenovo/Downloads/ML_PROJECT CUMMINS zip/ML_PROJECT CUMMINS/backbg.jpg")
#background_image = ImageTk.PhotoImage(image)
#background_label = Label(root, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

image = Image.open("imagebasic/bg.jpg") # Replace "path_to_image_file.jpg" with the actual path to your
#image file
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()),)
background_image = ImageTk.PhotoImage(image)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

UpdateDelay = 400
s = 'Welcome Face Recognition System'
s_index = 0
def update():
 global s_index
 double = s + ' ' + s
 display = double[s_index:s_index+30]
 l.config(text=display)
 s_index += 1
 if s_index >= len(double) // 2:
   s_index = 0
 root.after(UpdateDelay, update)
l = Label(root, text='Welcome Face Recognition System', font="Calibri 18 bold",
bg='#CAEBF0')
l.place(x=250, y=100)
root.after(UpdateDelay, update)
def open_new_window():
 root.destroy() # Close the first window
 subprocess.run(["python", "gui.py"]) # Open the new window
jumpbtn = Button(root, text="Get Started", padx=40, pady=20, command=open_new_window,bg='#CAEBF0', borderwidth=0, font="Times 14 bold")
jumpbtn.place(x=300, y=250)
root.mainloop()


from tkinter import *
from tkinter import *
from PIL import ImageTk, Image
import subprocess
# Create the Tkinter window
window =Tk()
window.title("Face Recognition")
window.geometry("800x600")
image = Image.open("imagebasic/bg.jpg") # Replace "path_to_image_file.jpg" with the actual path to your
#image file
image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()),
Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Create a button widget
button = Button(window, padx=40, pady=20,text="For Recognition",
bg='#CAEBF0',command=lambda: subprocess.run(["python", "program.py"]))
button .place(x=200,y=250)
button1 =Button(window,padx=40, pady=20, text="For Attendance", bg='#CAEBF0', command=lambda:
subprocess.run(["python", "DeepFace.py"]))
button1 .place(x=400,y=250)
# Start the Tkinter event loop


window.mainloop()