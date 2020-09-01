out_file = "output.log"
temp_file = "temp.log"
line_index = 0

with open("C:\\SQL.LOG", "r") as in_file:
    for line in in_file:
        if line_index <= 10:
            print(line)
            if input("is this line worth keeping?") == "y":
                with open(out_file) as outfile:
                    outfile.write(line)
            line_index += 1
        else:
            with open(temp_file, "a") as tempfile:
                tempfile.write(line)

with open(temp_file, "r") as tempfile, open("C:\\SQL.LOG", "w") as in_file:
    for line in tempfile:
        in_file.write(line)
