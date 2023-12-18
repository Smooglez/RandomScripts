#!/usr/bin/python3
import sys

def sortFile(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                words = line.strip().split()
                if len(words) >= 2:
                    letter1 = words[0][0]
                    letter2 = words[1][0]
                    print(f"{letter2}{words[0]}")
                    print(f"{words[0]}{letter2}")
                    print(f"{letter1}{words[1]}")
                    print(f"{words[1]}{letter1}")
                    print(f"{words[1]}{words[0]}")
                    print(f"{words[0]}{words[1]}")
                    print(f"{words[0]}")
                    print(f"{words[1]}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    sortFile(file_path)
