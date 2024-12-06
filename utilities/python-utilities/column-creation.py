import sys
import re

def parse_file(file_path):
    numerical_values = []

    with open(file_path, 'r') as file:
        for line in file:
            # Extract numerical values
            matches = re.findall(r'([-+]?\d*\.?\d+)', line)
            numerical_values.extend(matches)

    return numerical_values

def print_aligned_values(values):
    # Determine the width needed to align all values to the right
    width = max(len(value) for value in values) + 3  # Adding 3 for space and vertical separator

    print("=" * (width - 1) + "|")
    for idx, value in enumerate(values):
        if idx == 1 or idx == 5:
            print("=" * (width - 1) + "|")
        elif idx != 0:
            print("-" * (width - 1) + "|")
        print(f"{value:>{width-1}}|")
    print("=" * (width - 1) + "|")

def main():
    if len(sys.argv) != 2:
        print("Usage: python aligned_numerical_values_right.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        numerical_values = parse_file(file_path)
        print_aligned_values(numerical_values)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()

