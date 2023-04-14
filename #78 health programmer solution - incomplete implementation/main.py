import time
from pygame import mixer
from datetime import datetime
# from pygame import * wrong practice

def musicLoop(file,stopper):
    mixer.init()
    mixer.music.load(f"#78 health programmer solution\{file}.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play()
    while True:
        query = input(" ")
        if query == stopper :
            mixer.music.stop()
            break

def loggIn(msg):
    with open('#78 health programmer solution\mylogs.txt','a') as f:
        f.write(f"{msg} at {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time.time()
    init_eye = time.time()
    init_Phy = time.time()
    raise_water =60*40
    raise_eye = 60*30  #take time in sec
    raise_Phy = 60*45

    while True:
        if time.time() - init_water > raise_water:
            print("water drinking time . To stop alarm press 'r'")
            musicLoop('song','r')
            init_water = time.time()
            loggIn('water drink')

        if time.time() - init_eye > raise_eye:
                    print("eye excercise time . To stop alarm press 'r'")
                    musicLoop('song','r')
                    init_eye = time.time()
                    loggIn('eye excercise')

        if time.time() - init_Phy > raise_Phy:
                    print("Physical time . To stop alarm press 'r'")
                    musicLoop('song','r')
                    init_Phy = time.time()
                    loggIn('physical excercise')