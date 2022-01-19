from tkinter import messagebox, filedialog

messagebox.showwarning('Warning', 'file not found')
messagebox.showerror('Error', 'Division by zero')
result = messagebox.askokcancel('Continue', 'Go on?')
result = messagebox.askyesnocancel('Really', 'Want to go on?')

file_name = filedialog.askopenfilename(defaultextension='*.csv')
print(file_name)

file_names = filedialog.askopenfilenames(defaultextension="*.py")
print(file_names)
