# include<iostream>
# include <string>
# include <unordered_map>



struct ListNode{
	int val;
	ListNode* next;

	ListNode(int value): val(value), next(nullptr) {}
};

class LinkedList{
public:
	ListNode* head;

	// constructor
	LinkedList(): head(nullptr) {}

	// helper function to insert values
	void insert(int value){
		ListNode* newNode = new ListNode(value);

		if (head == nullptr) {
			head = newNode;
		} else {
			ListNode* current = head;
			while (current->next != nullptr)
				current = current->next;
			current->next = newNode;
		}
	}

	// helper function to display the linked list
	void display() {
		ListNode* current = head;
		while (current != nullptr) {
			std::cout << current->val << " -> ";
			current = current->next;
		}
		std::cout << "nullptr" << std::endl;
	}
};

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

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
	return 0;
}