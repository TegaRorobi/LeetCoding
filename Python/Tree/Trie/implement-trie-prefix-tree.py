
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        return f"Trie(children={self.children}, isWord={self.isWord})"

    def insert(self, word: str) -> None:
        curr = self.root 
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert('orange')
obj.insert('apple')
# print(obj)
print(obj.search('orange'))
print(obj.startsWith('app'))
print(obj.search('mango'))

'''
Trie(children={
    'o': Trie(children={
        'r': Trie(children={
            'a': Trie(children={
                'n': Trie(children={
                    'g': Trie(children={
                        'e': Trie(children={}, 
                            isWord=True)}, 
                        isWord=False)}, 
                    isWord=False)}, 
                isWord=False)}, 
            isWord=False)}, 
        isWord=False), 
    'a': Trie(children={
        'p': Trie(children={
            'p': Trie(children={
                'l': Trie(children={
                    'e': Trie(children={}, 
                        isWord=True)}, 
                    isWord=False)}, 
                isWord=False)}, 
            isWord=False)}, 
        isWord=False)}, 
    isWord=False)
'''