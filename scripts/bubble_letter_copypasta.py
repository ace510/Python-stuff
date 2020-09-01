import string
import argparse

parser = argparse.ArgumentParser(description="generate funny Discord meme" "letters")
parser.add_argument(
    "copy_pasta",
    type=str,
    nargs="+",
    help="the string" " to be turned to emoji",
)

args = parser.parse_args()

copy_pasta = " ".join(args.copy_pasta)

output = []

for letter in copy_pasta:
    if letter.lower() in string.ascii_letters:
        output.append(f":regional_indicator_{letter.lower()}: ")

    monch = "ERROR"
    if letter == " ":
        monch = "<br/>"
    elif letter not in string.ascii_letters:
        monch = ""
    else:
        monch = f":regional_indicator_{letter.lower()}: "

    output.append(monch)

output_str = "".join(output)

print(output_str[:2000])
