import datetime
import time
import pytesseract
from PIL import ImageGrab

# Defina o intervalo de coleta em segundos (por exemplo, 60 segundos para coletar a cada minuto)
# Set the collection interval in seconds (e.g. 60 seconds for collection every minute)
intervalo_coleta = 10

# Defina as coordenadas (x, y) e as dimensões (largura, altura) da região a ser capturada
# Define the coordinates (x, y) and dimensions (width, height) of the region to be captured
x = 438  # Substitua pelo valor correto # Change with the correct value
y = 629  # Substitua pelo valor correto # Chage with the correct value
largura = 200  # Substitua pelo valor correto  | replace with the width value [RANGE]
altura = 50  # Substitua pelo valor correto | replace with the height value [RANGE]

while True:
    # Obtenha a data e hora atual
    # Get current date and time
    data_hora_atual = datetime.datetime.now()

    # Capture a região especificada da tela como uma imagem
    # Capture the specific region of the screen as an image
    imagem = ImageGrab.grab(bbox=(x, y, x + largura, y + altura))

    # Use OCR para extrair o texto da imagem
    # Use OCR to extract text from image
    texto_extraido = pytesseract.image_to_string(imagem)

    # Extraia apenas os numeros encontrados no texto
    # Extract only the numbers found in the text
    numeros = ''.join(filter(str.isdigit, texto_extraido))

    if numeros:
        # Se numeros foram encontrados, imprima-os
        # If numbers were found, print them
        print(f"Numeros coletados: {numeros}")
        print(f"Data e hora da coleta: {data_hora_atual}")

        # Salve os numeros em um arquivo de texto
        # Save the numbers to a text file
        with open("coleta.txt", "a") as arquivo_texto:
            arquivo_texto.write(f"Numeros coletados: {numeros}\nData e hora da coleta: {data_hora_atual}\n")
    else:
        # Caso contrario, indique que nenhum numero foi encontrado
        # Else, No number was found
        print("Nenhum numero encontrado na região da tela.")

    # Aguarde o intervalo definido antes da próxima coleta
    # w8 the break to next collect
    time.sleep(intervalo_coleta)