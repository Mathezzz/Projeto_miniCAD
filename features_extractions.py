# -*- coding: utf-8 -*-
"""
Created on Mon May  1 08:30:15 2023

@author: ander
"""

import cv2
import numpy as np

def desenhar_linhas(img, pontos):
    ponto_anterior = pontos[0]
    for ponto in pontos[1:]:
        cv2.line(img, (ponto_anterior.ravel()), (ponto.ravel()), (255,255,255), 1)
        ponto_anterior = ponto
    return img

imagem = cv2.imread('F:/ander/Downloads/foguete_colorido.jpg')
dim = (int(imagem.shape[1]*0.12), int(imagem.shape[0]*0.12))
imagem = cv2.resize(imagem, dim)

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cantos = cv2.goodFeaturesToTrack(imagem_cinza, 30, 0.03, 10)
cantos = np.int0(cantos)
print(len(cantos))

for i, ponto in enumerate(cantos):
    x,y = ponto.ravel()
    print(f'X: {x}   Y: {y}')
    cv2.circle(imagem, (x,y), 3, 255, -1)
    cv2.putText(imagem, str(i), (x, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

imagem_desenhada = desenhar_linhas(imagem, cantos)

# cv2.imshow('Imagem com features',imagem)
# cv2.imshow('Imagem cinza', imagem_cinza)
# stack = np.hstack((cv2.cvtColor(imagem_cinza, cv2.COLOR_GRAY2BGR), imagem))
stack = np.hstack((cv2.cvtColor(imagem_cinza, cv2.COLOR_GRAY2BGR), imagem_desenhada))
cv2.imshow('Imagens', stack)
cv2.waitKey(0)
cv2.destroyAllWindows()