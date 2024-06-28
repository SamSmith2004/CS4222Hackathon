import csv

def getData():
    # read csv file to a list of dictionaries
    with open('./data/cs4222_students_list.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
        
    return data