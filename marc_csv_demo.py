"""
Extract data from a MARC file and output to CSV.

Use with Python 3. Unicode handling expected.
"""
import pymarc
import csv
import argparse
import sys


def main(arguments):
    csv_writer = make_csv_writer(arguments.output, arguments.fields)
    csv_writer.writeheader()
    for marc_file in arguments.marc_files:
        marc_reader = pymarc.MARCReader(marc_file)
        for record in marc_reader:
            row = {}  # create a dictionary row
            for fieldnames in make_fieldnames(arguments.fields,
                                              needcsv=False):
                fields = record.get_fields(*fieldnames)
                data = []
                for field in fields:
                    data.append(field.format_field())
                row["+".join(fieldnames)] = " | ".join(data)
            csv_writer.writerow(row)
    arguments.output.close()


def make_fieldnames(fields, needcsv=True):
    """Return fieldnames from the args, Some encapsulation here"""
    fieldnames = []
    for field_name in fields.split(','):
        # handle 001, 002, 003
        elements = []
        for element in field_name.strip().split('+'):
            elements.append(element.strip())
        fieldnames.append(elements)
    if needcsv:
        return ["+".join(field_name) for field_name in fieldnames]
    else:
        return fieldnames


def make_csv_writer(output, fields):
    """Returns a CSV DictWriter"""
    fieldnames = make_fieldnames(fields)
    csv_writer = csv.DictWriter(output, fieldnames=fieldnames)
    return csv_writer


def parse_arguments():
    parser = argparse.ArgumentParser()
    # MUST read MARC as binary
    parser.add_argument("marc_files", help="MARC file(s) to open", nargs="+",
                        type=argparse.FileType('rb'))
    parser.add_argument("-o", "--output", default=sys.stdout,
                        type=argparse.FileType('w'),
                        help="output file: default stdout")
    parser.add_argument("-f", "--fields",
                        help="fields to extract: comma and plus separated " +
                             "list, example: 100+110+111+130,245,250")
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_arguments()
    main(args)