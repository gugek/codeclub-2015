#!/usr/bin/python
"""
hello_marc.py

Opens a MARC file using pymarc and read in a single record
"""
import pymarc
import argparse


def main(arguments):
    marc_file = open(arguments.filename, 'rb')
    reader = pymarc.MARCReader(marc_file, force_utf8=True)
    record = next(reader)  # returns a record object
    if arguments.field:
        print(record[arguments.field])
    else:
        print(record)  # print the MARC-text representation of the record
    return record


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="MARC file to open")
    parser.add_argument("-f", "--field",
                        help="fieldname to print, must be a tagname")
    
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_arguments()
    main(args)