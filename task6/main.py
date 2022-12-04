import cv2, sys, threading
from tkinter import *
from pynput.keyboard import Key, Listener
from PIL import Image, ImageTk

from mqtt import MqttPoster
from find_clicks import ClickAndSetPoint


win= Tk()
win.geometry("700x700")
img_label =Label(win)
img_label.grid(row=0, column=0)
img_label.place(x=160, y=60)


exit_button = Button(win, text="Exit", command=win.destroy).pack()


video_src = ''
if len(sys.argv) > 1:
    video_src = sys.argv[1]


delete_points_key = 'c'
mqtt = MqttPoster()
draw_points = ClickAndSetPoint()



if video_src:
    source = cv2.VideoCapture(video_src)

else:
    source = cv2.VideoCapture(0)

# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_points.mouse_callback)


img_label.bind('<Button-1>', draw_points.tk_mouse_callback)
win.bind('<Key>', draw_points.tk_on_delete_key_press)


def for_opencv_thread():
    while 1:
        ret, img = source.read()
        draw_points.draw_all_points(img)
 

        mqtt.send(draw_points.get_points())


        cv2image= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image = img)
        
        # img_label.image = imgtk
        img_label.pack()
        img_label.configure(image=imgtk)
        


opencv_thr = threading.Thread(target=for_opencv_thread)
opencv_thr.start()

win.mainloop()
