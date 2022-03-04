import music_theory as mt
import music_works as mw
from midiutil.MidiFile import MIDIFile
from random import choice, randint

midi = MIDIFile(1, adjust_origin=True)
midi.addTempo(0, 0,180)
midi.addProgramChange(0,0,0,12)

scale=mt.create_scale("A","Pentatonic",1)

cnt=0
for note in scale:
    midi.addNote(0,0,note,cnt,1,100)
    cnt+=1
print(scale)
with open('output.mid', 'wb') as f:
	midi.writeFile(f)

mw.play("output.mid")

