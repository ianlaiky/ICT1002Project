
import csv

# def write_file(header,data):
#     """
#     Appends data to file: Header & data
#     :param header: @list
#     :param data: @list
#     """
#     with open('match.csv', 'a') as csvfile:
#         wirrfile = csv.writer(csvfile)
#         wirrfile.writerow(header)
#         wirrfile.writerow(data)
#
#     csvfile.close()


def write_file(data):
    """
    Appends data to file: data

    :param data: @list
    """
    with open('match.csv', 'ab') as csvfile:
        wirrfile = csv.writer(csvfile)
        wirrfile.writerow(data)

    csvfile.close()

def clear_file():
    """
Purge all data on file
    """
    f = open('match.csv', 'w')
    f.close()

