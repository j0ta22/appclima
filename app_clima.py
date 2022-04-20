import imp
from statistics import mode
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import ttk
from xml.dom import minicompat
import requests
from PIL import Image
import PIL.ImageTk


class ClimaApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.inicializar_gui()
        self.API_OPEN_WEATHER_MAP = 'd090c09158bf73066f4cbdc6228b46ae'
        self.URL_OPEN_WEATHER_MAP = 'https://api.openweathermap.org/data/2.5/weather'
    

    def inicializar_gui(self):
        self.title('App clima')
        self.iconbitmap("sol.ico")
        canvas = tk.Canvas(self, height=400, width=400)
        canvas.pack()

        cielo = PIL.Image.open(r"C:/Users/Casa/Desktop/Python/proyectos/appclima/a.jpg")
        cielo = PIL.ImageTk.PhotoImage(cielo)
        lbl_cielo = tk.Label(self, image=cielo)
        lbl_cielo.Image = cielo
        lbl_cielo.place(relx=0, rely=0, relheight=1, relwidth=1)

        frame_comp = tk.Frame(self, bg='#0B4C76', bd=5)
        frame_comp.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')
        #frame_comp.wm_attributes('-transparentcolor', '#add123')

        self.txt_ciudad = tk.Entry(frame_comp, font=('Times', 14))
        self.txt_ciudad.place(relx=0, rely=0, relheight=1, relwidth=0.65)

        boton_buscar = tk.Button(frame_comp, text='Buscar', bg='#2D3142', fg='white', font=('Times', 12))
        boton_buscar['command'] = self.buscar
        boton_buscar.place(relx=0.65, rely=0, relheight=1, relwidth=0.3)

        frame_result = tk.Frame(self, bg='#0B4C76', bd=5)
        frame_result.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor='n')

        self.lbl_resultados = tk.Label(frame_result, font=('Times', 14))
        self.lbl_resultados.place(relx=0, rely=0, relheight=1, relwidth=1)



    def buscar(self):
        ciudad = self.txt_ciudad.get().strip()

        if len(ciudad) == 0:
            messagebox.showwarning('mensaje', "debe completar el campo 'ciudad'")
            return

        parametros = {'APPID' : self.API_OPEN_WEATHER_MAP, 'q' : ciudad, 'units' : 'metric', 'lang' : 'es'}
        respuesta = requests.get(self.URL_OPEN_WEATHER_MAP, parametros)

        estado_clima = respuesta.json()

        self.lbl_resultados['text'] = self.formatear_resultado(estado_clima)

    def formatear_resultado(self, estado_clima):
        try:
            nombre = estado_clima['name']
            pais = estado_clima['sys']['country']
            descripcion = estado_clima['weather'][0]['description']
            temperatura = estado_clima['main']['temp']
            minima = estado_clima['main']['temp_min']
            maxima = estado_clima['main']['temp_max']
            viento = estado_clima['wind']['speed']

            return f'Ciudad: {nombre}, {pais}\nCondiciones: {descripcion}\nTemperatura: {temperatura}°C\nMin: {minima}°C\nMax: {maxima}°C\nViento : {viento}M/S'
        except:
            return 'Se ha producido un error'





def main():
    app = ClimaApp()
    app.mainloop()

if __name__ == '__main__':
    main()
