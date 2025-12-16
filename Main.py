from ultralytics import YOLO
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "best.pt")
cap=cv2.VideoCapture(0)

i=0
last_plot=None

while True:
    r,f=cap.read()
    if not r: break

    if i%5==0:
        rs=m(f,stream=False,conf=0.25)[0]
        last_plot=rs.plot()
        shown=last_plot
    else:
        shown=last_plot if last_plot is not None else f

    cv2.imshow("d",shown)
    i+=1
    if cv2.waitKey(1)==27: break

cap.release()
cv2.destroyAllWindows()

