import cv2 
import os
import time
import uuid

IMAGES_PATH = '/Users/meghananekar/Desktop/RealTimeObjectDetection/Tensorflow/workspace/images/collectedImages'

labels = ['hello','thanks','yes','no','iloveyou']
number_imgs = 15

for label in labels:
    os.makedirs(os.path.join(IMAGES_PATH, label), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(20):
        ret, frame = cap.read()
        if not ret:
            print("Error: No frame captured")
            break
        imagename = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame) 
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()