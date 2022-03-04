from midiutil.MidiFile import MIDIFile
import music_theory as mt
import pygame

class Tab:
    def __init__(self,filename,tempo):
        self.tempo=tempo
        with open(filename,"r") as f:
            lines=f.readlines()
            beats=0
            phonies=[]
            for i in range(0,len(lines)):
                if lines[i][0]=="e" and lines[i][1]=="|":
                    for e in range(0,len(lines[i])):
                        note_array=[]
                        for u in range(0,6):
                            add_beat=False
                            if lines[i+u][e].isnumeric():
                                if lines[i+u][e+1].isnumeric():
                                    note_array.append(list(mt.GUITAR_STRINGS.values())[5-u]+int(lines[i+u][e]+lines[i+u][e+1]))
                                    add_beat=True
                                elif not lines[i+u][e-1].isnumeric():
                                    note_array.append(list(mt.GUITAR_STRINGS.values())[5-u]+int(lines[i+u][e]))
                                    add_beat=True
                            elif lines[i+u][e]=="X":
                                add_beat=True
                            if add_beat:
                                beats+=1
                        phonies.append(Phony((60/tempo)*beats,note_array))
            self.phonies=phonies
                

class Phony:
    def __init__(self,time,note_array):
        self.time=time
        self.note_array=note_array

def create_midi(tab,output_filename,instrument_id):
    midi = MIDIFile(1, adjust_origin=True)
    midi.addTempo(0, 0,tab.tempo)
    #https://pjb.com.au/muscript/gm.html
    midi.addProgramChange(0,0,0,instrument_id)

    for phony in tab.phonies:
        for note in phony.note_array:
            midi.addNote(0,0,note,phony.time,60/tab.tempo,100)
            print(note)

    with open(output_filename, 'wb') as f:
	    midi.writeFile(f)

def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print("Music file loaded!")
    except pygame.error:
        print ("File not found!")
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

def play(file_name):
    freq = 44100    # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2    # 1 is mono, 2 is stereo
    buffer = 1024    # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)

    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(0.8)

    try:
        # use the midi file you just saved
        #play_music(music_file)
        play_music(file_name)
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit
