# Healty Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 liters) - drank - log - every 40 mins
# Eyes - eyes.mp3 - every 30 min - done - log - every 30 min
# Physical activity - physical.mp3 - every 45 mins - done - log 
# use pygame module to play music


from pygame import mixer
from datetime import datetime
from time import time

def music_in_loop(file ,stopper):
    mixer.init()                      # Starting the mixer
    mixer.music.load(file)            # Loading the music
    mixer.music.play()                # Start playing the song 

    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
    
def log(msg):
    with open ("mylogs.txt", "a") as f:
        f.write(f"{msg}{datetime.now()}\n")
            
if __name__ == "__main__":
    # music_in_loop("water.mp3" , "stop")
    init_water = time()
    init_eye = time()
    init_activity = time()
    water_sec = 40*60
    eye_sec = 30*60
    activity_sec = 45*60

    while True:
        if time() - init_water > water_sec:
            print("Water Drinking Time. Enter drank to stop the program.")
            music_in_loop("Water.mp3", "drank")
            init_water = time()
            log("Drank water at:")
            
        if time() - init_eye > eye_sec:
            print("Eye Exercise Time. Enter done to stop the program.")
            music_in_loop("exercise.mp3", "done")
            init_eye = time()
            log("Done exercise at:")
            
        if time() - init_activity > activity_sec:
            print("Activity Time. Enter done to stop the program.")
            music_in_loop("exercise.mp3", "done")
            init_activity = time()
            log("Done activity at:")
            