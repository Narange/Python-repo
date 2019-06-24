from random import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Given the head, print the linked list
def print_linked_list(head):
    if(head is None):
        return "List is empty"
    while(head is not None):
        print(head.val, end=" ")
        head = head.next


# Generate a singly-linked list with given length and random int elements. Return the head.
def generate_random_list(length):
    if(length <= 0):
        return None

    # length > 0, make the head
    head = ListNode(randint(1, 10))
    previous_node = head

    # continue creating nodes and set the prev node's "next" to this one
    for i in range(1, length):
        current_node = ListNode(randint(1, 10))
        previous_node.next = current_node
        previous_node = current_node

    return head


# Determine if a linked list's values are the same if traversed in reverse
def is_palindrome(head: ListNode) -> bool:
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


# Generate multiple lists of a certain length, determine how many of them were palindromes
def num_of_palindromes(length, num_of_lists):
    palindrome_count = 0

    for i in range(num_of_lists):
        current_list = generate_random_list(length)
        print_linked_list(current_list)
        print(is_palindrome(current_list))
        if is_palindrome(current_list):
            palindrome_count += 1

    print(f"{palindrome_count}/{num_of_lists} lists were palindromes")


num_of_palindromes(3, 1000)
