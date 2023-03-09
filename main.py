# Import required Image library
from PIL import Image, ImageDraw, ImageFont
import PySimpleGUI as sg


filiais = {
    "Santos": "Av. Marginal Direita da Via Anchieta, 1135 -- Alemoa - Santos-SP, 11095-902",
    "Rio Claro": "Av. Pres. Kennedy, 900 - Jd. Quitandinha -- Rio Claro-SP, 13501-500",
    "Paulinia": "Rua Bortolo J. Ferro, 655 - Boa Esperança -- Paulínia-SP, 13148-050",
    "Guarulhos": "Rod. Hélio Schmidt, S/N - Aeroporto Internacional -- de São Paulo Ed. TECA - Sala 5.01, 07190-100",
    "Pinda": "Av. Buriti, 100 - Feital -- Pindamonhangaba-SP, 12441-270",
    "Campinas": "",
}

def gerar(nome, cargo, ramal, mail, filial):
    # Create an Image Object from an Image
    im = Image.open('base.png')
    draw = ImageDraw.Draw(im)

    # ------------------------ Nome ---------------------------------

    font = ImageFont.truetype('tahomabd.ttf', 32)
    draw.textsize(nome, font)
    # calculate the x,y coordinates of the text
    xy = (328, 50)
    draw.text(xy, nome, font=font, fill='#002857')

    # ----------------------- Setor ---------------------------------
    font = ImageFont.truetype('tahomabd.ttf', 24)
    draw.textsize(cargo, font)
    # calculate the x,y coordinates of the text
    xy = (328, 92)
    draw.text(xy, cargo, font=font, fill='#ffaa36')

    # ---------------------- Celular --------------------------------
    font = ImageFont.truetype('tahoma.ttf', 14)
    draw.textsize(ramal, font)
    # calculate the x,y coordinates of the text
    xy = (352, 141)
    draw.text(xy, ramal, font=font, fill='#000000')

    # ----------------------- Email ---------------------------------
    text = f"{mail}@grupogelog.com.br"
    font = ImageFont.truetype('tahoma.ttf', 14)
    draw.textsize(text, font)
    # calculate the x,y coordinates of the text
    xy = (352, 170)
    draw.text(xy, text, font=font, fill='#000000')

    # ---------------------- Endereco -------------------------------
    endereco = filiais[filial].split(" -- ", 1)
    font = ImageFont.truetype('tahoma.ttf', 14)
    # -------- Linha 1 -> Endereço ---------------
    draw.textsize(endereco[0], font)
    # calculate the x,y coordinates of the text
    xy = (352, 200)
    draw.text(xy, endereco[0], font=font, fill='#000000')
    # -------- Linha 2 -> Endereço ---------------
    draw.textsize(endereco[1], font)
    # calculate the x,y coordinates of the text
    xy = (352, 214)
    draw.text(xy, endereco[1], font=font, fill='#000000')


    im.show()
    im.save(f'X:\Assinaturas\{nome}.png')


dropdown = []
for item in filiais.keys():
    dropdown.append(item) 

layout = [
    [sg.Text("Nome de Exibição: "), sg.Input(key="nome", change_submits=True)],
    [sg.Text("Email: "), sg.Input(key="email"), sg.Text("@grupogelog.com.br")],
    [sg.Text("Cargo: "), sg.Input(key="cargo")],
    [sg.Text("Telefone:"), sg.Input(key="telefone")],
    [sg.Text("Filial:"), sg.DropDown(values=dropdown, key="filial")],
    [sg.Button('Gerar'), sg.Button('Exit')]
]

window = sg.Window("Assinatura", layout)

while True:  # Event Loop
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Gerar':
        gerar(values["nome"], values["cargo"], values["telefone"], values["email"], values["filial"])
        window["nome"].update(value="")
        window["cargo"].update(value="")
        window["email"].update(value="")

    if event == "nome":
        # Atualiza o campo de "E-Mail" com o primeiro e último nome
        aux = values["nome"].split(" ")
        if len(aux) == 1:
            aux = values["nome"]
        else:
            aux = aux[0] + aux[len(aux) - 1]

        window["email"].update(value=aux.lower())

window.close()


