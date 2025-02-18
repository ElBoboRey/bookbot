def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)



def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        newbie = file_contents.split()
        return len(newbie)

def character_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        results = {}
        for char in file_contents.lower():
            if char not in results:
                results[char] = 1
            else:
                results[char] += 1
    return results

def report(dictionary):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count()} words found in the document\n")

    for key in dictionary:
        if key in "abcdefghijklmnopqrstuvwxyz":
            print(f"The '{key}' character was found {dictionary[key]} times")
    print("--- End report ---")



if __name__ == "__main__":
    main()
    character_count()
    report(character_count())