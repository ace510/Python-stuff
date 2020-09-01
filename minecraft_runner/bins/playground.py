import time
from input_handler import bounce_key_ween, release_key_ween, press_key_ween
from image_grabber import whole_screen_shot
import random
from pynput.mouse import Button, Controller
import string


def analyze_compass(results: tuple):
    results[1].save("../.pics/compass_output.jpg")
    result = results[0]
    """taking the raw value from the compass screen read and vectorizing it"""
    compass_dict = {
        "north": "north",
        "east": "east",
        "west": "west",
        "south": "south",
        "narth": "north",
        "@ast": "east",
        "nearth": "north",
        "nerth": "north",
        "marth": "north",
        "sauth": "south",
        "noarth": "north",
        "farth": "north",
        "gast": "east",
    }
    for key, value in compass_dict.items():
        if key in result:
            return value

    fixed_result = list()
    for i in result:
        if i not in ' "*/:<>?\|()[]':
            fixed_result.append(i)
    file_name = "".join(fixed_result)

    try:
        results[1].save(f"../.exemplars/{file_name}.jpg")
    except ValueError:
        with open("../.exemplars/bad_names.txt", "a") as a_file:
            a_file.write(f"the name: {file_name} has invalid characters \n")

    return random.choice(("north", "east", "west", "south"))


mouse = Controller()
output_set = set()

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

for i in range(5):
    press_key_ween("W")
    # results = screen_shot((5, 615, 860, 657)) # left, top, right, bottom
    whole_screen = whole_screen_shot()
    compass_results = whole_screen.crop((5, 615, 860, 657))

    heading = analyze_compass(compass_results)
    if heading in ("east", "south"):
        mouse.move(-20, 0)
    elif heading == "west":
        mouse.move(20, 0)
    elif heading == "north":
        turn = random.choice((-5, 5))
        mouse.move(turn, 0)

    release_key_ween("w")


with open("../.pics/output.txt", "w+") as file:
    for item in output_set:
        file.write(item)
        file.write("\n")
