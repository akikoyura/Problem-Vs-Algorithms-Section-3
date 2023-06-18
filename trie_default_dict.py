import collections


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
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
    # Add words
    valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
    word_trie = Trie()
    for valid_word in valid_words:
        word_trie.add(valid_word)

    print(word_trie.exists('the'))

    # Tests
    assert word_trie.exists('the')
    assert word_trie.exists('any')
    assert not word_trie.exists('these')
    assert not word_trie.exists('zzz')
    print('All tests passed!')
