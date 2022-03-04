
NOTES=["C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/B","H"]

CHORDS={
    "Maj":[0,4,3],
    "Min":[0,3,4],
    "Dim":[0,3,3],
    "Aug":[0,4,4],
    "7":[0,4,3,3],
    "sus2":[0,2,5],
    "sus4":[0,5,2], #add2 és add9
    "Maj7":[0,4,3,4],
    "Min7":[0,3,4,3],
    "Minmaj7":[0,3,4,4],
    "Min75b":[0,3,3,4],
    "Dimmin7":[0,3,3,3],
    "Augmaj7":[0,4,4,3],
    "Augmin7":[0,4,4,2],
    "Min75b9b":[0,3,3,4,3],
    "Min75b9":[0,3,3,4,4],
    "9b":[0,3,3,3,4],
    "Maj79b":[0,4,3,3,3],
    "Maj79":[0,4,3,3,4],
    "Maj9b":[0,4,3,4,2],
    "Maj79":[0,4,3,4,3],
    "Maj79#":[0,4,3,4,4],
    "Min79b":[0,3,4,3,3],
    "Min79":[0,3,4,3,4],
    "Minmaj79b":[0,3,4,4,2],
    "Minmaj79":[0,3,4,4,3],
    "Augmaj79b":[0,4,4,3,2],
    "Augmaj79":[0,4,4,3,3],
    "Augmaj79#":[0,4,4,3,4],
    "Aug79b":[0,4,4,2,3],
    "Augmin79":[0,4,4,2,4]
    }

SCALES={
    "Modal":[2,2,1,2,2,2,1],
    "Harmonic":[2,1,2,2,1,3,1],
    "Melodic":[2,1,2,2,2,1],
    "Moll Blues":[3,2,1,1,3,1],
    "Pentatonic":[2,2,3,2,3]
}

MODAL_SCALE_NAMES=["Ionian",
    "Dorian",
    "Phrygian",
    "Lydian",
    "Mixolydian",
    "Aeolian",
    "Locrian"]

GUITAR_STRINGS={
    "E":40,
    "A":45,
    "D":50,
    "G":55,
    "H":59,
    "e":64
}

def get_note(note_num):
    return NOTES[note_num%12]

def create_chord(base_note:int,chord_type:str):
    notes=[]
    steps=0
    for i in range(0,len(CHORDS[chord_type])):
        steps+=CHORDS[chord_type][i]
        notes.append(steps+base_note)
    return notes

def create_scale(basenote:str,scalename:str,degree:int):

    notes=[]
    if type(degree)==str:
        if MODAL_SCALE_NAMES.index !=-1:
            degree=MODAL_SCALE_NAMES.index(degree)+1
    cnt=0
    for i in range(NOTES.index(basenote),128):
        if cnt>110:
            return notes
        cnt+=SCALES[scalename][(i+degree-1)%len(SCALES[scalename])]
        notes.append(NOTES.index(basenote)+cnt)
        
    return notes


