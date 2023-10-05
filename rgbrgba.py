"RGB<->RGBA相互変換"
import sys
from PIL import Image

if __name__=='__main__':
    img=Image.open(sys.argv[1])
    print(img.mode)
    if(img.mode=="RGBA"):
        img2=img.convert("RGB")
        img2.save(sys.argv[1])
        print("->RGB")
    elif(img.mode=="RGB"):
        img2=img.copy()
        img2.putalpha(alpha=255)
        img2.save(sys.argv[1])
        print("->RGBA")
    else:
        print("Others")