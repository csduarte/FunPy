 # open(name[, mode[, buffering]])
 #
 #    Open a file, returning an object of the file type described in section File Objects. If the file cannot be opened, IOError is raised. When opening a file, it’s preferable to use open() instead of invoking the file constructor directly.
 #
 #    The first two arguments are the same as for stdio‘s fopen(): name is the file name to be opened, and mode is a string indicating how the file is to be opened.
 #
 #    The most commonly-used values of mode are 'r' for reading, 'w' for writing (truncating the file if it already exists), and 'a' for appending (which on some Unix systems means that all writes append to the end of the file regardless of the current seek position). If mode is omitted, it defaults to 'r'. The default is to use text mode, which may convert '\n' characters to a platform-specific representation on writing and back on reading. Thus, when opening a binary file, you should append 'b' to the mode value to open the file in binary mode, which will improve portability. (Appending 'b' is useful even on systems that don’t treat binary and text files differently, where it serves as documentation.) See below for more possible values of mode.
 #
 #    The optional buffering argument specifies the file’s desired buffer size: 0 means unbuffered, 1 means line buffered, any other positive value means use a buffer of (approximately) that size (in bytes). A negative buffering means to use the system default, which is usually line buffered for tty devices and fully buffered for other files. If omitted, the system default is used. [2]
 #
 #    Modes 'r+', 'w+' and 'a+' open the file for updating (reading and writing); note that 'w+' truncates the file. Append 'b' to the mode to open the file in binary mode, on systems that differentiate between binary and text files; on systems that don’t have this distinction, adding the 'b' has no effect.
 #
 #    In addition to the standard fopen() values mode may be 'U' or 'rU'. Python is usually built with universal newlines support; supplying 'U' opens the file as a text file, but lines may be terminated by any of the following: the Unix end-of-line convention '\n', the Macintosh convention '\r', or the Windows convention '\r\n'. All of these external representations are seen as '\n' by the Python program. If Python is built without universal newlines support a mode with 'U' is the same as normal text mode. Note that file objects so opened also have an attribute called newlines which has a value of None (if no newlines have yet been seen), '\n', '\r', '\r\n', or a tuple containing all the newline types seen.
 #
 #    Python enforces that the mode, after stripping 'U', begins with 'r', 'w' or 'a'.
 #
 #    Python provides many file handling modules including fileinput, os, os.path, tempfile, and shutil.
 #
