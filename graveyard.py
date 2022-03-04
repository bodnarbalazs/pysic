# Configure a MIDI file with one track:
# midi = MIDIFile(1, adjust_origin=True)
# midi.addTempo(0, 0,180)

# # Select a random instrument:
# program = randint(0, 255)
#midi.addProgramChange(0, 0, 0, program)
# #https://pjb.com.au/muscript/gm.html
# midi.addProgramChange(0,0,0,24)


# Generate some random notes:
# duration = 1
# c_major = [60, 62, 64, 65, 67, 69, 71]
# for t in range(12):
# 	pitch = choice(c_major)
# 	# track, channel, pitch, time, duration, volume
# 	midi.addNote(0, 0, pitch, t * duration, duration, 100)
# midi.addNote(0,0,60,1,5,100)
# midi.addNote(0,0,64,1.5,4.5,100)
#midi.addNote(0,0,mt.GUITAR_STRINGS["e"],2,4,100)
# Write output file:
# with open('output.mid', 'wb') as f:
# 	midi.writeFile(f)


# thunder_tab=mw.Tab("bach.txt",180)
# mw.create_midi(thunder_tab,"bach.mid",27)

#chord=mt.CreateChord(60,"Min7")
# for note in chord:
#     midi.addNote(0,0,note,0,3,100)

# base=40
# cnt=0
# for i in range(0,40):
#     cnt+=mt.SCALES["Modal"][i%7]
#     midi.addNote(0,0,base+cnt,i,1,100)

# scale=mt.create_scale("E","Modal","Ionian")
# scale2=mt.create_scale("A","Modal","Ionian")

# cnt=0
# for note in scale:
#     midi.addNote(0,0,note,cnt,1,100)
#     cnt+=1
# cnt=0
# for note in scale2:
#     midi.addNote(0,1,note,cnt,1,100)
#     cnt+=1

#midi = MIDIFile(1, adjust_origin=True)
# midi.addTempo(0, 0,180)
# midi.addProgramChange(0,0,0,0)
# midi.addProgramChange(0,1,0,12)

# cnt=0
# for i in range(0,100):
#     midi.addNote(0,0,i,cnt,2,100)
#     cnt+=1
# with open('output.mid', 'wb') as f:
# 	midi.writeFile(f)