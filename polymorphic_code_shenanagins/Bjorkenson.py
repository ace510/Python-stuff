import string
import itertools

search_space = string.printable


def exeggutor(input_thingy):
    results = ""
    try:
        results = exec(input_thingy)
    except (SyntaxError, NameError, AttributeError):
        # boring syntax stuff
        # boring undefined variables
        # Attribute error caused by i.a
        pass
    except TypeError:
        # print('god, did not expect that to happen')
        # this one was caused by calling 0(), the abominations happen
        pass
    except ZeroDivisionError:
        # print('no dividing by zero')
        # 1%0 is a nono
        pass
    except ValueError:
        # may god have mercy on my soul a,=()
        pass
    except IndexError:
        # captured 'km'[8] makes sense
        pass
    except SyntaxWarning:
        pass
    return results


def main():
    for i in range(72):
        permie = itertools.combinations_with_replacement(search_space, i)
        for objecti in permie:
            permie_string = "".join(objecti)
            output = exeggutor(permie_string)
            if output:
                print(output)
                _ = input('keep searching?')


if __name__ == "__main__":
    main()
