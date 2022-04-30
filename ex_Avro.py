import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("user.avsc", "rb").read())  # need to know the schema to write. According to 1.8.2 of Apache Avro

writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 8, "favorite_color": "red"})
writer.close()

#od -v -t x1z users.avro 

reader = DataFileReader(open("users.avro", "rb"), DatumReader())  # the schema is embedded in the data file
for user in reader:
    print user
reader.close()
