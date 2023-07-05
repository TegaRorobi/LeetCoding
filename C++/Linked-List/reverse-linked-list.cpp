#include <iostream>

using std::cout;
using std::endl;

class ListNode {
public:
    int val;
    ListNode* next;

    ListNode(int value) : val(value), next(nullptr) {}
};

class LinkedList {
public:
    ListNode* head;

    LinkedList() : head(nullptr) {}

    void insert(int value) {
        ListNode* newNode = new ListNode(value);

        if (head == nullptr) {
            head = newNode;
        } else {
            ListNode* current = head;
            while (current->next != nullptr) {
                current = current->next;
            }
            current->next = newNode;
        }
    }

    void display() {
        ListNode* current = head;
        while (current != nullptr) {
            cout << current->val << " -> ";
            current = current->next;
        }
        cout << "nullptr" << endl;
    }
};


void reverseList(LinkedList & list) {
    ListNode* head = list.head;
    ListNode* prev = nullptr;
    ListNode* next = nullptr;
    while (head != nullptr) {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    list.head = prev;
}

// doing it in place with just pointers for the fun of it
void reverseList2(LinkedList & list) {
    ListNode** head = &(list.head);
    ListNode* prev = nullptr;
    ListNode* nxt = nullptr;

    while (*head != nullptr) {
        nxt = (*head)->next;
        (*head)->next = prev;
        prev = (*head);
        (*head) = nxt;
    }

    *head = prev;
}

int main() {
    LinkedList list;

    // Inserting values into the linked list
    list.insert(1);
    list.insert(2);
    list.insert(3);
    list.insert(4);
    list.insert(5);

    cout << "Original Linked List: ";
    list.display();

    // Reversing the linked list
    reverseList(list);

    cout << "Reversed Linked List: ";
    list.display();

    return 0;
}