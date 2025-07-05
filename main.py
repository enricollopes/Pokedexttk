from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk 
import re
from dados import *

co0 = "#444466"  # preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def trocar_pokemon(nome):
    pokemon = pokemons[nome]
    
    frame_pokemon.configure(bg=pokemon['cor'])

    pok_nome['text'] = nome
    pok_nome['bg'] = pokemon['cor']
    
    pok_id['text'] = pokemon['numero']
    pok_id['bg'] = pokemon['cor']
    
    pok_tipo['text'] = pokemon['tipo']
    pok_tipo['bg'] = pokemon['cor']

    nova_imagem = Image.open(pokemon['imagem']).resize((238, 238))
    nova_imagem = ImageTk.PhotoImage(nova_imagem)
    pok_imagem.configure(image=nova_imagem, bg=pokemon['cor'])
    pok_imagem.image = nova_imagem  

    hp = pokemon['status']['HP']
    ataque = pokemon['status']['Ataque']
    defesa = pokemon['status']['Defesa']
    velocidade = pokemon['status']['Velocidade']
    total = hp + ataque + defesa + velocidade

    pok_hp['text'] = f'HP: {hp}'
    pok_ataque['text'] = f'Ataque: {ataque}'
    pok_defesa['text'] = f'Defesa: {defesa}'
    pok_velocidade['text'] = f'Velocidade: {velocidade}'
    pok_total['text'] = f'Total: {total}'

    pok_hab1['text'] = pokemon['habilidades'][0]
    pok_hab2['text'] = pokemon['habilidades'][1]


pok_nome = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pok_nome.place(x=12, y=15)

pok_tipo = Label(frame_pokemon, text='Elétrico', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=50)

pok_id = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_id.place(x=12, y=75)

imagem_pokemon = Image.open('images/pikachu.png')
imagem_pokemon = imagem_pokemon.resize((238, 238))
imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

pok_imagem = Label(frame_pokemon, image=imagem_pokemon, relief='flat', bg=co1, fg=co0)
pok_imagem.place(x=70, y=50)

pok_tipo.lift()

# STATUS

pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

pok_hp = Label(janela, text='HP: 300', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=350)

pok_ataque = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_ataque.place(x=15, y=375)

pok_defesa = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_defesa.place(x=15, y=400)

pok_velocidade = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_velocidade.place(x=15, y=425)


def extrair_numero(label):
    return int(re.findall(r'\d+', label.cget("text"))[0])

hp = extrair_numero(pok_hp)
ataque = extrair_numero(pok_ataque)
defesa = extrair_numero(pok_defesa)
velocidade = extrair_numero(pok_velocidade)

total = hp + ataque + defesa + velocidade       

pok_total = Label(janela, text=f'Total: {total}', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=450)

# HABILIDADES

pok_habilidades = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_habilidades.place(x=200, y=310)

pok_hab1 = Label(janela, text='Choque de Trovão', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hab1.place(x=200, y=350)

pok_hab2 = Label(janela, text='Cabeçada', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hab2.place(x=200, y=375)


# BOTÕES
imagem_pokemon_1 = Image.open('images/cabeca-pikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

b_pok_1= Button(janela,command=lambda:trocar_pokemon('Pikachu'), image=imagem_pokemon_1, text='Pikachu',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=10)

imagem_pokemon_2 = Image.open('images/cabeca-gyarados.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

b_pok_2= Button(janela,command=lambda:trocar_pokemon('Gyarados'), image=imagem_pokemon_2, text='Gyarados',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_2.place(x=375, y=70)

imagem_pokemon_3 = Image.open('images/cabeca-gengar.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

b_pok_3= Button(janela,command=lambda:trocar_pokemon('Gengar'), image=imagem_pokemon_3, text='Gengar',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_3.place(x=375, y=130)

imagem_pokemon_4 = Image.open('images/cabeca-dragonite.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

b_pok_4= Button(janela,command=lambda:trocar_pokemon('Dragonite'), image=imagem_pokemon_4, text='Dragonite',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_4.place(x=375, y=190)

imagem_pokemon_5 = Image.open('images/cabeca-charmander.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

b_pok_5= Button(janela,command=lambda:trocar_pokemon('Charmander'), image=imagem_pokemon_5, text='Charmander',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_5.place(x=375, y=250)

imagem_pokemon_6 = Image.open('images/cabeca-bulbasaur.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

b_pok_6= Button(janela,command=lambda:trocar_pokemon('Bulbasaur'), image=imagem_pokemon_6, text='Bulbasaur',width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_6.place(x=375, y=310)

trocar_pokemon('Pikachu')

janela.mainloop()

