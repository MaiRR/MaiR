from random import random

# Returns the contents of the file with name `file`
def read_file(file):
    with open(file) as f:
        return f.read()

# Parse a CSV row with contents `csv_row`
def parse_csv_row(csv_row):
    row = []
    cell = ''
    in_quotes = False
    for i in csv_row:
        if i == '"':
            in_quotes = not in_quotes
        elif i == ',' and not in_quotes:
            row.append(cell)
            cell = ''
        else:
            cell += i
    row.append(cell)
    return row

# Adds the csv row `row` into `weights`
# using entry 1 as a weight and entry 0 as a value
def add_weight(weights, row):
    weights[row[0]] = float(row[1])

# Has an `n` chance of returning True, where `n` is a float
def chance(n):
    return random() < n

# Converts `csv` to a weighted list
def csv_to_weighted_list(csv):
    # First strip all whitespace then split to get the lines
    lines = csv.strip().split('\n')
    # Remove the first and last lines,
    # which are a header and total, respectively
    lines = lines[1:-1]
    weights = {}
    for line in lines:
        row = parse_csv_row(line)
        add_weight(weights, row)
    return weights

# Returns a value of `weights`
# using its corresponding key as a percentage
def weighted_choice(weights):
    remaining_weight = 100
    for val in weights:
        weight = weights[val]
        if chance(weight / remaining_weight):
            return val
        else:
            remaining_weight -= weight
    return None # If percentages don't add up to 100

# Read 'occupations.csv' and return an occupation based on its weight
def main():
    occupations = read_file('occupations.csv')
    weighted_list = csv_to_weighted_list(occupations)
    print(weighted_choice(weighted_list))

if __name__ == "__main__":
    main()

