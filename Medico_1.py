
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
#https://www.figma.com/file/IAeIXTDNhMZGxLJ1I7SzSP/SE?node-id=7%3A37&t=P3cpcqN1YLgKBAgp-1
#figd_jSS3V4xYU4OSjT9lVirWXLGWpuEklIoD4DFWtO2-
import matplotlib.pyplot as plt
import numpy as np
from fuzzy_expert.variable import FuzzyVariable
from fuzzy_expert.rule import FuzzyRule
from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Juan Pablo Salazar\Desktop\latex\Gestion\build\assets\frame0")

enfer=""
reco=""
z=0
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("850x480")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 453,
    width = 832,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    154.9456787109375,
    16.98492431640625,
    anchor="nw",
    text="Bienvenido a doctor Simi Similar!",
    fill="#000000",
    font=("Inter Bold", 32 * -1)
)

canvas.create_text(
    187.12762451171875,
    67.0457763671875,
    anchor="nw",
    text="Donde nuestro sistema le ayudara a diagnosticar sus enfermedades, asi sabra si es una enfermedad comun o es algo que necesita ser tratado por alguien con mas conocimientos que este sistema ",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    13.7025146484375,
    152.8643798828125,
    anchor="nw",
    text="Instrucciones: \n1)Ingrese su informacion y seleccione todos los sintomas que coincidan con su padecimiento actual \n2)Presione el boton “Enviar” para proceder con su diagnostico\n3)Según el resultado, tome las precauciones recomendadas ",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    5.401611328125,
    262.0,
    anchor="nw",
    text="Seleccione su edad:",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)
EDAD=Scale(window,from_=0, to=150,orient=HORIZONTAL)
EDAD.place(x=150,y=250)

canvas.create_text(
    3.401611328125,
    400.0000305175781,
    anchor="nw",
    text="Seleccione su altura:",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)
altura=Scale(window,from_=1, to=250,orient=HORIZONTAL)
altura.place(x=150,y=400)


canvas.create_text(
    390.401611328125,
    233.0,
    anchor="nw",
    text="Sintomas:",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    5.401611328125,
    227.0,
    anchor="nw",
    text="Informaacion personal:",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

canvas.create_text(
    5.401611328125,
    320.99998474121094,
    anchor="nw",
    text="Seleccione su peso:",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)
peso=Scale(window,from_=1, to=250,orient=HORIZONTAL)
peso.place(x=150,y=320)


image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    70.65704345703125,
    78.98492431640625,
    image=image_image_1
)

canvas.create_rectangle(
    367.018798828125,
    220.80638122558594,
    369.28369140625,
    449.0,
    fill="#000000",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    769.781681060791,
    79.4697265625,
    image=image_image_2
)

canvas.create_rectangle(
    -0.2798747420310974,
    141.3332844376564,
    833.9615478515625,
    143.92495727539062,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -0.27987462282180786,
    219.92366236448288,
    833.9613037109375,
    220.8041229248047,
    fill="#000000",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    820.9337921142578,
    182.3645477294922,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=811.1004104614258,
    y=166.2735595703125,
    width=19.666763305664062,
    height=30.181976318359375
)

################################de mi cosecha #######################################################
tos=tk.BooleanVar()
fiebre=tk.BooleanVar()
DolorCa=tk.BooleanVar()
CuerpoCu=tk.BooleanVar()
DolorG=tk.BooleanVar()
Congestion_N=tk.BooleanVar()
#Var der
Perdida_ol=tk.BooleanVar()
Moqueo=tk.BooleanVar()
Irri_ojos=tk.BooleanVar()
Dif_res=tk.BooleanVar()
Flemas=tk.BooleanVar()
Escalo=tk.BooleanVar()
DolorA=tk.BooleanVar()
#Impresion izq
tos1= tk.Checkbutton(window, text="tos",variable=tos).place(x=417,y=257)
fiebre1= tk.Checkbutton(window, text="fiebre",variable=fiebre).place(x=417,y=287)
DolorCa1= tk.Checkbutton(window, text="Dolor Cabeza",variable=DolorCa).place(x=417,y=317)
CuerpoC1= tk.Checkbutton(window, text="Cuerpo Cortado",variable=CuerpoCu).place(x=417,y=347)
DolorG1= tk.Checkbutton(window, text="Dolor de gargata",variable=DolorG).place(x=417,y=377)
Congestion_N1= tk.Checkbutton(window, text="Congestion Nasal",variable=Congestion_N).place(x=417,y=407)
#Impresion der
P_ol1= tk.Checkbutton(window, text="Perdida olfato",variable=Perdida_ol).place(x=647,y=257)
MocoV1= tk.Checkbutton(window, text="Moqueo",variable=Moqueo).place(x=647,y=287)
irri1= tk.Checkbutton(window, text="Irritacion de ojos",variable=Irri_ojos).place(x=647,y=317)
Dif=tk.Checkbutton(window, text="Dificultad para respirar",variable=Dif_res).place(x=647,y=347)
Flemas1= tk.Checkbutton(window, text="Flemas",variable=Flemas).place(x=647,y=377)
Escalo1= tk.Checkbutton(window, text="Escalofrios",variable=Escalo).place(x=647,y=407)
DolorA1= tk.Checkbutton(window, text="Dolor Articulaciones",variable=DolorA).place(x=647,y=437)



database = [
    {"nombre":"Resfriado", "Perdida olfato":False, "Escalofrios":False, "Dolor articulacion":False, "Dificultad para respirar":False, "Tos":True, "Fiebre":False, "Congestion Nasal":True , "Secrecion":True, "Dolor Garganta":True, "Irritacion de ojos":False, "Dolor Cabeza":False,"Dolor de cuerpo":True,"Flemas":True},

    {"nombre": "Gripe", "Perdida olfato":False, "Escalofrios":False, "Dolor articulacion":False, "Dificultad para respirar":False, "Tos":True, "Fiebre":True, "Congestion Nasal":True , "Secrecion":True, "Dolor Garganta":True, "Irritacion de ojos":True, "Dolor Cabeza":True,"Dolor de cuerpo":True,"Flemas":True},

    {"nombre": "Influenza", "Perdida olfato":False, "Escalofrios":False, "Dolor articulacion":True, "Dificultad para respirar":True, "Tos":True, "Fiebre":True, "Congestion Nasal":True , "Secrecion":True, "Dolor Garganta":True, "Irritacion de ojos":True, "Dolor Cabeza":True,"Dolor de cuerpo":True,"Flemas":True},

    {"nombre": "COVID", "Perdida olfato":True, "Escalofrios":True, "Dolor articulacion":False, "Dificultad para respirar":False, "Tos":True, "Fiebre":True, "Congestion Nasal":True , "Secrecion":True, "Dolor Garganta":True, "Irritacion de ojos":True, "Dolor Cabeza":True,"Dolor de cuerpo":True,"Flemas":True},
]



def consulta(bo, propiedad):
    if bo == 1:
        ans = True
    else:
        ans = False
    to_remove=[]
    for d in database:
        if d[propiedad] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

    if len(database) == 1:
        print("no chacho e imprimo: "+database[0]["nombre"])
        if(database[0]["nombre"]=="Gripe"):
            diagnostico="Alta probabilidad de un resfriado"
            tratamiento="Reposo, Hidratación, Vaporizaciones, tomar analgesicos si empieza a doler, Descongestivo Nasal"
            z=1
            print("Diagnostico: " + diagnostico)
            print("Recomendaciones: " + tratamiento)
        elif(database[0]["nombre"]=="Resfriado"):
            diagnostico="Alta probabilidad de Gripe"
            tratamiento="Antiviral, Antitusigenos y si no se trata puede causar Neumonia, encefalitis, meningitis"
            z=2
            print("Diagnostico: " + diagnostico)
            print("Recomendaciones: " + tratamiento)
        elif(database[0]["nombre"]=="Influenza"):
            diagnostico="Alta probabilidad de Influenza"
            tratamiento="Reposar, hidratarse, ir con el medico y tomar antiviral como  oseltamivir"
            z=3
            #print("Diagnostico: " + diagnostico)
            #print("Recomendaciones: " + tratamiento)
        elif(database[0]["nombre"]=="COVID"):
            diagnostico="Definitivamente COVID"
            tratamiento="Quedarse en casa, Reposar, hidratarse, ir con el medico y tomar antivirales como Paxlovid"
            z=4
            #print("Diagnostico: " + diagnostico)
            #print("Recomendaciones: " + tratamiento)
        else: 
            diagnostico="No pude dar un diagnostico con los datos proporcionados"
            tratamiento="Ir al doctor"
            z=5
            #print("Diagnostico: " + diagnostico)
            #print("Recomendaciones: " + tratamiento)
        window.destroy()
        window2 = Tk()
        window2.geometry("700x522")
        window2.configure(bg = "#FFFFFF")


        canvas = Canvas(
            window2,
            bg = "#FFFFFF",
            height = 522,
            width = 675,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            253.02667236328125,
            45.23809814453125,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )
       

        canvas.create_text(
            256.09368896484375,
            88.94271850585938,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )



        canvas.create_text(
            315.13323974609375,
            12.267974853515625,
            anchor="nw",
            text="Recordatorio:",
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )

        canvas.create_text(
            315.13323974609375,
            40.267974853515625,
            anchor="nw",
            text="Si no encuentra los sintomas compatibles \n con su situacion, consulte a su medico",
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )

        canvas.create_text(
            106.57794189453125,
            130.34707641601562,
            anchor="nw",
            text="Cuida tu salud",
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )

        canvas.create_text(
            97.376953125,
            44.471343994140625,
            anchor="nw",
            text="Haz ejercicio regularmente",
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )

        canvas.create_text(
            64.40679931640625,
            339.66917419433594,
            anchor="nw",
            text="Recomendaciones:",
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )
        canvas.create_text(
            64.40679931640625,
            390.66917419433594,
            anchor="nw",
            text=tratamiento,
            fill="#000000",
            font=("Inter SemiBold", 14 * -1)
        )



        canvas.create_text(
            44.47137451171875,
            164.85073852539062,
            anchor="nw",
            text="Diagnostico:",
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )
        canvas.create_text(
            44.47137451171875,
            200.85073852539062,
            anchor="nw",
            text=diagnostico,
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )

        canvas.create_text(
            36.80389404296875,
            13.034698486328125,
            anchor="nw",
            text="Informacion:",
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )

        canvas.create_text(
            107.34466552734375,
            88.17596435546875,
            anchor="nw",
            text="Cuida tu alimentacion",
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )

        
        canvas.create_rectangle(
            304.3987797498703,
            11.501227259635925,
            305.16552734375,
            161.78375244140625,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            21.46890914440155,
            164.0839604139328,
            622.5990600585938,
            164.8507080078125,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            24.53592574596405,
            79.74173629283905,
            305.16552734375,
            80.50848388671875,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            26.8361576795578,
            121.91284835338593,
            303.63201904296875,
            122.67959594726562,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            26.8361576795578,
            323.5674504041672,
            651.7354125976562,
            324.33421325683594,
            fill="#000000",
            outline="")
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_1 = canvas.create_image(
            58.6029052734375,
            54.97015380859375,
            image=image_image_1
        )

            




def submitForm():
    bo=Perdida_ol.get()
    i=consulta(bo, "Perdida olfato")
    bo=Escalo.get()
    i=consulta(bo, "Escalofrios")
    bo=DolorA.get()
    i=consulta(bo, "Dolor articulacion")
    bo=Dif_res.get()
    i=consulta(bo, "Dificultad para respirar")
    bo=tos.get()
    i=consulta(bo, "Tos")
    bo=fiebre.get()
    i=consulta(bo, "Fiebre")
    bo=Congestion_N.get()
    i=consulta(bo, "Congestion Nasal")
    bo=Moqueo.get()
    i=consulta(bo, "Secrecion")
    bo=DolorG.get()
    i=consulta(bo, "Dolor Garganta")
    bo=Irri_ojos.get()
    i=consulta(bo, "Irritacion de ojos")
    bo=DolorCa.get()
    i=consulta(bo, "Dolor Cabeza")
    bo=CuerpoCu.get()
    i=consulta(bo, "Dolor Cuerpo")
    bo=Flemas.get()
    i=consulta(bo, "Flemas")
    


submit=Button(window,text="Enviar",command=submitForm).place(x=560,y=437)


    

    




window.resizable(False, False)
window.mainloop()