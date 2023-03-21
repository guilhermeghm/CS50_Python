import sys
import os
from os import path
from PIL import Image, ImageOps

if (len(sys.argv) < 2):
    sys.exit("Too few command-line arguments")
elif (len(sys.argv) > 3):
    sys.exit("Too many command-line arguments")
elif not path.exists(sys.argv[1]):
    sys.exit("File does not exist")

elif (len(sys.argv) == 3):
    beforeImg = os.path.splitext(sys.argv[1])
    afterImg  = os.path.splitext(sys.argv[2])
 
    if beforeImg[1] != ".jpg" and beforeImg[1] != ".jpeg" and beforeImg[1] != ".png":
        print(sys.argv[1])
        sys.exit("Invalid output")
    elif beforeImg[1] != afterImg[1]:
        sys.exit("Input and output have different extensions")
    else:
        shirt     = Image.open("shirt.png")
        muppetImg = Image.open(sys.argv[1])
        muppetNew = ImageOps.fit(muppetImg, shirt.size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        muppetNew.paste(shirt, box=None, mask=shirt)
        muppetNew.save(sys.argv[2])
