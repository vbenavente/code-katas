# -*- coding: utf-8 -*-
import linked_list


def proper_parenthetics(a_string):
    """Return broken(-1), balanced(0) or open(1) parenthesis for string."""
    sll = linked_list.LinkedList()
    a_string = a_string[::-1]
    for char in a_string:
        if char == ')' or char == '(':
            sll.push(char)
    current = sll.head
    try:
        if current.data == ')':
            return -1
        else:
            while current is not None:
                open_count = 0
                close_count = 0
                while current is not None:
                    if current.data == '(':
                        open_count += 1
                        current = current.next_node
                    elif current.data == ')':
                        close_count += 1
                        current = current.next_node
                if open_count == close_count:
                    return 0
                elif open_count > close_count:
                    return 1
                return -1
    except AttributeError:
        raise IndexError("List is empty.")
