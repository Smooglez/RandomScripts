import sys

def generate_combinations(first_names, last_names, selected_combinations, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for first_name in first_names:
            for last_name in last_names:
                if '1' in selected_combinations:
                    output_file.write(first_name[0] + last_name + '\n')
                if '2' in selected_combinations:
                    output_file.write(first_name + last_name[0] + '\n')
                if '3' in selected_combinations:
                    output_file.write(first_name + last_name + '\n')
                if '4' in selected_combinations:
                    output_file.write(last_name + first_name + '\n')
                if '5' in selected_combinations:
                    output_file.write(first_name + '.' + last_name + '\n')
                if '6' in selected_combinations:
                    output_file.write(last_name + '.' + last_name + '\n')
                if '7' in selected_combinations:
                    output_file.write(first_name + '\n')
                if '8' in selected_combinations:
                    output_file.write(last_name + '\n')

def read_wordlist(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def get_selected_combinations():
    print("Select combinations to include (separate with commas):")
    print("1. First letter of first name + last name")
    print("2. First name + first letter of last name")
    print("3. First name + last name")
    print("4. Last name + first name")
    print("5. First name + period + last name")
    print("6. Last name + period + last name")
    print("7. First name")
    print("8. Last name")

    selected_combinations = input("Enter the combination numbers (e.g., 1,3,5): ")
    return selected_combinations.split(',')

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <first_names_file> <last_names_file> [output_file]")
        sys.exit(1)

    first_names = read_wordlist(sys.argv[1])
    last_names = read_wordlist(sys.argv[2])

    selected_combinations = get_selected_combinations()

    output_file_path = 'output_wordlist.txt' if len(sys.argv) < 4 else sys.argv[3]
    generate_combinations(first_names, last_names, selected_combinations, output_file_path)

if __name__ == "__main__":
    main()
