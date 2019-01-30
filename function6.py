import csv


def write_file(data):
    """
    Appends data to file: data

    :param data: @list
    """
    with open('match.csv', 'ab') as csvfile:
        wirrfile = csv.writer(csvfile,
                              quotechar=',', quoting=csv.QUOTE_MINIMAL)
        wirrfile.writerow(data)

    csvfile.close()


def clear_file():
    """
Purge all data on file
    """
    f = open('match.csv', 'w')
    f.close()
