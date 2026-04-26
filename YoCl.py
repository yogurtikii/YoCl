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
            label = customtkinter.CTkLabel(root, text = "Completed for..." + str(i1*w).split(".")[1]+"%", text_color="#78f960")
            label.place(relx=0.7, rely=0.22, anchor="e")
        else:
            label.destroy()
            label = customtkinter.CTkLabel(root, text = "Completed! \n Thanks for using YoCl!", text_color="#78f960")
            label.place(relx=0.7, rely=0.22, anchor="e")
def crtdir():
    content = crttext.get()
    try:
        crtl=customtkinter.CTkLabel(root, text = "")
        if crtl != "":
            crtl.destroy()
        os.mkdir(content)
        crtl = customtkinter.CTkLabel(root, text = f"Directory {content} was created! \n Thanks for using YoCl!", text_color="#78f960")
        crtl.place(relx=0.7, rely=0.30, anchor="e")
    except FileExistsError:
        crtl=customtkinter.CTkLabel(root, text = "")
        if crtl != "":
            crtl.destroy()
        crtl = customtkinter.CTkLabel(root, text = "File arleady exists!", text_color="#ff5858")
        crtl.place(relx=0.7, rely=0.30, anchor="e")
    except FileNotFoundError:
        crtl=customtkinter.CTkLabel(root, text = "")
        if crtl != "":
            crtl.destroy()
        crtl = customtkinter.CTkLabel(root, text = "Path not found!", text_color="#ff5858")
        crtl.place(relx=0.7, rely=0.30, anchor="e")
def remfile():
    content = remtext.get()
    try:
        os.remove(content)
        reml=customtkinter.CTkLabel(root, text = "")
        if reml != "":
            reml.destroy()
        reml = customtkinter.CTkLabel(root, text = f"File {content} was removed! \n Thanks for using YoCl!", text_color="#78f960")
        reml.place(relx=0.7, rely=0.38, anchor="e")
    except  FileNotFoundError:
        reml=customtkinter.CTkLabel(root, text = "")
        if reml != "":
            reml.destroy()
        reml = customtkinter.CTkLabel(root, text = "File not found!", text_color="#ff5858")
        reml.place(relx=0.7, rely=0.38, anchor="e")
def goto():
    target_path = gototext.get()
    try:
        cur = customtkinter.CTkLabel(root, text = f"Curent working directory: {os.getcwd()}", text_color="#888888" )
        os.chdir(target_path)
        if cur != "":
            cur.destroy()
        cur = customtkinter.CTkLabel(root, text = f"Curent working directory: {os.getcwd()}", text_color="#888888" )
        cur.place(anchor="center", rely=0.9, relx=0.5)
        gotol = customtkinker.CTkLabel(root, text = f"We go to {target_path} successful", text_color="#78f960")
    except  OSError:
        gotol=customtkinter.CTkLabel(root, text = "")
        if gotol != "":
            gotol.destroy()
        gotol = customtkinter.CTkLabel(root, text = "Directory not found!", text_color="#ff5858")
        gotol.place(relx=0.7, rely=0.46, anchor="e")
root=customtkinter.CTk()
customtkinter.set_default_color_theme("green")
root.title("YoCl 1.2.0")
root.geometry('750x500')
root.configure(fg_color="#1a1a1a")
    
wel = customtkinter.CTkLabel(root, text = "Hi, its YoCl, curent version-1.2.0, it's can be bugs", text_color="#57A3F2", font=customtkinter.CTkFont(size=24, weight="bold"))
wel.pack()

cur = customtkinter.CTkLabel(root, text = f"Curent working directory: {os.getcwd()}", text_color="#888888" )
cur.place(anchor="center", rely=0.9, relx=0.5)

sortb = customtkinter.CTkButton(root, text="Click me to sort your files", command=sort, fg_color="#f9de60")
sortb.pack(anchor="w")

n = customtkinter.CTkLabel(root, text = "", )
n.pack()

crtb = customtkinter.CTkButton(root, text="Click me to create new directory", command=crtdir, fg_color="#586dff")
crtb.pack(anchor="w", side="top")
crtl = customtkinter.CTkLabel(root, text = "Directory to create name:", text_color="#888888")
crtl.pack(anchor="w")
crttext = customtkinter.CTkEntry(root, placeholder_text="Name")
crttext.place(relx=0.0, rely=0.32, anchor="w")


remb = customtkinter.CTkButton(root, text="Click me to remove file", command=remfile, fg_color="#ff5858")
remb.place(relx=0.0, rely=0.44, anchor="w")
reml = customtkinter.CTkLabel(root, text = "File to remove name:", text_color="#888888")
reml.place(relx=0.0, rely=0.50, anchor="w")
remtext = customtkinter.CTkEntry(root, placeholder_text="Name")
remtext.place(relx=0.0, rely=0.55, anchor="w")

gotob = customtkinter.CTkButton(root, text="Click me to go to directory", command=goto)
gotob.place(relx=0.0, rely=0.67, anchor="w")
gotol = customtkinter.CTkLabel(root, text = "Path to directory:", text_color="#888888")
gotol.place(relx=0.0, rely=0.73, anchor="w")
gototext = customtkinter.CTkEntry(root, placeholder_text="Path")
gototext.place(relx=0.0, rely=0.78, anchor="w")

root.mainloop()
