import os
import customtkinter
import time
def sort():
    global stl
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
    for i in files:
        os.replace(i, os.path.join(os.path.splitext(i)[1], i))
        i1+=1
        if i1*w != 1:
            if i1 > 1:
                stl.destroy()
            stl = customtkinter.CTkLabel(mainf, text = "Completed for..." + str(i1*w).split(".")[1]+"%", text_color="#78f960")
            stl.pack(anchor="w", pady=10, padx=20)
        else:
            stl.destroy()
            stl = customtkinter.CTkLabel(mainf, text = "Completed! \n Thanks for using YoCl!", text_color="#78f960")
            stl.pack(anchor="w", pady=10, padx=20)
def crtdir():
    content = crttext.get()
    global stl
    try:
        stl.destroy()
        os.mkdir(content)
        stl = customtkinter.CTkLabel(mainf, text = f"Directory {content} was created! \n Thanks for using YoCl!", text_color="#78f960")
        stl.pack(anchor="w", pady=10, padx=20)
    except FileExistsError:
        stl.destroy()
        stl = customtkinter.CTkLabel(mainf, text = "File arleady exists!", text_color="#ff5858")
        stl.pack(anchor="w", pady=10, padx=20)
    except FileNotFoundError:
        stl.destroy()
        stl = customtkinter.CTkLabel(mainf, text = "Path not found!", text_color="#ff5858")
        stl.pack(anchor="w", pady=10, padx=20)
def remfile():
    content = remtext.get()
    global stl
    try:
        os.remove(content)
        stl.destroy()
        stl = customtkinter.CTkLabel(mainf, text = f"File {content} was removed! \n Thanks for using YoCl!", text_color="#78f960")
        stl.pack(anchor="w", pady=10, padx=20)
    except  FileNotFoundError:
        stl.destroy()
        stl = customtkinter.CTkLabel(mainf, text = "File not found!", text_color="#ff5858")
        stl.pack(anchor="w", pady=10, padx=20)
def goto():
    global cur, stl
    target_path = gototext.get()
    try:
        cur = customtkinter.CTkLabel(mainf, text = f"Curent working directory: {os.getcwd()}", text_color="#888888" )
        os.chdir(target_path)
        cur.destroy()
        cur = customtkinter.CTkLabel(mainf, text = f"Curent working directory: {os.getcwd()}", text_color="#888888" )
        cur.pack(anchor="w", pady=10, padx=20)
        stl.destroy()
        stl = customtkinker.CTkLabel(mainf, text = f"We go to {target_path} successful", text_color="#78f960")
        stl.pack(anchor="w", pady=10, padx=20)
    except  OSError:
        stl.destroy()
        stl = customtkinter.CTkLabel(mainf, text = "Directory not found!", text_color="#ff5858")
        stl.pack(anchor="w", pady=10, padx=20)
root=customtkinter.CTk()
customtkinter.set_default_color_theme("green")
root.title("YoCl 1.3.1")
root.geometry('750x500')
root.configure(fg_color="#1a1a1a")
    
wel = customtkinter.CTkLabel(root, text = "Hi, its YoCl, curent version-1.3.1, it's can be bugs", text_color="#57A3F2", font=customtkinter.CTkFont(size=24, weight="bold"))
wel.pack(pady=20)

mainf = customtkinter.CTkFrame(root, fg_color="#242424", corner_radius=15)
mainf.pack(pady=20, padx=20, fill="both", expand=True)

cur = customtkinter.CTkLabel(mainf, text = f"Curent working directory: {os.getcwd()}", text_color="#888888" )
cur.pack(anchor="w", pady=20, padx=20)

sortb = customtkinter.CTkButton(mainf, text="Click me to sort your files", command=sort, fg_color="#f9de60", width=700, text_color="#1a1a1a", font=customtkinter.CTkFont(size=24))
sortb.pack(anchor="w", pady=20, padx=20)

crtf = customtkinter.CTkFrame(mainf, width=750, height=100,fg_color="#242424", corner_radius=15)
crtf.pack(pady=20, padx=20, fill="both")
crtb = customtkinter.CTkButton(crtf, text="Click me to create new directory", command=crtdir, fg_color="#586dff", corner_radius=15, text_color="#1a1a1a")
crtb.pack(anchor="s",side="left")
crttext = customtkinter.CTkEntry(crtf, placeholder_text="Directory to create name:", width=600, fg_color="#555555", corner_radius=15)
crttext.pack(anchor="w",side="left", padx=10)

remf = customtkinter.CTkFrame(mainf, width=750, height=100,fg_color="#242424", corner_radius=15)
remf.pack(pady=20, padx=20, fill="both")
remb = customtkinter.CTkButton(remf, text="Click me to remove file", command=remfile, fg_color="#ff5858", corner_radius=15, text_color="#1a1a1a")
remb.pack(anchor="s",side="left")
remtext = customtkinter.CTkEntry(remf, placeholder_text="File to remove name:", width=600, fg_color="#555555", corner_radius=15)
remtext.pack(anchor="s",side="left", padx=10)

gotof = customtkinter.CTkFrame(mainf, width=750, height=100,fg_color="#242424", corner_radius=15)
gotof.pack(pady=20, padx=20, fill="both")
gotob = customtkinter.CTkButton(gotof, text="Click me to go to directory", command=goto, text_color="#1a1a1a", corner_radius=15)
gotob.pack(anchor="s",side="left")
gototext = customtkinter.CTkEntry(gotof, placeholder_text="Path to directory:", width=600, fg_color="#555555", corner_radius=15)
gototext.pack(anchor="s",side="left", padx=10)

stl = customtkinter.CTkLabel(mainf, text = "...", text_color="#888888" )
stl.pack(anchor="w", pady=10, padx=20)

root.mainloop()
