def get_min_and_max_words(sentence):
    words = sentence.split(" ")
    min_word = min(words, key=len)
    max_word = max(words, key=len)

    print("Mot le plus petit:", min_word)
    print("Mot le plus long:", max_word)

    return min_word, max_word


def get_min_and_max_words_sorted(sentence):
    words = sentence.split(" ")
    sorted_words = sorted(words)
    min_word = min(sorted_words, key=len)
    max_word = max(sorted_words, key=len)

    print("Mot le plus petit:", min_word)
    print("Mot le plus long:", max_word)

    return min_word, max_word


get_min_and_max_words("Un qq sachant chasser sait chasser sans son chien")
get_min_and_max_words_sorted("Un qq sachant chasser sait chasser sans son chien")
