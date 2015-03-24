#!/usr/bin/python
"""
hello_marc.py

Opens a MARC file using pymarc and read in a single record
"""
import pymarc
import argparse


def main(arguments):
    reader = pymarc.MARCReader(arguments.filename, force_utf8=True)
    record = reader.next()  # returns a record object
    print("Hello World!")
    print(record)  # print the MARC-text representation of the record
    return record


    # alternate reading using iteration
    """
    for record in reader:  # python idiom for looping through or iterating
        print(record)
    """

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="MARC file to open")
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_arguments()
    main(args)