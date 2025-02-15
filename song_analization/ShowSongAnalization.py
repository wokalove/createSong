import os
from SpeechRecognizer import SpeechRecognizer
from MusicNoteDetection import MusicNoteDetection
from ConvertSongToPdf import ConvertSongToPdf
from LanguageRecognition import LanguageRecognition

class ShowSongAnalization:
    def combineSpeechAndNotesRecognition(self, audio_file, title):
        sr = SpeechRecognizer()
        detected_lang = LanguageRecognition().recognizeLanguageFromAudio(48000,audio_file)
        text = sr.textTransciption(audio_file, detected_lang)
        notes = MusicNoteDetection().note_detect(audio_file)
        
        ConvertSongToPdf().convertDataToPdf(text, notes, title, detected_lang)
	

# if __name__ == "__main__":
#     path = os.getcwd()
#     file_name = path + "/music_files/polska.wav"
#     title = "New song"
#     ShowSongAnalization().combineSpeechAndNotesRecognition(file_name, title)
    
    