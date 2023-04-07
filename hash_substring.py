def read_input():
    type = input()
    if "I" in type:
        patt = input()
        search = input()
    else:
        file = "tests/06"
        with open(file, 'r', encoding="utf-8") as f:
            patt = f.readline()
            search = f.readline()
    return (patt.rstrip(), search.rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    indexes = []
    for i in range(len(text)):
        if text[i] == pattern[0] and len(pattern) + i <= len(text):
            found = True
            for j in range(len(pattern)):
                if text[i+j] != pattern[j]:
                    found = False
            if found:
                indexes.append(i)
    return indexes

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

