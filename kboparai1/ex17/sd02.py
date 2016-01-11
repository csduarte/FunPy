from sys import argv
open(argv[2], 'w').write(open(argv[1]).read())
#http://stackoverflow.com/questions/11594100/how-can-i-further-shorten-this-python-script-which-copies-the-contents-of-one-fi