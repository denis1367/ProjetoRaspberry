from gtts import gTTS
import os
AudioDoTexto = gTTS(text='mas e claro que o sooolllll, , vai voltar amanhannn, mais uma vez eu sei!',lang='pt')
AudioDoTexto.save("/tmp/audio.mp3")
os.system("mpg321 /tmp/audio.mp3")
