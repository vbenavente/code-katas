import linked_list


def matchmaker(string1, string2):
    """Return True or False based on proper closing of string2 characters."""
    sll = linked_list.LinkedList()
    string2 = string2[::-1]
    for char in string1:
        if char in string2:
            sll.push(char)
    current = sll.head
    try:
        if current.data in [')', ']', '}']:
            return False
        else:
            while current is not None:
                open_count = 0
                close_count = 0
                while current is not None:
                    if current.data in ['(', '[', '{']:
                        open_count += 1
                        current = current.next_node
                    elif current.data == [')', ']', '}']:
                        close_count += 1
                        current = current.next_node
                if open_count == close_count:
                    return True
                elif open_count > close_count:
                    return False
                return False
    except AttributeError:
        raise IndexError("List is empty.")
