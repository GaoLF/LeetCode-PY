class Trietree:
    def __init__(self):
        self.key = False
        self.son = [None for i in xrange(26)]
class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.tree = Trietree()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        root = self.tree
        for i in word:
            index = ord(i) - ord('a')
            if not root.son[index]:
                root.son[index] = Trietree()
            root = root.son[index]
        root.key = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        root = self.tree
        return self.check(word,root)

    def check(self,word,root):
        #print word
        x = 0
        for i in word:
           # print i
            if i == '.':
                for j in root.son:
                    if j and self.check(word[x+1:],j):
                        return True
                return False
            else:
                index = ord(i) - ord('a')
                #print index,word
                if root.son[index]:
                    root = root.son[index]
                else:
                    return False
            x += 1
        if root.key:
            return True
        return False

# Your WordDictionary object will be instantiated and called as such:
A = WordDictionary()
A.addWord("a")
#print A.search("pattern")
#A.addWord("a")
print A.search(".a")
A.addWord("bad")
"""
print A.search("bad")
A.addWord("xteate")
print A.search("b..")
print A.search("")
"""