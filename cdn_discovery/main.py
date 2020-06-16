import guts

def main():
    with open('readme.md') as readme_file:
        for line in readme_file.readlines():
            print(line)


if __name__ == "__main__":
    main()