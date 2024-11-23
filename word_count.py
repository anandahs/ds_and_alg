from collections import Counter


def count_word_frequency(words):
    counter_dict = dict(Counter(words))
    print(counter_dict)


def count_word_frequency2(words):
    words_count = dict()

    for word in words:
        if word in words_count:
            words_count[word] = words_count[word] + 1
        else:
            words_count[word] = 1

    print(words_count)


def count_word_frequency3(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


if __name__ == "__main__":
    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
    count_word_frequency(words)

if __name__ == "__main__":
    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
    count_word_frequency(words)
    count_word_frequency2(words=words)
    count_word_frequency3(words=words)
