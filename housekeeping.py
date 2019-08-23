import csv


def create_data_csv(project_name):
    csv_name = project_name + ".csv"
    with open(csv_name, "w"):
        pass


def set_csv_header(project_name, header):
    csv_name = project_name + ".csv"
    with open(csv_name, 'w', encoding='utf-8') as table:
        csv_writer = csv.writer(table, delimiter='\t')
        csv_writer.writerow(header)


def create_iterator_set(n):
    iterator_set = set(range(n))
    return iterator_set


