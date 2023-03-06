def write_to_file(file_name, s):
    f = open(file_name, "a")
    f.write(s+"\n")
    f.close()