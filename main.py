def main():
    with open('books/frankenstein.txt') as f:
        file_content = f.read()
        return file_content


def count_words(file_content):
    words = file_content.split()
    return len(words)

def string_to_charactor_count(file_content):
    lowered_string = file_content.lower()
    character_count = {}
    for char in lowered_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(dict):
    return dict["count"]

def check_for_aphabet(char):
    if char.isalpha():
        return True
    else:
        return False

def final_character_list(character_count):
    character_list = []
    for char in character_count:
        if check_for_aphabet(char):
            character_list.append({"char": char, "count": character_count[char]})
    return character_list




file_content = main()
character_count = count_words(file_content)
character_list = string_to_charactor_count(file_content)
final_list = final_character_list(character_list)
final_list.sort(reverse=True, key=sort_on)
print("--- Begin report of books/frankenstein.txt ---")
print(f"{character_count} workds found in the document")
print("\n")
for char in final_list:
    print(f"The '{char['char']}' character was found {char['count']} times")


