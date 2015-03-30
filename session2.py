import pymarc
reader = pymarc.MARCReader(hello_marc.dat. force_utf8=True)
record = reader.next() # returns a record object
print (record.title())
