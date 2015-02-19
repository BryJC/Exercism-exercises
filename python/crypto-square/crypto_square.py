from re import sub
from math import sqrt

def encode(text):
    
text = (sub('[^a-zA-Z0-9]','', text)).lower()
columns = int((sqrt(len(text))+1)//1)
myArray = [[0 for j in range(columns)] for i in range(columns)]

x = 0
for i in myArray:
    for j in i:
        if x >= len(text):
            break
        else:
            myArray[myArray.index(i)][i.index(j)] = text[x]
            x += 1
        
newArray = []
for i in range(0, len(myArray)):
    newArray.append([row[i] for row in myArray])
        
        
final = reduce(lambda x,y: x+[' ']+y, newArray)
return reduce(lambda x,y: x+y, final)        
    
    
    
    
