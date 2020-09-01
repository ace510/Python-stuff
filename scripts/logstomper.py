log_file = "C:\\SQL.LOG"
log_condensed = "Condensed.log"
condenset = set()


def main():
    condenset_cycles = 0
    with open("C:\\SQL.LOG", "r") as in_file, open(log_condensed, "a") as logCondensed:
        try:
            for line in in_file:
                line_stripped = line.strip("\n")
                # print(line_stripped)
                condenset.add(line_stripped)

                if condenset.__len__() >= 1000:
                    for item in condenset:
                        logCondensed.write(item)

                    condenset.clear()
                    condenset_cycles += 1
                    print(condenset_cycles)
        except PermissionError:
            print("There was an error accessing the log")

        else:
            print("was successfull")


if __name__ == "__main__":
    main()
    while True:
        try:
            with open(log_file, "w") as clean_file:
                clean_file.write("all clean")
        except PermissionError:
            print("one hope this time")
