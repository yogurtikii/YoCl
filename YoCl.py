import os
import customtkinter
import time
from PIL import Image
from deep_translator import GoogleTranslator
import threading
event = threading.Event()
def sort():
    global stl, lgm
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
        if i1*w == 1:
            stl.destroy()
            stl = customtkinter.CTkLabel(mainf, text = GoogleTranslator(source='en', target=lg).translate("Files has been sorted! \n Thanks for using YoCl!"), text_color="#78f960")
            stl.pack(anchor="w", pady=10, padx=20)
def crtdir():
    content = crttext.get()
    global stl, lgm
    try:
        stl.destroy()
        os.mkdir(content)
        stl = customtkinter.CTkLabel(mainf, text = GoogleTranslator(source='en', target=lg).translate(f"Directory {content} was created! \n Thanks for using YoCl!"), text_color="#78f960")
        stl.pack(anchor="w", pady=10, padx=20)
    except FileExistsError:
        stl.destroy()
        stl = customtkinter.CTkLabel(mainf, text = GoogleTranslator(source='en', target=lg).translate("File arleady exists!"), text_color="#ff5858")
        stl.pack(anchor="w", pady=10, padx=20)
    except FileNotFoundError:
        stl.destroy()
        stl = customtkinter.CTkLabel(mainf, text = GoogleTranslator(source='en', target=lg).translate("Path not found!"), text_color="#ff5858")
        stl.pack(anchor="w", pady=10, padx=20)
def remfile():
    content = remtext.get()
    global stl, lgm
    try:
        if os.path.isdir(content):
            stl.destroy()
            stl = customtkinter.CTkLabel(mainf, text = GoogleTranslator(source='en', target=lg).translate("Cant remove directories!"), text_color="#ff5858")
            stl.pack(anchor="w", pady=10, padx=20)
        else:
            os.rmdir(content)
        stl.destroy()
        stl = customtkinter.CTkLabel(mainf, text = GoogleTranslator(source='en', target=lg).translate(f"File {content} was removed! \n Thanks for using YoCl!"), text_color="#78f960")
        stl.pack(anchor="w", pady=10, padx=20)
    except  FileNotFoundError:
        stl.destroy()
        stl = customtkinter.CTkLabel(mainf, text = GoogleTranslator(source='en', target=lg).translate("File not found!"), text_color="#ff5858")
        stl.pack(anchor="w", pady=10, padx=20)
def goto():
    global cur, stl, lgm
    target_path = gototext.get()
    try:
        os.chdir(target_path)
        cur.destroy()
        cur = customtkinter.CTkLabel(mainf, text = GoogleTranslator(source='en', target=lg).translate(f"Curent working directory: {os.getcwd()}"), text_color="#888888" )
        cur.pack(anchor="w", pady=10, padx=20)
        stl.destroy()
        stl = customtkinter.CTkLabel(mainf, text = GoogleTranslator(source='en', target=lg).translate(f"We go to {target_path} successful"), text_color="#78f960")
        stl.pack(anchor="w", pady=10, padx=20)
    except  OSError:
        stl.destroy()
        stl = customtkinter.CTkLabel(mainf, text =GoogleTranslator(source='en', target=lg).translate("Directory not found!"), text_color="#ff5858")
        stl.pack(anchor="w", pady=10, padx=20)
def lagset():
    global lgm
    if lgm.get()!="language":
        event.set()
        root.quit()
root=customtkinter.CTk()
customtkinter.set_default_color_theme("green")
root.title("YoCl 1.4.0")
root.geometry('750x500')
root.configure(fg_color="#1a1a1a")

lgl = customtkinter.CTkLabel(root, text="en-English \n ru-Русский \n de-Deutsch \n es-España \n zh-CN-中文(简体) \n ja-日本語", fg_color="#586dff")
lgl.pack(anchor="center", pady=20)
lgm = customtkinter.CTkOptionMenu(root, values=["en", "ru", "de", "es", "zh-CN", "ja"])
lgm.set("language")
lgm.pack(anchor="center", pady=100)
lgb = customtkinter.CTkButton(root, text="Set language", command=lagset, fg_color="#586dff", corner_radius=15, text_color="#1a1a1a")
lgb.pack(anchor="center", pady=20)
root.mainloop()
event.wait()
lgl.destroy()
lg=lgm.get()
lgb.destroy()
lgm.destroy()

welf = customtkinter.CTkFrame(root, fg_color="#242424", corner_radius=15)
welf.pack(pady=10, padx=20, fill="both")
    
wel = customtkinter.CTkLabel(welf, text = GoogleTranslator(source='en', target=lg).translate("Hi, its YoCl, curent version-1.4.0, it's can be bugs"), text_color="#57A3F2", font=customtkinter.CTkFont(size=18, weight="bold"))
wel.pack(pady=20, anchor="w", padx=20,side="left")

image = customtkinter.CTkImage(light_image=Image.open("photo_2026-04-25_17-42-12.png"),dark_image=Image.open("photo_2026-04-25_17-42-12.png"),size=(75, 75))
imagel = customtkinter.CTkLabel(welf, image=image, text="")
imagel.pack(anchor="e",side="left")

mainf = customtkinter.CTkFrame(root, fg_color="#242424", corner_radius=15)
mainf.pack(pady=5, padx=20, fill="both", expand=True)

sortb = customtkinter.CTkButton(mainf, text=GoogleTranslator(source='en', target=lg).translate("Click me to sort your files"), command=sort, fg_color="#f9de60", width=700, text_color="#1a1a1a", font=customtkinter.CTkFont(size=24))
sortb.pack(anchor="w", pady=20, padx=20)

crtf = customtkinter.CTkFrame(mainf, width=750, height=100,fg_color="#242424", corner_radius=15)
crtf.pack(pady=20, padx=20, fill="both")
crtb = customtkinter.CTkButton(crtf, text=GoogleTranslator(source='en', target=lg).translate("Click me to create new directory"), command=crtdir, fg_color="#586dff", corner_radius=15, text_color="#1a1a1a")
crtb.pack(anchor="s",side="left")
crttext = customtkinter.CTkEntry(crtf, placeholder_text=GoogleTranslator(source='en', target=lg).translate("Directory to create name:"), width=600, fg_color="#555555", corner_radius=15)
crttext.pack(anchor="w",side="left", padx=10)

remf = customtkinter.CTkFrame(mainf, width=750, height=100,fg_color="#242424", corner_radius=15)
remf.pack(pady=20, padx=20, fill="both")
remb = customtkinter.CTkButton(remf, text=GoogleTranslator(source='en', target=lg).translate("Click me to remove file"), command=remfile, fg_color="#ff5858", corner_radius=15, text_color="#1a1a1a")
remb.pack(anchor="s",side="left")
remtext = customtkinter.CTkEntry(remf, placeholder_text=GoogleTranslator(source='en', target=lg).translate("File to remove name:"), width=600, fg_color="#555555", corner_radius=15)
remtext.pack(anchor="s",side="left", padx=10)

gotof = customtkinter.CTkFrame(mainf, width=750, height=100,fg_color="#242424", corner_radius=15)
gotof.pack(pady=20, padx=20, fill="both")
gotob = customtkinter.CTkButton(gotof, text=GoogleTranslator(source='en', target=lg).translate("Click me to go to directory"), command=goto, text_color="#1a1a1a", corner_radius=15)
gotob.pack(anchor="s",side="left")
gototext = customtkinter.CTkEntry(gotof, placeholder_text=GoogleTranslator(source='en', target=lg).translate("Path to directory:"), width=600, fg_color="#555555", corner_radius=15)
gototext.pack(anchor="s",side="left", padx=10)

cur = customtkinter.CTkLabel(mainf, text = GoogleTranslator(source='en', target=lg).translate(f"Curent working directory: {os.getcwd()}"), text_color="#888888" )
cur.pack(anchor="w", pady=5, padx=20)


stl = customtkinter.CTkLabel(mainf, text = "...", text_color="#888888" )
stl.pack(anchor="w", pady=5, padx=20)

root.mainloop()
