from .parse_function_declaration import parse_function_declaration
from .iterables import conditionals


def generate():
    print("Enter/Paste non-built-in Python function code. Type \" END \" or press Ctrl-D to save it.")
    contents = []
    while True:
        try:
            line = input()
            if line == "END":
                break
        except EOFError:
            break
        contents.append(line)


    line1 = parse_function_declaration(contents[0])
    contents.pop(0)
    result = conditionals(contents)

    print(line1)
    print(result)

def main():
    generate()
    return

if __name__ == "__main__":
    main()