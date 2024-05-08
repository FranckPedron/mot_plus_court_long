def get_min_and_max_words(sentence):
    words = sentence.split(" ")
    min_word = min(words, key=len)
    max_word = max(words, key=len)

    print("Mot le plus petit:", min_word)
    print("Mot le plus long:", max_word)

    return min_word, max_word


get_min_and_max_words("Un chasseur sachant chasser sait chasser sans son chien")
