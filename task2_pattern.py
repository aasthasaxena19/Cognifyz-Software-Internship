def print_pattern(rows):
    print("Number Pattern Program\n")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

try:
    rows = int(input("Enter number of rows: "))
    print_pattern(rows)
except ValueError:
    print("Please enter a valid number")
