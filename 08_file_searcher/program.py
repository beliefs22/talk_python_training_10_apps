import os
from collections import namedtuple

Search_Result = namedtuple("Search_Result", "file line_num text")


def main():
    print_header()
    folder = get_folder_from_user()
    if folder:
        if folder == "quit":
            print("Good Bye")
            return
        search_text = get_search_text_from_user()
        results = search_folder(folder, search_text)
        for result in results:
            print("--------------Match")
            print(result.file)
            print(result.line_num)
            print(result.text.strip())


def print_header():
    print("----------------------------")
    print("               File Searcher")
    print("----------------------------")


def get_folder_from_user():
    folder = input("What folder would you like to search[leave empty to quit]? ")
    if folder.strip() == "":
        print("quitting")
        return "quit"
    elif not os.path.isdir(folder):
        print(os.getcwd())
        print("Sorry that is not a directory")
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    search_text = input("What word would you like to search for? ")
    if not search_text:
        return None

    return search_text.lower()


def search_file(full_item, search_text):
    with open(full_item, 'r', encoding='utf-8') as fin:
        for line_num, line in enumerate(fin):
            if line.lower().find(search_text) != -1:
                match = Search_Result(full_item, line_num, line)
                yield match


def search_folder(folder, search_text):

    current_files = os.listdir(folder)

    for item in current_files:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folder(full_item)

        else:
            yield from search_file(full_item, search_text)


if __name__ == '__main__':
    main()