'''Nome: Luiz Henrique Lourenção - NUSP: 10284862
   SCC0251 - Processamento de Imagens
   Trabalho Final de Processamento de Imagens
   Título: Reconhecimento de Dígitos em Imagens
   Descrição: O projeto consiste em reconhecer os dígitos de uma imagem de placa de carro brasileira padrão e transformá-los em texto
'''

import numpy as np
import imageio as im
import cv2

#RECEBENDO A IMAGEM ORIGINAL

imgName = str(input())

img = cv2.imread(imgName + ".png")

cv2.imshow("Original", img)

'''transformando a imagem em preto e branco
            SEGMENTACAO'''

limiar = 255 * 30/100 #numero escolhido em cima de testes nas imagens

lower_white = np.array([0,0,0], dtype=np.uint8)
upper_white = np.array([limiar, limiar, limiar], dtype=np.uint8)

mask = cv2.inRange(img, lower_white, upper_white)

x, y = np.shape(mask)

imgfinal = mask

for i in range(x):
    for j in range(y):
        if(mask[i][j] == 255):
            imgfinal[i][j] = 0
        else:
            imgfinal[i][j] = 255

cv2.imshow("Segmentada", imgfinal)

#Encontrando a linha que tem o maior valor de soma (maior quantidade de pixels brancos)

maiorVertical = 0
maiorHorizontal = 0

for i in range(y):
    if(np.sum(imgfinal[:,i]) > maiorVertical):
        maiorVertical = np.sum(imgfinal[:,i])

#Se a linha tiver 15% ou mais dos valores sendo pretos, entao ela eh uma linha de digito 

for i in range(y):
    if(np.sum(imgfinal[:,i]) > maiorVertical * 85/100):
        imgfinal[:,i] = 127

for i in range(x):
    if(np.sum(imgfinal[i,:]) > maiorHorizontal):
        maiorHorizontal = np.sum(imgfinal[i,:])

#Se a coluna tiver 20% ou mais dos valores sendo pretos, entao ela eh uma coluna de digito

for i in range(x):
    if(np.sum(imgfinal[i,:]) > maiorHorizontal * 80/100):
        imgfinal[i,:] = 127

cv2.imshow("Separada", imgfinal)

cv2.waitKey(0)

'''Professor, estou com dificuldades para encontrar imagens com a mesma resolução.
Como pode ser observado no relatório parcial, a imagem que eu usei de exemplo e que tem
a menor resolução, teve um resultado melhor pelo menos na parte de pré-processamento, 
nos próximos dias vou tentar reduzir a resolução das outras e ver oque acontece.
Se você souber a solução e quiser me dar uma dica eu aceito hahaha.
Também terei que pesquisar sobre oque fazer depois de ter os digitos separados, tive que 
parar por aqui para fazer o relatório parcial e entregá-lo dentro do prazo.'''
