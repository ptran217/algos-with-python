from stack import Stack

def dec_to_bin(dec_num):
    rem_stack = Stack()

    while dec_num > 0:
        rem = dec_num % 2
        rem_stack.push(rem)
        dec_num = dec_num // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())

    return bin_string

print(dec_to_bin(16))