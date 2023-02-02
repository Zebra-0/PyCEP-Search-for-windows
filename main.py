# codigo criado com intencao de evoluir nos estudos de python, com gui e consumo de api.
# criado por Gabriel Hernandes
# linkedin: https://br.linkedin.com/in/gabriel-hernandes-4a3b8b248?trk=people-guest_people_search-card
# github: https://github.com/Gabriel-Hernandess/PyCEP-Search

import requests
from tkinter import *
from tkmacosx import Button
from PIL import ImageTk,Image
import json
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkintermapview import TkinterMapView

# funcao para puxar e exibir dados
def search():
    try:
        cep_client = cep.get()

        # verifica se a pessoa digitou com '-', se sim, ira remover e deixar apenas os digitos
        if len(cep_client)==9:
            cep_client.replace('-', '')

        # puxar dados
        r = requests.get(f"https://viacep.com.br/ws/{cep_client}/json/")
        r = r.json()

        # transformar em dados
        end = r.get("logradouro")
        cep_end = r.get("cep")
        bairro = r.get("bairro")
        cidade = r.get("localidade")
        estado = r.get("uf")
        ddd = r.get("ddd")

        # exibir
        Label(program, text=end).place(x=300, y=220)
        Label(program, text=bairro).place(x=550, y=220)
        Label(program, text=cidade).place(x=300, y=260)
        Label(program, text=estado).place(x=400, y=260)

        # definir endereco para ir ao map_widget.set_address
        local = bairro+', '+cidade+", brasil"

        # exibir mapa
        map_widget = TkinterMapView(program, width=800, height=450, corner_radius=5, bd=6)
        map_widget.set_address(local, marker=True)
        map_widget.set_zoom(22)
        map_widget.place(x=150, y=300)

    except:
        messagebox.showinfo("CEP INVALIDO", "Tente novamente!")

# iniciar programa
program=Tk()

# config da janela
program.title("CEP Search")
program.geometry("1080x800")
program.minsize(1080, 800) 
program.maxsize(1080, 800)

# definindo fundo do programa
bg_img = Image.open("/Users/gabrielhernandes/Documents/Busca CPF - Python/test.jpg")
resized = bg_img.resize((1080, 800), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized)
Background = Label(program, image=img).place(x=0, y=0)

# textos
texto1 = Label(program, text="PyCEP Search", font="Arial 35",justify=CENTER, bg="white", fg="black", height=2, anchor=S).pack()
texto2 = Label(program, text="Digite o cep no campo abaixo:", bg="grey", anchor=S).place(x=300, y=125)

# entrar com cep e defini-lo na variavel para puxar dados na api
cep = Entry(program, bg="white", fg="black")
cep.place(x=300, y=150, width=220)

# botao para chamar a funcao e puxar dados
srch = Image.open("search.png")
resize = srch.resize((10, 10), Image.ANTIALIAS)
btn = ImageTk.PhotoImage(resize)
pesquisar = Button(program, text="Pesquisar", image=btn, compound=LEFT, activebackground="grey", bd=5, highlightbackground = "black", highlightthickness = 3, bg="white", command=search).place(x=600, y=142)

program.mainloop()
