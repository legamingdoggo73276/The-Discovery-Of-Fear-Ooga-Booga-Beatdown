from pygame import mixer 
mixer.init()

mixer.music.load('fire-crackling.mp3')
mixer.music.play()

#test lol, doubt will be using this
#counts in seconds
mixer.music.set_pos(660)
mixer.music.queue('C418-haggstrom.mp3')

print(mixer.music.get_busy())

print(mixer.music.get_volume())
mixer.music.set_volume(0.81)
print(mixer.music.get_volume())


print(mixer.music.get_pos())

#counts in miliseconds
#also stops the audio
#mixer.music.fadeout(10000)
#print(mixer.music.get_pos())


'p to pause'
'u to unpase'
's to stop/exit'
'r to rewind'

while True: 
    inp = input(' ')
    if inp == 'p':
        mixer.music.pause()
        print(mixer.music.get_busy())
    elif inp == 'u':
        mixer.music.unpause()
        print(mixer.music.get_busy())
    elif inp == 's':
        mixer.music.stop()
        print(mixer.music.get_busy())
        break
    elif inp == 'r':
        mixer.music.rewind()
        print(mixer.music.get_busy())
    
    