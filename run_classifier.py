import cv2
import sys

def get_classifier(im=None, cascade=None):
    if im == None and cascade == None:
            #get arguments from command line
            im = cv2.imread(sys.argv[1]) #save image file as opencv image
            cascade = cv2.CascadeClassifier(sys.argv[2]) #create a CascadeClassifier object from classifier
    return im, cascade

def dectectObject(im, cascade, scale ):
    return cascade.detectMultiScale(image=im,scaleFactor=scale)
def drawRect(im, rect, color):
    i=1
    for obj in rect:
        img=im.copy() #create a copy of original image
        cv2.rectangle(img, tuple(obj[:2]),tuple(obj[2:]), color) #draw rectangle from the list of classified rectangles

        cv2.imwrite("result_%d.jpg"%i , img) #save drawn image
        i+=1

if __name__ == '__main__':

    im, cascade = get_classifier()
    rect = dectectObject(im, cascade, scale=2)
    drawRect(im, rect, color=(0,255,0))
