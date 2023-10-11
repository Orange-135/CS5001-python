from text_cleaner import sentence_to_word_list


def test_sentence_to_word_list():
    TEST_ATTRIBUTE = "test attribute"
    word_list = ["test","attribute"]
    assert sentence_to_word_list(TEST_ATTRIBUTE) == word_list