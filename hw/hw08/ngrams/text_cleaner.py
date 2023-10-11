import re


def add_word_to_word_list(word_list, word):
    word_list.append("".join(word))
    word.clear()


def sentence_to_word_list(sentence):
    word_list = []
    word = []
    for ch in sentence:
        if ch.isalnum() or ch == "'":
            word.append(ch)
        elif ch == ",":
            if word:
                add_word_to_word_list(word_list, word)
            word_list.append("COMMA")
        elif word:
            add_word_to_word_list(word_list, word)
    if word:
        add_word_to_word_list(word_list, word)
    return word_list


def sentences_to_word_lists(sentences):
    return [sentence_to_word_list(sentence) for sentence in sentences]


class TextCleaner:
    def __init__(self):
        self.replacements = {
            "mr.": "mr"
        }

    def clean(self, text):
     sentences = re.findall(r'\b[\w\']+\b|[,.]', text.lower())
     sentences = ['COMMA' if s == ',' else s for s in sentences]
     sentences = [self.replacements.get(s, s) for s in sentences]
     sentences = ' '.join(sentences).split('. ')
     sentences = [[word.strip("'") for word in s.split()] for s in sentences]
     return sentences
