# python3
from os.path import exists

def read_input():
    type = input()
    if "I" in type:
        patt = input()
        search = input()
    else:
        print(type)

    #print("Pattern:"+patt)
    #print("Search:"+search)
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (patt.rstrip(), search.rstrip())
    return ("","")

def print_occurrences(output):
    # this function should control output, it doesn't need any return
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
            
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return indexes


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

