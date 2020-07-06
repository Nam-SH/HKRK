#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data), end=" ")

        node = node.next


# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    if not head:
        return head

    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.prev = nxt
        curr.next = prev
        prev = curr
        curr = nxt

    return prev

t = 1

for t_itr in range(t):
    llist_count = 4

    llist = DoublyLinkedList()

    data = [1, 2, 3, 4]
    for _ in range(llist_count):
        llist_item = data[_]
        llist.insert_node(llist_item)

    llist1 = reverse(llist.head)

    print_doubly_linked_list(llist1, ' ')