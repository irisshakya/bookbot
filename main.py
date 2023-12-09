

def main():
    path = 'books/frankenstein.txt'

    with open(path) as f:
        file_contents = f.read()


    str_counter = count_str(file_contents)
    get_dict = get_chars_dict(file_contents)
    char_sorted_list = chars_to_list(get_dict)

    print(f"--- Begin report of {path} ---")
    print(f"{str_counter} words found in the document")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def count_str(x):
    words = x.split()
    return len(words)

def get_chars_dict(tex):
    chars = {}
    for t in tex:
        lo = t.lower() 
        # add one 
        if lo in chars:
            chars[lo] += 1
        else:
            chars[lo] = 1
    return chars

def sort_on(d):
    return d['num']
# num_chars = {
#   'p' : 8796,
#    'o' : 7685
# }
def chars_to_list(num_chars):
    sorted_list = []

    for chr in num_chars:
        sorted_list.append({"char": chr, "num": num_chars[chr]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

if __name__ == '__main__':
    main()


