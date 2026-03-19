#include <iostream>

using namespace std;

struct ListNode {
	int val;
	ListNode* next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
	ListNode* reverseList(ListNode* head) {
		ListNode* prev = nullptr;
		ListNode* curr = head;
		ListNode* next_node = nullptr;
		while (curr != nullptr) {
			next_node = curr->next;
			curr->next = prev;
			prev = curr;
			curr = next_node;
		}
		return prev;
	}
};

int main() {
	ListNode* head = new ListNode(0);
	ListNode* node1 = new ListNode(1);
	ListNode* node2 = new ListNode(2);
	ListNode* node3 = new ListNode(3);
	head->next = node1;
	node1->next = node2;
	node2->next = node3;
	Solution sol1;
	cout << sol1.reverseList(head)->val;
	return 0;
}