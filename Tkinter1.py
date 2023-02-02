#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("500x500")
x = 0
def bgcolor():
  global x
  if x % 4 == 0:
    root.configure(bg='red')
  elif x % 4 == 1:
    root.configure(bg='green') 
  elif x % 4 == 2:
    root.configure(bg='blue')  
  elif x % 4 == 3:
    root.configure(bg='yellow')  
  x += 1
# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()
lbl_username = tk.Label(frame_login, text='Username:',font="helvetica")
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
lbl_password = tk.Label(frame_login, text="Password:",font="helvetica")
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)
btn_login = tk.Button(frame_login,text ="Login", command = bgcolor)
btn_login.pack()
root.mainloop()