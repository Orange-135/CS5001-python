from word_ladder import WordLadder


def test_make_ladder():
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}

    w1 = "angel"
    w2 = "devil"
    wl = WordLadder(w1, w2, valid_words[len(w1)])
    assert wl.make_ladder().items == ["angel", "anger", "aeger", "leger", "lever", "level", "devel", "devil"]

