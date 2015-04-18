import pymarc

marc_file = open('hello_marc.dat', 'rb')  # make sure open as binary
reader = pymarc.MARCReader(marc_file, force_utf8=True)
print(next(reader))  # use next function

