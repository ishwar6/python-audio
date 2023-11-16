import json

from audio_recognizer import AudioRecognizer
from audio_recognizer.logic.recognizer.file_recognizer import FileRecognizer
from audio_recognizer.logic.recognizer.microphone_recognizer import MicrophoneRecognizer



# UPDATED DATABASE CONFIGURATION
config = {
    "database": {
        "host": "localhost",
        "user": "abhi",  
        "password": "1234",
        "database": "audio_test_db",
    },
    "database_type": "postgres"
}



if __name__ == '__main__':

    # create a AudioRecognizer instance
    arc = AudioRecognizer(config)

    # Fingerprint all the mp3's in the directory we give it
    arc.fingerprint_directory("test", [".wav",".mp3"])

    # important
    # 1
    # Recognize audio from a file
    results = arc.recognize(FileRecognizer, "mp3/725376412393_01_01_org.mp3")
    print(f"From file we recognized: {results}\n")


    # # # Or use a recognizer without the shortcut, in anyway you would like
    # recognizer = FileRecognizer(arc)
    # results = recognizer.recognize_file("mp3/757226296709.mp3")
    # print(f"No shortcut, we recognized: {results}\n")


