import cv2
import matplotlib.pyplot as plt
import numpy as np

def draw(mydict):
    image = np.ones((400, 400, 3), dtype = np.uint8) #hay que calcular el tamaño
    image = 255* image #white image
    color = (0, 0, 0) #Black color in RGB
    thickness = -1
    for i,entry in enumerate(list(mydict.keys())):
        if (entry[0]>=0 and entry[1]>=0):
            end_point = (entry[0]+1, entry[1]+1)
            image = cv2.rectangle(image, entry, end_point, color, thickness)
    # Displaying the image 
    cv2.imshow('GameOfLife', image) 
    cv2.waitKey(500)
 
def count_neighbors_alive(key, mydict):
    alive = 0
    for k in [-1, 0, 1]:
            for q in [-1, 0, 1]:
                if k==0 and q==0:
                    continue
                else:
                    neighbor = (key[0] + k, key[1] + q)
                    if neighbor in mydict.keys():
                        alive = alive + 1
    return alive
 
def update(mydict):
    key_set = mydict.keys()
    new_dict = {}
    for key in key_set:
        #check neighbors 
        for k in [-1, 0, 1]:
            for q in [-1, 0, 1]:
                neighbor = (key[0] + k, key[1] + q)
                if neighbor not in key_set: #if alive, it will be checked at some point. It is dead
                    alive = count_neighbors_alive(neighbor, mydict)
                    if alive == 3:
                        new_dict[neighbor] = 1
        #the cell itself
        alive = count_neighbors_alive(key, mydict)
        if alive==2 or alive==3:
            new_dict[key] = 1
    return new_dict    
    
mydict =  {}
        
   
mydict = {(100,50): 1, (101,50): 1, (102,50): 1, (101,51): 1,
          (40,40):1, (41,40):1, (42,40):1, (42,41):1, (43,41):1, (43,42):1, (43,43):1,
          (46,43):1, (46,42):1, (46,41):1, (47,41):1, (47,40):1, (48,40):1, (49,40):1,
          (40,37):1, (41,37):1, (42,37):1, (42,36):1,(43,36):1,(43,35):1,(43,34):1,
          (46,34):1,(46,35):1, (46,36):1,(47,36):1,(47,37):1,(48,37):1,(49,37):1,
          
          (80,80):1,(81,80):1,(82,80):1,(86,80):1, (87,80):1, (88,80):1, (78,78):1,(78,77):1,(78,76):1,
           (78,72):1,(78,71):1 ,(78,70):1, (80,75):1, (81,75):1, (82,75):1, (83,76):1,(83,77):1,(83,78):1,
           (85,78):1,(85,77):1, (85,76):1, (86,75):1,(87,75):1,(88,75):1, (90,76):1,(90,77):1,(90,78):1,
           (90,72):1, (90,71):1, (90,70):1, (86,73):1, (87,73):1,(88,73):1, (82,73):1,(81,73):1, (80,73):1,
           (83,72):1,(83,71):1,(83,70):1,(85,72):1,(85,71):1,(85,70):1, (86,68):1,(87,68):1,(88,68):1,
           (82,68):1, (81,68):1, (80,68):1,
           (5,5):1, (6,6):1, (7,6):1, (7,5):1, (7,4):1}

draw(mydict)
while True:
    mydict = update(mydict)
    draw(mydict)
    if (len(mydict.keys())==0):
        cv2.destroyAllWindows()
        break
    

