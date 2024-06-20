#importing the modules
import random
from PIL import Image

while True:
    print('''1.roll the dice    2.To exit ''')
    ans = int(input(" what do you wannt do?"))
    if ans == 1:
        num = random.randrange(1,6)
           
        if num == 1 :
            img = Image.open(r"C:\Users\chand\OneDrive\Desktop\python projects\dice simulator\one.png")
            img.show()
               
        if num == 2 :
            img = Image.open(r"C:\Users\chand\OneDrive\Desktop\python projects\dice simulator\two.png")
            img.show()
    
        if num == 3 :
            img = Image.open(r"C:\Users\chand\OneDrive\Desktop\python projects\dice simulator\three.png")
            img.show()
    
        if num == 4 :
            img = Image.open(r"C:\Users\chand\OneDrive\Desktop\python projects\dice simulator\four.png")
            img.show()
    
        if num == 5 :
            img = Image.open(r"C:\Users\chand\OneDrive\Desktop\python projects\dice simulator\five.png")
            img.show()
    
        if num == 6 :
            img = Image.open(r"C:\Users\chand\OneDrive\Desktop\python projects\dice simulator\six.png")
            img.show()
    else :
        break
    

    
 

    

    
    

    
