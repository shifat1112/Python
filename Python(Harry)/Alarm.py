from audio import AudioPlayer
import time

def alarm(sec):
    counter = 0
    while counter<sec:
        time_left = sec - counter
        print(f"{time_left} sec left")
        time.sleep(1)
        counter =+ 1
alarm(5)
AudioPlayer("audio.wav").play(block=True)
