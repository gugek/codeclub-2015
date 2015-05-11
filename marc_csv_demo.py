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
    record_numbers = {}
    for marc_file in arguments.marc_files:
        marc_reader = pymarc.MARCReader(marc_file)
        for record in marc_reader:
            record_number = record['001'].value()
            if record_number in record_numbers:
                continue
            else:
                record_numbers[record_number] = 'SEEN'
            row = {}  # create a dictionary row
            for fieldnames in make_fieldnames(arguments.fields,
                                              needcsv=False):
                # >>> fieldnames
                # ['260', '264']
                fields = record.get_fields(*fieldnames)
                data = []
                for field in fields:
                    # 650 10 $a Contracts $z United States
                    data.append(field.format_field())
                key = "+".join(fieldnames)  # this matches to the header of CSV
                output_values = " | ".join(data)  # this goes into the CSV cell
                row[key] = output_values

            csv_writer.writerow(row)
        """
        rows = [
            {'field1': 'a', 'field2': 123},
            {'field2': 'b', 'field3': 400}
        ]
        csv_writer.writerows(rows)

        field1,field2
        a,123
        b,400

        field1  field
        a   123
        b   400
        """


    arguments.output.close()  # closing the file to make sure all data written


def make_fieldnames(fields, needcsv=True):
    """Return fieldnames from the args, Some encapsulation here

    fields = "245,260+264,650"
    >>> fieldnames
    ['245', '260', '264', '650']
    """
    fieldnames = []
    for field_name in fields.split(','):
        # ['245', '260+264', '650']
        #
        # handle 001, 002, 003
        elements = []
        for element in field_name.strip().split('+'):
            elements.append(element.strip())
        fieldnames.append(elements)
    if needcsv:
        # for headers need to return: ['245', '260+264', '650']
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
                        type=argparse.FileType('w', encoding="cp1252"),
                        help="output file: default stdout")
    parser.add_argument("-f", "--fields",
                        help="fields to extract: comma and plus separated " +
                             "list, example: 100+110+111+130,245,250")
    arguments = parser.parse_args()
    print(arguments)
    return arguments


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
