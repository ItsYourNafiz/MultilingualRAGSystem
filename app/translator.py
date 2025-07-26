from langdetect import detect
from googletrans import Translator

translator = Translator()

def translate_to_english(text):
    if detect(text) == "en":
        return text
    return translator.translate(text, src='bn', dest='en').text

def translate_to_original(text, original_lang='bn'):
    return translator.translate(text, src='en', dest=original_lang).text
