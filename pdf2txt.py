import fitz

with fitz.open('your-file.pdf') as pdf:
    text = ''

    for pag in pdf:
        text += f'{pagina.getText()}\n'

print(text)
