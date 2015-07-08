class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.end = 0
        self.son = [None for i in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if node.son[index]:
                node = node.son[index]
            else:
                node.son[index] = TrieNode()
                node = node.son[index]
        node.end = 1


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.son[index]:
                return False
            node = node.son[index]
        if node.end == 1:
            return True
        else:
            return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not node.son[index]:
                return False
            node = node.son[index]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

trie = Trie()
trie.insert("abcd")
print trie.search("abcd")
print trie.startsWith("abcd")
trie.insert("abce")
print trie.search("abce")