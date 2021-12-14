from musx import Note, Seq, Score, MidiFile
from musx.midi.gm import *
from sys import argv
from random import randint

fileName = "presentation"
scale = [-5, -3, -1, 0, 2, 4, 5, 7, 9, 11, 12, 14, 16]
ins = {1: ElectricGrandPiano, 2: Flute, 3: Clarinet, 4: Oboe, 5: Trumpet, 6: Trombone, 7: Tuba, 8: Xylophone, 10: Woodblock, 11: BlownBottle}


def duckduckgoose(score, seed=0, phraseLength=2, pitchInit=60, repeat=1):
    # initial information for game
    rhy = 2/phraseLength
    seedPrev = 1
    # step = 7

    # number of go-arounds in game
    for _ in range(repeat):
        # order of instruments to play melodic element
        for s in seed:
            if s == 0:
                s = 10
            elif s == 9:
                s = 11

            # potentially run Goose, 20% chance
            gooseValue = randint(1,5)
            if gooseValue == 2:
                score.compose(goose(score, phraseLength, pitchInit, s, seedPrev))
            else: # otherwise, run the next instrument in the sequence

                # number of notes to play in a phrase
                for _ in range(phraseLength):
                    duckNote = Note(time=score.now, duration=rhy, pitch=int(pitchInit + scale[randint(0, len(scale) - 1)]), amplitude=0.5, instrument=s)
                    score.add(duckNote)
                    yield rhy
                seedPrev = s


def goose(score, phraseLength, pitch, ins1, ins2):
    print("HONK!")
    # gooseStep = 3
    gooseRhy = 1/phraseLength
    # two instruments kinda duet with each other in an alternate key
    for _ in range(phraseLength * 5):
        duetTime = score.now
        gooseNote1 = Note(time=duetTime, duration=gooseRhy, pitch=int(pitch + 1 + scale[randint(0, len(scale) - 1)]), amplitude=0.75, instrument=ins1)
        gooseNote2 = Note(time=duetTime, duration=gooseRhy, pitch=int(pitch + 1 + scale[randint(0, len(scale) - 1)]), amplitude=0.75, instrument=ins2)
        score.add(gooseNote1)
        score.add(gooseNote2)
        yield gooseRhy


def end(score, pitch, phraseLength):
    endTime = score.now
    for i in ins:
        
        endNote = Note(time=endTime, duration = 4/phraseLength, pitch=pitch, amplitude=0.65, instrument = i)
        score.add(endNote)


def init():
    # Take in a seed from the user
    try:
        if argv[1] != -1:
            seed = [int(x) for x in str(argv[1])]
        else: seed = [randint(0,9) for s in "music three oh five"]
    except:
        seed = [randint(0,9) for s in "music three oh five"]

    # Take in a phrase length from the user
    try:
        if argv[2] != -1:
            phraseLength = int(argv[2])
        else: phraseLength = randint(1,8)
    except:
        phraseLength = randint(1,8)

    # Take in a starting pitch from the user
    try:
        if argv[3] != -1:
            pitch = int(argv[3])
        else: pitch = randint(55,66)
    except:
        pitch = randint(55, 66)

    # Take in a number of repeats from the user
    try:
        if argv[4] != -1:
            repeat = int(argv[4])
        else: repeat = 1
    except:
        repeat = 1

    # Print and return command line results
    print("seed -> " + str([x for x in seed]))
    print("phraseLength -> " + str(phraseLength))
    print("pitch -> " + str(pitch))
    print("repeats -> " + str(repeat))
    return seed, phraseLength, pitch, repeat


# This makes me sad :(
# def stepOp(index):
#     result = index
#     result += randint(-2,2)    
#     result += int(pick(-1, -1, -1, -1, 0, 1, 1, 1, 1)) % (len(scale) - 1)
#     if result < 0:
#         result = 0
#     return result


if __name__ == '__main__':
    
    # command-line data
    seed, phraseLength, pitch, repeat = init();

    # composition-writing material
    track0 = MidiFile.metatrack(tempo=80, timesig=[4,4], keysig=[0,0], ins=ins)
    track1 = Seq()
    score = Score(out=track1)

    # creating score
    score.compose(duckduckgoose(score, seed, phraseLength, pitch, repeat))
    end(score, pitch, phraseLength)
    file = MidiFile(fileName + ".mid", [track0, track1]).write()
    print(fileName + ".mid successfully written.")
