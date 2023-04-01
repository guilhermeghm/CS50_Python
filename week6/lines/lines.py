import sys
import ast

def count_lines(filename):

    with open(filename, 'r') as f:
        code = f.read()

    tree = ast.parse(code)
    lines = code.split('\n')

    line_numbers = set()
    for node in ast.walk(tree):
        if hasattr(node, 'lineno'):
            line_numbers.add(node.lineno)

    for i, line in enumerate(lines):
        if i+1 not in line_numbers and not line.strip().startswith('#') and line.strip():
            line_numbers.add(i+1)

    return len(line_numbers)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    if not filename.endswith('.py'):
        sys.exit("Not a Python file")

    try:
        with open(filename):
            pass
    except FileNotFoundError:
        sys.exit("File does not exist")

    num_lines = count_lines(filename)
    print(num_lines)
