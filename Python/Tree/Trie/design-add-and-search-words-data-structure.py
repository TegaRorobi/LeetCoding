class DictNode:
    isWord = False
    children = {}


class WordDictionary:
    "Uses an external DictNode class with a hashmap"
    def __init__(self):
        self.root = DictNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = DictNode()
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word, node=None, ind=0) -> bool:
        curr = node or self.root
        for i in range(ind, len(word)):
            char = word[i]
            if char == '.':
                for child_node in curr.children.values():
                    if self.search(word, child_node, i+1):
                        return True
                return False
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord


class WordDictionary2:
    "Creates child nodes of itself."
    def __init__(self):
        self.isWord = False
        self.children = {}

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionary2()
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self
        for ind in range(len(word)):
            char = word[ind]
            if char == '.':
                for child_dict in curr.children.values():
                    if child_dict.search(word[ind+1:]):
                        return True
                return False
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord


class WordDictionary3:
    "Uses a stack and the difference between the ord values as indices "
    "to track the next dictionary values down the trie."
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False 

    def addWord(self, word):
        curr = self
        for c in word:
            if not curr.children[ord(c)-ord('a')]:
                curr.children[ord(c)-ord('a')] = WordDictionary3()
            curr = curr.children[ord(c)-ord('a')]
        curr.isWord = True 

    def search(self, word):
        curr = self
        for i in range(len(word)):
            char = word[i]
            if char == '.':
                for child_dict in curr.children:
                    if child_dict != None and child_dict.search(word[i+1:]):
                        return True
                return False
            if curr.children[ord(char)-ord('a')] is None:
                return False
            curr = curr.children[ord(char)-ord('a')]
        return curr.isWord



obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')

print(obj.search('pad'))
print(obj.search('mad'))
print(obj.search('.ad'))
print(obj.search('b..'))