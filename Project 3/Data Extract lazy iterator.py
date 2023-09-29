from collections import namedtuple

def clean_data(file):
    with open(file) as f:
        for row in f:
            yield row.strip('\n').split(",")

def organize_data(file):
    yield from clean_data(file)

class Violations:
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        return organize_data(self.file)

def create_violations(file):
    car_violations = None
    for count, row in enumerate(Violations(file)):
        if count == 0:
            field_names = [field.strip().replace(' ', '_') for field in row]  # Clean and format field names
            car_violations = namedtuple("CarHistory", field_names)
        else:
            car = car_violations(*row)  # Create named tuple instance
            print(car)

if __name__ == "__main__":
    data_file = "nyc_parking_tickets_extract.csv"
    create_violations(data_file)
