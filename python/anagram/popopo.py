class Anagrams(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.indexed_words = {}
        self.preprocess()

    def make_key(self, word):
        sorted_word = list(word)
        sorted_word.sort()
        return tuple(sorted_word)

    def preprocess(self):
        for word in self.dictionary:
            key = self.make_key(word)
            self.indexed_words.setdefault(key, []).append(word)

    def anagram(self, word):
        key = self.make_key(word)
        return tuple(self.indexed_words[key])

    def anagrams(self):
        return [anagrams for key, anagrams in self.indexed_words.iteritems()
                if len(anagrams) > 1]
