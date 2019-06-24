# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head):
    if(head is None):
        return "List is empty"
    while(head is not None):
        print(head.val, end=" ")
        head = head.next


def isPalindrome(head: ListNode) -> bool:
    new_list = []
    original_head = head

    while(head is not None):
        new_list.append(head.val)
        head = head.next

    list_index = len(new_list) - 1
    head = original_head
    while(head is not None):
        if(head.val != new_list[list_index]):
            return False
        head = head.next
        list_index -= 1

    return True


node1 = ListNode(8)

node2 = ListNode(4)
node1.next = node2

node3 = ListNode(8)
node2.next = node3

print_list(node1)
print(isPalindrome(node1))
