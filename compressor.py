from PIL import Image
import os

#Ruta en windows
imageFolder = "C:\\imagenes\\"

#Ruta en linux
#imageFolder = "/home/user/imagenes"

if __name__ == "__main__":
    for filename in os.listdir(imageFolder):
        name, extension = os.path.splitext(imageFolder + filename)
        
        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(imageFolder + filename)
            picture.save(imageFolder + "compressed_"+filename, optimize=True, quality=60)