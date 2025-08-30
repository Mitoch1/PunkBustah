import os
import signal
import psutil # type: ignore
from tkinter import *

def Punk_Bustah_Killa():
    k1ll("PnkBstrA.exe")
    k1ll("PnkBstrB.exe")

def k1ll(target_process):
     print(f"{target_process} is no more")

     process_list=[]

     for process in psutil.process_iter():
            process_list.append({"pid": process.pid, "name": process.name()})
            for process in process_list:
                if process["name"] == target_process:
                    os.kill(process["pid"], signal.SIGILL)




window = Tk()
button = Button(window, text= "PunkBustah")
button.config(command=Punk_Bustah_Killa)
button.pack()
window.mainloop()



