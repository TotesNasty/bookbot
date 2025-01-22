char_count = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
}

def sort_on(item):
    return item[1] 

def sort():
    sorted_char_count = sorted(char_count.items(), key=sort_on, reverse=True)
    return sorted_char_count

def char_report(word_count, sorted_char_count):
    print("--- Character Count Report ---")
    print(f" There are {word_count} words in the text.")    
    print("  ")
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    print ("--- End of Report ---")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
 #       print(file_contents)
        lower_case_contents = file_contents.lower()
        word_count = len(file_contents.split())
        print(f"Word count: {word_count}")
        for letter in lower_case_contents:
            if letter in char_count:
                char_count[letter] += 1
        sorted_char_count = sort()
    char_report(word_count, sorted_char_count)
main()