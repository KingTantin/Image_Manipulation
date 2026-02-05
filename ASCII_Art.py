from PIL import Image
import cv2
from PIL import Image as im 

def ASCII(file, resolution: int) -> str:

    #Resolution
    with Image.open(file) as image:
        x, y = image.size
    #New Resolution
    g = x/y
    dividend_x = x/resolution              
    dividend_y = dividend_x*g       #leads to the picture beeing more oriented to original ratio
    #Reduces Size of Image
    img = cv2.imread(file)
    res = cv2.resize(img, dsize=(int(x/dividend_x), int(y/dividend_y)), interpolation=cv2.INTER_CUBIC)
    res_imag = im.fromarray(res) 
    imag_bw = res_imag.convert("L") #makes picture black and white
    imag = imag_bw.convert('RGB')   
    #ASCII Dict: 0 = Dunkel, 10 = Hell
    ASCII_Dict = {0: '  ', 1: '..', 2: ';;', 3:'**', 4: '++', 5: 'ii', 6: 'aa', 7: 'gg', 8: '%%', 9: '$$', 10: '##'} 
    ASCII_ART = ''
    #Pixel Loops + ASCII print
    for y_loop in range(int(y/dividend_y)-1):
        for x_loop in range(int(x/dividend_x)-1):
            pixelRGB = imag.getpixel((x_loop, y_loop))
            brightness = int(sum(pixelRGB)**(1/3))
            
            ASCII_ART += ASCII_Dict[brightness]        

        ASCII_ART += '\n'                              
    return ASCII_ART        

file = r'C:\Users\Username\Downloads\Filename'        #add your path here
art = ASCII(file, 50)    
print(art)
