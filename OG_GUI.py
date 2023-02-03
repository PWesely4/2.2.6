#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
import tkinter.scrolledtext as tkst

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
bt_image = tk.PhotoImage(file="button.gif")
bt_image = bt_image.subsample(10,10)
frame_login = tk.Frame(root)
frame_login.pack()
lbl_username = tk.Label(frame_login, text='Username:',font="helvetica")
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
lbl_password = tk.Label(frame_login, text="Password:",font="helvetica")
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)
btn_login = tk.Button(frame_login,text ="Login", command = bgcolor,image=bt_image)
btn_login.pack()

frame1 = tk.Frame(
    master = root,
    bg = '#808000'
)
frame1.pack(fill='both', expand='yes')
editArea = tkst.ScrolledText(
    master = frame1,
    wrap   = tk.WORD,
    width  = 20,
    height = 10
)

editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
# Adding some text, to see if scroll is working as we expect it
editArea.insert(tk.INSERT,
"""\
Integer posuere erat a ante venenatis dapibus.
Posuere velit aliquet.
Aenean eu leo quam. Pellentesque ornare sem.
Lacinia quam venenatis vestibulum.
Nulla vitae elit libero, a pharetra augue.
Cum sociis natoque penatibus et magnis dis.
Parturient montes, nascetur ridiculus mus.
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
h
h
h
h
h
h
h
h
h
h
h
h
h
h
h
h
h
h
h
""")
root.mainloop()