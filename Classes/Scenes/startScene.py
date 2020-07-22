from random import randint
import settings as sett
import time

intro = True
mainLoop = False

class StartScene:
    player1_text = ""
    player2_text = ""
    player3_text = ""
    player4_text = ""    
    preTime = 0
    def draw(self, canvas):
        
        if intro:
            print("intro running")
            # Initialize text
            if self.player1_text == "":
                self.player1_text = canvas.create_text(sett.screenWidth/2-sett.playerIntroTextOffset, sett.screenHeight-sett.playerIntroTextOffsetFromBorder, anchor="nw", angle=0, text="Press a button to join", font=("Purisa", 30), fill="white")
                self.player2_text = canvas.create_text(sett.playerIntroTextOffsetFromBorder, sett.screenHeight/2-sett.playerIntroTextOffset, anchor="nw", angle=270, text="Press a button to join", font=("Purisa", 30), fill="white")
                self.player3_text = canvas.create_text(sett.screenWidth/2+sett.playerIntroTextOffset, sett.playerIntroTextOffsetFromBorder, anchor="nw", angle=180, text="Press a button to join", font=("Purisa", 30), fill="white")
                self.player4_text = canvas.create_text(sett.screenWidth-sett.playerIntroTextOffsetFromBorder, sett.screenHeight/2+sett.playerIntroTextOffset, anchor="nw", angle=90, text="Press a button to join", font=("Purisa", 30), fill="white")
            else:
                # Intro loop
                nowTime = time.time()
                if self.preTime < nowTime-1:
                    self.preTime=nowTime
                    canvas.itemconfigure(self.player1_text, state='hidden')
                    canvas.itemconfigure(self.player2_text, state='hidden')
                    canvas.itemconfigure(self.player3_text, state='hidden')
                    canvas.itemconfigure(self.player4_text, state='hidden')
                else:
                    canvas.itemconfigure(self.player1_text, state='normal')
                    canvas.itemconfigure(self.player2_text, state='normal')
                    canvas.itemconfigure(self.player3_text, state='normal')
                    canvas.itemconfigure(self.player4_text, state='normal')
                    
        elif mainLoop:
            print("main loop running")
        else:
            print("ending")



