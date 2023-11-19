from mido import MidiFile, Message
from tkinter import *
import numpy as np


whatabitch = MidiFile ("C:/Users/jairo/Documents/python/midi_files/whatabitch.mid", clip =True)
aiste = MidiFile ("C:/Users/jairo/Documents/python/midi_files/aistevalsas.mid", clip =True)
def displayNotes (mid):
    note_lib = {
        0: "C",
        1: "C#",
        2: "D",
        3: "D#",
        4: "E",
        5: "F",
        6: "F#",
        7: "G",
        8: "G#",
        9: "A",
        10: "A#",
        11: "B"
    }
    i=0
    notes = []
    print ("Opened midi file:", mid, "\n")
    for track in mid.tracks:
        print ("Track ",i, ": ", track)
        i+=1
    user_track=int(input("Select a track:\n"))

    for Message in mid.tracks[user_track]:
        if hasattr (Message, 'note'):

            notes.append (note_lib[(Message.note)%12]+str(int(np.floor(Message.note/12))))
    return notes




print (displayNotes(aiste))
