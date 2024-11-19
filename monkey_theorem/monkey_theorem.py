import random
import string

target_string = 'methinks it is like a weasel'

def create_random_string(target_string):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for x in range(len(target_string)))

def compare_string(new_string):
    matched_chars = 0
    for i in range(len(new_string)):
        if new_string[i] == target_string[i]:
            matched_chars += 1
    return matched_chars / len(new_string)

def change_one_char(new_string):
    result = list(new_string)
    result[random.randint(0,len(new_string) - 1)] = random.choice(string.ascii_lowercase + ' ')
    return "".join(result)

def generate_and_score():
    i = 0
    while i <= 1000:
        if i == 0:
            best_str = create_random_string(target_string)
            best_score = compare_string(best_str)
        else:
            new_str = change_one_char(best_str)
            new_score = compare_string(new_str)
            if new_score > best_score:
                best_str = new_str
                best_score = new_score
        print("Generated: %s Score: %3.2f"% (best_str, best_score * 100))
        if best_score == 1:
            print("Perfect Score!")
            break

        i += 1

generate_and_score()