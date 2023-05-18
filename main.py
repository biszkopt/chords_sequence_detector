from MicRecorder import MicRecorder
from ChordDecoder import ChordDecoder

# script params ----------------------------------------

record_seconds = 0.1
chords_sequence = ["C, D, E, F, G, A, B"]


# ------------------------------------------------------

recorder = MicRecorder()
decoder = ChordDecoder()
#seqdec = SequenceDetector()
#out = OutputDriver()

recorder.record_seconds = record_seconds

#seqdec.sequence = chords_sequence
#seqdec.ignore_duplicates = True  # if prev_chord == chord then pass, ale jeśli chord=none(bo cisza) to już nie ignoruje

while True:

    recorder.rec()
    audio_file_path = recorder.output_file()

    chords = decoder.analyze(audio_file_path)
    print(chords)
    #seqdec.analyze(chords)

    #if seqdec.detected:
        #out.toggle()
        #seqdec.restart()














