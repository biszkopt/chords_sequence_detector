import pyaudio  # Soundcard audio I/O access library
import wave # Python 3 module for reading / writing simple .wav files
import os

class MicRecorder:

    # Setup channel info
    FORMAT = pyaudio.paInt16  # data type formate
    CHANNELS = 2  # Adjust to your number of channels
    RATE = 44100  # Sample Rate
    CHUNK = 1024  # Block Size
    WAVE_OUTPUT_FILENAME = "file.wav"

    record_seconds = 5  # Record time

    # Startup pyaudio instance
    audio = pyaudio.PyAudio()
    last_recording = None

    def __init__(self):
        pass

    def rec(self, record_seconds=None):
        if record_seconds is None:
            record_seconds = self.record_seconds

        # start Recording
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                 rate=self.RATE, input=True,
                                 frames_per_buffer=self.CHUNK)
        print("recording...")
        self.last_recording = []

        # Record for record_seconds
        for i in range(0, int(self.RATE / self.CHUNK * record_seconds)):
            data = stream.read(self.CHUNK)
            self.last_recording.append(data)
        print("finished recording")

        # Stop Recording
        stream.stop_stream()
        stream.close()
        self.audio.terminate()

    def output_file(self, frames=None):
        if frames is None:
            frames = self.last_recording

        self._frames_to_wav(frames)

        return os.path.dirname(__file__) + '/' + self.WAVE_OUTPUT_FILENAME

    def _frames_to_wav(self, frames):
        # Write your new .wav file with built in Python 3 Wave module
        with wave.open(self.WAVE_OUTPUT_FILENAME, 'wb') as wave_file:
            wave_file.setnchannels(self.CHANNELS)
            wave_file.setsampwidth(self.audio.get_sample_size(self.FORMAT))
            wave_file.setframerate(self.RATE)
            wave_file.writeframes(b''.join(frames))


