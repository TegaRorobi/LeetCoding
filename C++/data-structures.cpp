# include<iostream>

using std::cout;
using std::endl;

class ListNode{
public:
	int val;
	ListNode* next;

	ListNode(int value): val(value), next(nullptr) {}
}


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
			cout << current->val << " -> ";
			current = current->next;
		}
		cout << "nullptr" << endl;
	}
}


class TreeNode {
public:
	int val;
	TreeNode* left;
	TreeNode* right;

	TreeNode(int value): val(value), left(nullptr), right(nullptr) {}
}