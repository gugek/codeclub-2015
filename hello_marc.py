#!/usr/bin/python
"""
hello_marc.py

Opens a MARC file using pymarc and read in a single record
"""
import pymarc
import argparse
import pprint


def main():
    marc_file = open('hello_marc.dat', 'rb')
    reader = pymarc.MARCReader(marc_file, force_utf8=True)
    # record = next(reader)  # returns a record object
    for record in reader:
        print(type(record))
        print(type(record.fields))
        print(record.leader)
        # print(record)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="MARC file to open")
    parser.add_argument("-f", "--field", help="fieldname to print")
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    main()