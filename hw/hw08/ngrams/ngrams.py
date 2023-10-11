from ngram_frequencies import generate_ngram_freqs
from text_cleaner import TextCleaner


def print_ngram(ngram_type, name, word_lists):
    ngram_freqs = generate_ngram_freqs(ngram_type, word_lists)
    print(f"Top 10 {name}:")
    for ngram in ngram_freqs.top_n_freqs(10):
        print(f"\t{ngram}")


def main():
    out = open('corpse_bride.txt', "r")
    file = out.read()

    word_lists = TextCleaner().clean(file)
    [print_ngram(n, f"{n}-grams", word_lists) for n in range(1, 4)]

main()