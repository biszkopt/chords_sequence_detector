from MicRecorder import MicRecorder
from ChordDecoder import ChordDecoder
from SequenceDetector import SequenceDetector

# script params ----------------------------------------

record_seconds = 1
chords_sequence = "D, A, E, G, B, E".split(", ")
exceptions = "N".split(", ")
alternatives = "Dm, Am, Em, Gm, Bm, Em".split(", ")


# ------------------------------------------------------

recorder = MicRecorder()
decoder = ChordDecoder()
seqdec = SequenceDetector()
#out = OutputDriver()

recorder.record_seconds = record_seconds

recorder.open()

seqdec.sequence = chords_sequence
seqdec.ignore_duplicates = True  # if prev_chord == chord then pass, ale jeśli chord=none(bo cisza) to już nie ignoruje
seqdec.exceptions = exceptions
seqdec.alternatives = alternatives

while True:

    recorder.rec()
    audio_file_path = recorder.output_file()

    chords = decoder.analyze(audio_file_path)
    
    raw_chords = []
    
    for c in chords:
        raw_chords.append(c.chord)
            
        #if c.chord is not "N":
            #print(c.chord)
            
    
    
    seqdec.analyze(raw_chords)

    #if seqdec.detected:
        #out.toggle()
        #seqdec.restart()


recorder.close()












