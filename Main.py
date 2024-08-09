import time

from threading import Thread, Lock

import sys



lock = Lock()



def animate_text(text, delay=0.1):

    with lock:

        for char in text:

            sys.stdout.write(char)

            sys.stdout.flush()

            time.sleep(delay)

        print()



def sing_lyric(lyric, delay, speed):

    time.sleep(delay)

    animate_text(lyric, speed)



def sing_song():

    lyrics = [

        ("Nights are the hardest", 0.1),
        ("But I'll be okay", 0.1),
        ("If we are meant to be", 0.11),
        ("Hey, we'll find our way", 0.1),
        ("But now, let it be", 0.2),
        ("Cause you know what they say", 0.1),
        ("If you love somebody", 0.1),
        ("Gotta set them free...", 0.1),
        ("I love you but I'm letting go", 0.13),
        ("I love you but I'm letting go", 0.13),
        ("I love you but I'm letting go", 0.15),
        ("I love you but I'm letting go", 0.13),
        ("AKU GA BISA YURAA, AKU MAU NYERAH AJA🥲", 0.1) 
    ]

    delays = [3.0, 5.80, 7.9, 9.16, 12.92, 18.9, 19.0, 19.1, 28.3, 34.8, 41.4, 47.9, 52.0]

    

    threads = []

    for i in range(len(lyrics)):

        lyric, speed = lyrics[i]

        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))

        threads.append(t)

        t.start()

    

    for thread in threads:

        thread.join()



if __name__ == "__main__":

    sing_song()
