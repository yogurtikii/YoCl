import os
import customtkinter
import time
def sort():
    files=os.listdir()
    temp=""
    extistons=[]
    w=0
    w=1/len(files)
    i1=0
    for i in files:
        temp=os.path.splitext(i)
        temp=temp[1]
        extistons.append(temp)
    extistons=set(extistons)
    extistons=list(extistons)
    for i in extistons:
        if i != "":
            os.makedirs(i, exist_ok=True)
        else:
            os.makedirs("Nothing", exist_ok=True)
    for i in files:
        os.replace(i, os.path.join(os.path.splitext(i)[1], i))
        i1+=1
        if i1*w != 1:
            if i1 > 1:
                label.destroy()
            label = customtkinter.CTkLabel(root, text = "Completed for..." + str(i1*w, 2).split(".")[1]+"%" )
            label.place(relx=0.4, rely=0.2, anchor="e")
        else:
            label.destroy()
            label = customtkinter.CTkLabel(root, text = "Completed! \n Thanks for using YoCl!")
            label.place(relx=0.4, rely=0.22, anchor="e")
            time.sleep(2)
            label.destroy()
def crtdir():
    content = textbox.get("1.0", "end-1c")
    try:
        os.mkdir(content)
        label = customtkinter.CTkLabel(root, text = f"Directory {content} was created! \n Thanks for using YoCl!", )
        label.pack()
        time.sleep(2)
        label.destroy()
    except FileExistsError:
        label = customtkinter.CTkLabel(root, text = "File arleady exists!", )
        label.pack()
        time.sleep(2)
        label.destroy()
def remfile():
    content = textbox.get("1.0", "end-1c")
    try:
        os.remove(content)
        label = customtkinter.CTkLabel(root, text = f"File {content} was removed! \n Thanks for using YoCl!", )
        label.pack()
        time.sleep(2)
        label.destroy()
    except  FileNotFoundError:
        label = customtkinter.CTkLabel(root, text = "File not found!", )
        label.pack()
        time.sleep(2)
        label.destroy()
root=customtkinter.CTk()
customtkinter.set_default_color_theme("green")
root.title("YoCl 1.1.0")
root.geometry('750x500')
root.configure(fg_color="#b1b1b1")
    
label = customtkinter.CTkLabel(root, text = "Hi, its YoCl, curent version-1.1.0, it's can be bugs", text_color="#90ee90")
label.pack()

label = customtkinter.CTkLabel(root, text = f"Curent working directory: {os.getcwd()}", text_color="#90ee90" )
label.pack()

button = customtkinter.CTkButton(root, text="Click me to sort your files", command=sort)
button.pack(anchor="w")

label = customtkinter.CTkLabel(root, text = "", )
label.pack()

button = customtkinter.CTkButton(root, text="Click me to create new directory", command=crtdir)
button.pack(anchor="w", side="top")
label = customtkinter.CTkLabel(root, text = "Directory to create name:", text_color="#90ee90")
label.pack(anchor="w")
textbox = customtkinter.CTkTextbox(root, width=200, height=10, corner_radius=10, border_width=2)
textbox.place(relx=0.0, rely=0.37, anchor="w")
textbox.insert("1.0", "")

button = customtkinter.CTkButton(root, text="Click me to remove file", command=remfile)
button.place(relx=0.0, rely=0.49, anchor="w")
label = customtkinter.CTkLabel(root, text = "File to remove name:", text_color="#90ee90")
label.place(relx=0.0, rely=0.54, anchor="w")
textbox = customtkinter.CTkTextbox(root, width=200, height=10, corner_radius=10, border_width=2)
textbox.place(relx=0.0, rely=0.60, anchor="w")
textbox.insert("1.0", "")

root.mainloop()
