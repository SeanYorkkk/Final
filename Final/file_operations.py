import csv

def save_to_file(data, filename):
    """Save data to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for key, values in data.items():
            writer.writerow([key] + values)

def load_from_file(filename):
    """Load data from a CSV file."""
    data = {}
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data[row[0]] = list(map(float, row[1:]))
    return data
