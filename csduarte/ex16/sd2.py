from sys import argv

script, file_path = argv

f = open(file_path, 'r+')

print "Current File"
print "============"
print f.read()
print "============"

print "Adding a new line"
f.write("Extra Line\n")

f.close()
