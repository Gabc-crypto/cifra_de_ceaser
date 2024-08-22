from tkinter import Label, Button, Entry, Tk

def ceasar(data: str, key: int, mode: int):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    # Este 'c' significa character = carácter
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == 1 else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data

def codificado(texto_entry, chave_entry, resultado_label):
    texto = texto_entry.get()
    chave = int(chave_entry.get())
    texto_codificado = ceasar(texto, chave, 1)
    resultado_label.config(text = f'Texto codificado: {texto_codificado}')

def descodificado(texto_entry, chave_entry, resultado_label):
    texto = texto_entry.get()
    chave = int(chave_entry.get())
    texto_descodificado = ceasar(texto, chave, 0)
    resultado_label.config(text = f'Texto descodificado: {texto_descodificado}')

def main():
    root = Tk()
    root.title("Cifra de Ceasar")
    root.config(padx=50, pady=50)

    texto_label = Label(root, text = 'Digite um texto: ')
    texto_label.grid(row=0, column=0)

    texto_entry = Entry(root)
    texto_entry.grid(row=0, column=1)

    chave_label = Label(root, text = 'Digite a chave: ')
    chave_label.grid(row=1, column=0)

    chave_entry = Entry(root)
    chave_entry.grid(row=1, column=1)

    codificar_button = Button(root, text = 'Codificar', command=lambda: codificado(texto_entry, chave_entry, resultado_label))
    codificar_button. grid(row=2, column=0)

    descodificar_button = Button(root, text = 'Descodificar', command=lambda: descodificado(texto_entry, chave_entry, resultado_label))
    descodificar_button.grid(row=2, column=1)

    resultado_label = Label(root, text = 'Resultado: ')
    resultado_label.grid(row=3, column=0, columnspan=2)

    root.mainloop()

main()