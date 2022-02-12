from tkinter import messagebox, ttk
import tkinter as tk
import os
from tkinter.filedialog import askopenfilename
from pathlib import Path


root = tk.Tk()
root.title('V icon adder')
root.resizable(False, False)
root.attributes('-toolwindow', True)
root.attributes('-topmost', True)


def process_compile():
    btn_process.configure(text='Generating .exe ...')
    path = os.path.split(v_file)[0]
    print(path)
    name = Path(v_file).stem
    with open(path+'/'+name+'.rc', 'w')as f:
        f.write('id ICON "'+icon_file+'"')
    command = 'cmd /c windres '+name+'.rc '+name+'.o'
    os.chdir(path)
    os.system(command)
    command = 'cmd /c v -showcc -cc gcc -cflags "-I'+path+' '+path+'/'+name+'.o" '+name+'.v'
    os.system(command)
    btn_process.configure(text='Generate .exe')
    messagebox.showinfo('Info', 'Icon added with success !')


def browse_v():
    global v_file
    v_file = askopenfilename()
    entry_vcode.insert(0, v_file)


def browse_icon():
    global icon_file
    icon_file = askopenfilename()
    entry_icon.insert(0, icon_file)
    icon_file = icon_file.replace('/', '//')


frm1 = ttk.Frame(root)
frm1.pack(anchor='nw')

ttk.Label(frm1, text='V file :').pack(anchor='nw', padx=10, pady=10)

entry_vcode = ttk.Entry(frm1)
entry_vcode.pack(anchor='nw', side='left', padx=10)

ttk.Button(frm1, text='Browse', command=browse_v).pack(anchor='ne', side='right', padx=10)


frm2 = ttk.Frame(root)
frm2.pack(anchor='nw')

ttk.Label(frm2, text='Icon :').pack(anchor='nw', padx=10, pady=10)

entry_icon = ttk.Entry(frm2)
entry_icon.pack(anchor='nw', side='left', padx=10)

ttk.Button(frm2, text='Browse', command=browse_icon).pack(anchor='ne', side='right', padx=10)


btn_process = ttk.Button(root, text='Generate .exe', command=process_compile)
btn_process.pack(anchor='s', pady=10)


root.mainloop()
