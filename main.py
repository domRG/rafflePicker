import secrets


def getDrawRange():
    inpStr = input("Enter draw range:\n(e.g. '3-219')\n")
    try:
        # confirm input in form 'X-Y', X & Y are integers, and X < Y
        assert '-' in inpStr
        minMax = list(map(int, inpStr.split('-')))
        assert minMax[0] < minMax[1]
    except:
        # if failed, try again by recursion (caution, endless loop)
        print(f"Error with input: '{inpStr}', please try again.")
        minMax = getDrawRange()
    return minMax


def getExcludes():
    inpStr = input("Enter numbers to exclude:\n(e.g. '53,74,158,211', or press Enter to skip)\n")
    try:
        # input list split and mapped to integers
        excludes = list(map(int, inpStr.split(',')))
    except:
        if inpStr == '':
            # catch no excludes
            excludes = []
        else:
            # otherwise, try again by recursion (caution, endless loop)
            print(f"Error with input: '{inpStr}', please try again.")
            excludes = getExcludes()
    return excludes


def getParams():
    drawRange = getDrawRange()
    excludes = getExcludes()

    # output to user for confirmation
    print(f"\nDraw Range: {'-'.join([str(x) for x in drawRange])}")
    print(f"Exclude: {str(excludes)[1:-1]}")

    print("\nIs this setup correct?")
    inpStr = ""
    yn = ["y", "n"]
    while not any(inpStr.casefold() == x for x in yn):
        # wait for correct input (case-insensitive) (caution, endless loop)
        inpStr = input("(y/n)\n")
        if inpStr.casefold() == yn[1]:
            # if params rejected, try again by recursion (caution, endless loop)
            drawRange, excludes = getParams()

    return drawRange, excludes


if __name__ == '__main__':
    drawRange, excludes = getParams()

    drawList = list(range(drawRange[0], drawRange[1]+1))
    for x in excludes:
        try:
            drawList.remove(x)
        except:
            print(f"Cannot exclude {x:3d} - not in range {'-'.join([str(x) for x in drawRange])}, or already removed")

    # TODO maybe change this to facilitate `input("How many results would you like?")` or
    #  'press enter for next result, press "x+enter" to exit'
    places = ["1st", "2nd", "3rd", "4th", "5th", "6th"]

    print("\n--- Results ---")
    for place in places:
        if len(drawList) == 0:
            # drawList is depleted
            break

        # select item from drawList
        sel = secrets.choice(drawList)
        # output
        print(f"{place} Place: {sel:4d}")
        # remove selected item from list (can't be chosen again)
        drawList.remove(sel)

    print('')
    print('Press {Enter} to exit')
    inp = input()
