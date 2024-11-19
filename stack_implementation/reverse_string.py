from stack import Stack

def rev_string(my_str):
    n = len(my_str)
    s = Stack()
    new_str = ''
    for i in range(n):
        s.push(my_str[i])

    while not s.is_empty():
        new_str += s.pop()
    return new_str

string = 'test1234'
print(rev_string(string))