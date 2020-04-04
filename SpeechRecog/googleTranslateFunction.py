import googletrans
from googletrans import Translator

class Translate(object):
    def DAVIDtranslator(self, text):
        # Takes in a same string and returns the message
        # In the language of the users choice
        words = text.split(" ")
        start = words.index("translate")
        indexWords = ["in", "to", "into"]
        language = None
        for word in indexWords:
            if words[-2] == word:
                language = words[-1]
                if language == "Chinese":
                    language = "chinese (simplified)"
                words = " ".join(words[start+1:-2])
                break
        if language == None: 
            language = "english"
            words = " ".join(words[start+1:])
        translator = Translator()
        result = translator.translate(words, dest = language)
        answer = result.text
        return answer