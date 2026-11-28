
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL || head->next == NULL || k == 0)
            return head;

        ListNode* temp = head;
        int len = 1;

        while (temp->next != NULL) {
            temp = temp->next;
            len++;
        }

        temp->next = head;

        k = k % len;

        int steps = len - k;

        while (steps--) {
            temp = temp->next;
        }

        head = temp->next;
        temp->next = NULL;

        return head;
    }
};
