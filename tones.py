# written by Sherri Goings
# with some code borrowed from <unknown source>
# 9-10-10

#! /usr/bin/env python

import sys, math, aifc
from contextlib import closing

DOT = 30
DAH = 3 * DOT
OCTAVE = 1.5                              # 1 == 441 Hz, 2 == 882 Hz, ...

nowave = b'\0' * 200

def mkwave(octave):    
    sinewave = bytearray()
    for i in range(int(400/octave)):
        val = int(math.sin(math.pi * i * octave / 50.0) * 30000)
        sinewave.extend([(val >> 8) & 255, val & 255])
    return bytes(sinewave)

defaultwave = mkwave(OCTAVE)
fp = aifc.open("music.aifc", 'w') 

notes = [1]
notes.append(1.075)
notes.append(1.135)
notes.append(1.19)
notes.append(1.265)
notes.append(1.333)
notes.append(1.417)
notes.append(1.497)
notes.append(1.58)
notes.append(1.679)
notes.append(1.785)
notes.append(1.885)
notes.append(2)

def setup():
    fp.setframerate(44100)
    fp.setsampwidth(2)
    fp.setnchannels(1)

def addNote(pitch, length):
    newwave = mkwave(notes[pitch])
    sine(fp, int(notes[pitch]*length), newwave)

    
def addPause(length):
    pause(fp, length)   
        
def closefile():
    print("\nWrote music to file music.aifc\n")
    fp.close()
     
def sine(fp, length, wave):
    for i in range(length):
        fp.writeframesraw(wave)

def pause(fp, length):
    for i in range(length):
        fp.writeframesraw(nowave)


def main():
    ''' tests current note range '''
    setup()
    for i in range(13):
        addNote(i,50)
    closefile()

if __name__=="__main__":
    main()
