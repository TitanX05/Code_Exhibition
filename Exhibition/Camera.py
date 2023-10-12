import numpy as np
import pandas as panda
import cv2 

def cv():
    vid = cv2.VideoCapture(0) 
  
    while(True): 
        ret, frame = vid.read() 

        cv2.imshow('Web cam', frame) 

        if cv2.waitKey(1) == 32:
            break

    vid.release()
    cv2.destroyAllWindows()