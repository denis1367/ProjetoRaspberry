# -*- coding: utf-8 -*-
import pyaudio
import wave
while True:
    p= raw_input(str("denis"))
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 2 #ESTE E O TEMPO DE GAVAÇÃO
    WAVE_OUTPUT_FILENAME = p+".wav" # NOME DO ARQUIVO WAV
    audio = pyaudio.PyAudio()
    #INICIA A GRAVAÇÃO
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print " GRAVANDO"
    frames= []
    for i in range(0, int(RATE /CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print "termino da gravação"

    #~PARANDO A GRAVAÇÃO
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
