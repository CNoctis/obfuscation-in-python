import os
#El presente programa tiene como finalidad "Oscurecer"/Dificultar es decir obfuscation el contenido de un txt


# Usar el directorio donde se encuentre el texto a modificar
path_folder = r"C:\Users\Cristian\Documents\Python"
os.chdir(path_folder)

# Función offuscar hace el texto más dificil de entender/leer, recibe un archivo .txt
def obfuscation(text):
    text = text.decode("UTF-8")
    texencryp = ""
    terms = [ \
        {'letters': "abcdefghijk", 'obfuscar': "¾«%¬ð"}
        , {'letters': "mnñopqrstuvwxyz", 'obfuscar': "œå"}
        , {'letters': "12345", 'obfuscar': "«ý"}
        , {'letters': "67890", 'obfuscar': "»ŒÐû"}
        , {'letters': "áéíóúü", 'obfuscar': "®ª—º"}]

    for letra in text:
        texencryp += letra
        for term in terms:
            if letra.lower() in term['letters']:
                texencryp += term['obfuscar']
    return texencryp


# Función desoffuscar recibe un texto previamente offuscado(oscurecido/dificultado) por la función offuscar y limpia el texto haciendo 100% legible su contenido.
def deobfuscation(text):
    term = "¾«%¬ðœå«ý»ŒÐû®ª—º"
    limpio = ''.join(letter.replace('\r','') for letter in text.decode("UTF-8") if letter not in term )
    return limpio



def main():
    # Crea un archivo txt offuscado
    with open('texto.txt', 'rb') as archivo:
        with open("texto_obfuscation.txt", "w", encoding='utf-8') as file:
            file_obfuscation= obfuscation(archivo.read())
            file.write(file_obfuscation)

    # Crea un archivo txt desoffucasdo
    with open("texto_obfuscation.txt", "rb") as f:
        with open("texto_deobfuscation.txt", "w", encoding='utf-8') as txt:
            file_deobfuscation = deobfuscation(f.read())
            txt.write(file_deobfuscation)


if __name__ == '__main__':
    main()
