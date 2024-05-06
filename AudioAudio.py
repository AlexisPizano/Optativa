import pyaudio
import wave
import speech_recognition as sr
import pyttsx3

def grabar_audio(nombre_archivo, duracion):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Grabando...")

    frames = []

    for i in range(0, int(RATE / CHUNK * duracion)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("¡Grabación completada!")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(nombre_archivo, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def convertir_audio_a_texto(nombre_archivo):
    recognizer = sr.Recognizer()

    with sr.AudioFile(nombre_archivo) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="es-ES")
        return text

def leer_texto_en_voz(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(texto)
    engine.runAndWait()

def main():
    nombre_archivo = "grabacion.wav"
    duracion_grabacion = 7  # Duración de la grabación en segundos

    input("Presiona Enter para comenzar a grabar...")
    grabar_audio(nombre_archivo, duracion_grabacion)
    print("Audio grabado satisfactoriamente.")

    texto = convertir_audio_a_texto(nombre_archivo)
    print("Texto obtenido:", texto)

    opcion = input("¿Quieres escuchar el texto? (s/n): ")
    if opcion.lower() == "s":
        leer_texto_en_voz(texto)

if __name__ == "__main__":
    main()
