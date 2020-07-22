from tkinter import Tk, Canvas, Frame, BOTH
import Classes.Scenes.startScene as Scene
import settings as sett

currentScene = Scene.StartScene()

class Drawer:
    def drawLoop(self):
        global canvas
        global currentScene

        currentScene.draw(canvas)

        canvas.after(200, self.drawLoop)


root = Tk()
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
canvas = Canvas(root, width=2000, height=2000, highlightthickness=0)
canvas.configure(background='black')

# Draw Corners
canvas.create_line(0, 0, 1, 0, fill="white")
canvas.create_line(0, sett.screenHeight-1, 1, sett.screenHeight-1, fill="white")
canvas.create_line(sett.screenWidth-1, 0, sett.screenWidth, 0, fill="white")
canvas.create_line(sett.screenWidth-1, sett.screenHeight-1, sett.screenWidth, sett.screenHeight-1, fill="white")

canvas.pack()

drawer = Drawer()
drawer.drawLoop()

root.mainloop()


# import time
# import threading
# k = "k"

# def thread_function():
#     global k
#     while(k != "kkkkkkk"):
#         k = k + "k"
#         time.sleep(2)
    
    
# t = threading.Thread(target=thread_function)
# t.start()

# while(k != "kkkkkkk"):
#         print(k)
#         time.sleep(1)


