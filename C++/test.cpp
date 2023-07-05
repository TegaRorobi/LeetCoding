
# include <iostream>
# include <string>
# include <unordered_map>

class Trie {
public:
	struct TrieNode {
		bool isEndOfWord;
		std::unordered_map<char, TrieNode*> children;

		TrieNode() :isEndOfWord(false) {};
	};

	// the root attribute(a pointer to a TrieNode)
	TrieNode* root;

	// the constructor
	Trie(){ root = new TrieNode();}

	// method for inserting words to the trie
	void insert(std::string word) {
		TrieNode* curr = root;
		for (char c: word) {
			if (curr->children.find(c) == curr->children.end()){
				curr->children[c] = new TrieNode();
			}
			curr = curr->children[c];
		}
		curr->isEndOfWord = true;
	}

	// method to search for a word in a trie
	bool search(std::string word) {
		TrieNode* node = searchPrefix(word);
		return (node != nullptr && node->isEndOfWord);
	}

	// method to search if any word in the trie starts with an input string
	bool startsWith(std::string word) {
		TrieNode* node = searchPrefix(word);
		return node != nullptr;
	}

private:
	TrieNode* searchPrefix(std::string word) {
		TrieNode* curr = root;
		for (char c:word) {
			if (curr->children.find(c)==curr->children.end())
				return nullptr;
			curr = curr->children[c];
		}
		return curr;
	};
};



int main() {
	Trie trie;

	trie.insert("apple");
	trie.insert("banana");
	trie.insert("ban");
	trie.insert("array");

	std::cout << "'apple' in the trie: " << trie.search("apple") << std::endl;
	std::cout << "'array' in the trie: " << trie.search("array") << std::endl;

	std::cout << "a word in the trie starts with 'ban': " << trie.startsWith("g") << std::endl;
	std::cout << "a word in the trie starts with 'arr': " << trie.startsWith("arr") << std::endl;
}