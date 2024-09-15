import sys
import locale

def byte_count(file_name):
    try:
        with open(file_name, 'rb') as file:
            content = file.read()
        print(f"{len(content)} {file_name}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

def line_count(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        print(f"{len(lines)} {file_name}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

def word_count(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
        print(f"{len(words)} {file_name}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

def char_count(file_name):
    try:
        with open(file_name, 'r', encoding=locale.getpreferredencoding()) as file:
            content = file.read()
        print(f"{len(content)} {file_name}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

def default_count(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            lines = content.splitlines()
            words = content.split()
            bytes_size = len(content.encode('utf-8'))
        print(f"{len(lines)} {len(words)} {bytes_size} {file_name}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

def default_count_from_input():
    content = sys.stdin.read()
    lines = content.splitlines()
    words = content.split()
    bytes_size = len(content.encode('utf-8'))
    print(f"{len(lines)} {len(words)} {bytes_size}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        default_count(sys.argv[1])
    elif len(sys.argv) == 1:
        default_count_from_input()
    elif len(sys.argv) == 3:
        option = sys.argv[1]
        file_name = sys.argv[2]
        if option.startswith('-') and not file_name.startswith('-'):
            if option == '-c':
                byte_count(file_name)
            elif option == '-l':
                line_count(file_name)
            elif option == '-w':
                word_count(file_name)
            elif option == '-m':
                char_count(file_name)
            else:
                print(f"Error: Invalid option '{option}'. Use -c, -l, -w, or -m.")
        else:
            print("  python3 ccwc.py <file>")
            print("  python3 ccwc.py -[c|l|w|m] <file>")
