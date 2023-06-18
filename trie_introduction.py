basic_trie = {
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    'h': {
        'i': {'word_end': True},
        'word_end': False
    }
}


def is_word(word):
    """
    Look for the word in `basic_trie
    """
    current_node = basic_trie
    for char in word:
        if char not in current_node:
            return False
        current_node = current_node[char]
    return current_node['word_end']


def test_is_words(test_words):
    for word in test_words:
        if is_word(word):
            print('"{}" is a word'.format(word))
        else:
            print('"{}" is not a word'.format(word))


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def exists(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word


if __name__ == '__main__':
    print('Is "a" a word: {}'.format(basic_trie['a']['word_end']))
    print('Is "ad" a word: {}'.format(basic_trie['a']['d']['word_end']))
    print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))

    # test is words
    test_is_words(['ap', 'add'])

    word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
    word_trie = Trie()

    # Add words
    for word in word_list:
        word_trie.add(word)

    # Test words
    test_words = ['bear', 'goo', 'good', 'goos']
    for word in test_words:
        if word_trie.exists(word):
            print('"{}" is a word.'.format(word))
        else:
            print('"{}" is not a word.'.format(word))
