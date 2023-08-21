import cv2
import numpy as np
import os
import glob
from matplotlib import pyplot as plt

def showSingleImage(img, title, size):
    fig, axis = plt.subplots(figsize = size)

    axis.imshow(img, 'gray')
    axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
    plt.show()

def showMultipleImages(imgsArray, titlesArray, size, x, y):
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1 and y == 1):
        showSingleImage(imgsArray, titlesArray)
    elif(x == 1):
        fig, axis = plt.subplots(y, figsize=(size[0], size[1] * y))  # Increase height
        yId = 0
        for img in imgsArray:
            axis[yId].imshow(img, 'gray')
            axis[yId].set_anchor('NW')
            axis[yId].set_title(titlesArray[yId], fontdict={'fontsize': 18, 'fontweight': 'medium'}, pad=10)

            yId += 1
    elif(y == 1):
        fig, axis = plt.subplots(1, x, figsize=(size[0] * x, size[1]))  # Increase width
        fig.suptitle(titlesArray)
        xId = 0
        for img in imgsArray:
            axis[xId].imshow(img, 'gray')
            axis[xId].set_anchor('NW')
            axis[xId].set_title(titlesArray[xId], fontdict={'fontsize': 18, 'fontweight': 'medium'}, pad=10)

            xId += 1
    else:
        fig, axis = plt.subplots(y, x, figsize=size)  # Keep the specified size
        xId, yId, titleId = 0, 0, 0
        for img in imgsArray:
            axis[yId, xId].set_title(titlesArray[titleId], fontdict={'fontsize': 18, 'fontweight': 'medium'}, pad=10)
            axis[yId, xId].set_anchor('NW')
            axis[yId, xId].imshow(img, 'gray')
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def carregaVetorImagens(listaDeImagensDaPasta):
    imagens = len(listaDeImagensDaPasta)
    listaImagensCarregadas = []
    for imgPath in listaDeImagensDaPasta:
        img = cv2.imread(imgPath)  # Carrega a imagem usando o caminho
        listaImagensCarregadas.append(img)
        print("teste" + str(imgPath))
    return listaImagensCarregadas

def carregaVetorImagensCinza(listaDeImagensDaPasta):
    imagens = len(listaDeImagensDaPasta)
    listaImagensCarregadas = []
    for imgPath in listaDeImagensDaPasta:
        #print("Carregando as imagens em tom de cinza")
        img = cv2.imread(imgPath, 0)  # Carrega a imagem usando o caminho
        listaImagensCarregadas.append(img)
        print(str(imgPath))
    return listaImagensCarregadas


def aplicaThreshold(listaDeImagens):
    listaImagensLimiarizadas = []
    for imgPath in listaDeImagens:
        ret, thresh_img = cv2.threshold(imgPath, 180, 255, cv2.THRESH_BINARY)
        #print("Aplicando Threshold")
        listaImagensLimiarizadas.append(thresh_img)
    return listaImagensLimiarizadas

def identificaEstrelas(thresh_images):
    star_images = []

    for thresh_img in thresh_images:
        # Find contours in the thresholded image
        contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Create a copy of the original image to draw the detected stars
        star_img = thresh_img.copy()

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 50:  # Minimum area to consider as a potential star
                # Calculate the circularity of the contour
                perimeter = cv2.arcLength(contour, True)
                circularity = (4 * np.pi * area) / (perimeter * perimeter)

                if circularity > 0.5:  # Adjust this threshold as needed
                    cv2.drawContours(star_img, [contour], -1, (0, 255, 0), -1)  # Draw a green filled contour

        star_images.append(star_img)

    return star_images


def getImagensDaPasta():
    folder = 'imgs/*'
    listaDeImagensDaPasta = glob.glob(folder)
    print("Quantidade de imagens = " + str(len(listaDeImagensDaPasta)))

    #Criando as variaveis para as imagens usando a lista do glob
    andromeda = listaDeImagensDaPasta[0]
    aquila = listaDeImagensDaPasta[1]
    auriga = listaDeImagensDaPasta[2]
    canisMajor = listaDeImagensDaPasta[3]
    capricornus = listaDeImagensDaPasta[4]
    cetus = listaDeImagensDaPasta[5]
    columba = listaDeImagensDaPasta[6]
    gemini = listaDeImagensDaPasta[7]
    grus = listaDeImagensDaPasta[8]
    leo = listaDeImagensDaPasta[9]
    orion = listaDeImagensDaPasta[10]
    pavo = listaDeImagensDaPasta[11]
    pegasus = listaDeImagensDaPasta[12]
    phoenix = listaDeImagensDaPasta[13]
    pisces = listaDeImagensDaPasta[14]
    piscisAustrinus = listaDeImagensDaPasta[15]
    puppis = listaDeImagensDaPasta[16]
    ursaMajor = listaDeImagensDaPasta[17]
    ursaMinor = listaDeImagensDaPasta[18]
    vela = listaDeImagensDaPasta[19]

    imagensASeremCarregadas = [andromeda, aquila, auriga, canisMajor, capricornus, cetus, columba, gemini,
                            grus, leo, orion, pavo, pegasus, phoenix, pisces, piscisAustrinus, puppis,
                            ursaMajor, ursaMinor, vela]

    return imagensASeremCarregadas


def main():
    imagensASeremCarregadas = getImagensDaPasta()

    vetorDeImagens = carregaVetorImagensCinza(imagensASeremCarregadas)
    vetorDeImagens = aplicaThreshold(vetorDeImagens)
    vetorDeImagensIdentificadas = identificaEstrelas(vetorDeImagens)
    vetorDeTitulos = ["andromeda", "aquila", "auriga", "canisMajor", "capricornus", "cetus", "columba", "gemini", "grus", "leo", "orion", "pavo", "pegasus", "phoenix", "pisces", "piscisAustrinus", "puppis", "ursaMajor", "ursaMinor", "vela"]

    showMultipleImages(vetorDeImagensIdentificadas, vetorDeTitulos, (20,16), 5, 4)

if __name__ == "__main__":
    main()
