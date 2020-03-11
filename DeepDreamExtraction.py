"""
from PIL import Image
from math import floor
NormalAddress=input("Normal Image: ")
DeepDreamAddress = input("DeepDream: ")
ExtractedAddress = input("Extracted Address: ")
Normal = Image.open(NormalAddress)
NormalPix = Normal.load()
DeepDream = Image.open(DeepDreamAddress)
DeepDreamPix = DeepDream.load()

for x in range(Normal.size[0]):
    for y in range(Normal.size[1]):
        NormalPix[x,y] = (floor((DeepDreamPix[x,y][0]-NormalPix[x,y][0])/2+122.5),floor((DeepDreamPix[x,y][1]-NormalPix[x,y][1])/2+122.5),floor((DeepDreamPix[x,y][2]-NormalPix[x,y][2])/2+122.5))
Normal.save(ExtractedAddress)
"""
from PIL import Image
from math import floor
NormalAddress=input("Normal Image: ")
DeepDreamAddress = input("DeepDream: ")
ExtractedAddress = input("Extracted Address: ")
Normal = Image.open(NormalAddress)
NormalPix = Normal.load()
DeepDream = Image.open(DeepDreamAddress)
DeepDreamPix = DeepDream.load()

for x in range(DeepDream.size[0]):
    for y in range(DeepDream.size[1]):
        Tuple = [0.0000,0.0000,0.0000]
        for k in range(3):
            Tuple[k] = floor(-1*abs(DeepDreamPix[x,y][k]-NormalPix[x,y][k]))
            Tuple[k] = floor(-1*abs(100*(Tuple[k])**.2) + 255)
            if(Tuple[k]<0):
                Tuple[k] = 0
        NormalPix[x,y] = (Tuple[0],Tuple[1],Tuple[2])
Normal.save(ExtractedAddress)