import os
import sys
import time
from PIL import Image

def main(repertoire, taille):
    liste = os.listdir(repertoire)
    taille = int(taille)
    
    for image in liste:
        t1 = time.time()

        fichier = Image.open(repertoire + image)
        largeur, hauteur = fichier.size
        if (largeur > hauteur) :
            ratio = largeur / hauteur
            hauteur = int(taille / ratio)
            largeur = taille
            resize = (largeur, hauteur)

        else :
            ratio = hauteur / largeur
            largeur = int(taille / ratio)
            hauteur = taille
            resize = (hauteur, largeur)

        fichier = fichier.resize(resize)
        fichier.save(repertoire + image)

        #On écris les images
        print("Traitement de l'image : " + image)
        print("Taille Originale de l'image : " + str(largeur) + " x " + str(hauteur))
        print("Taille de l'image : " + str(largeur) + " x " + str(hauteur))     
        print('Temps de Traitement : %d ms'%((time.time()-t1)*1000))


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('USAGE: {} Repertoire Largeur'.format(sys.argv[0]))
    else:
        main(sys.argv[1], sys.argv[2])
