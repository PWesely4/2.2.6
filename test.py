import tkinter as tk
import tkinter.scrolledtext as tkst

root = tk.Tk()
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
""")
root.mainloop()