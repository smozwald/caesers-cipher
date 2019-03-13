def cipher(string, offset = 3):
    print("go")
    """Input a string, cipher according to offset(default 3) and return)."""
    LOWER_MIN = 97
    UPPER_MIN = 65
    LOWER_MAX = 122
    UPPER_MAX = 90
    LOWER = list(range(LOWER_MIN, LOWER_MAX+1))
    UPPER = list(range(UPPER_MIN, UPPER_MAX+1))
    new_string = ""

    ##Check that we need to actually run this, and also make offset manageable.
    if len(string) == 0:
        return ""
    if offset > 25:
        while offset > 25:
            offset = offset - 26
    if offset < -25:
        while offset < -25:
            offset = offset + 26
    if offset == 0:
        return string


    for char in string:
        if ord(char) in LOWER:
            new_ord = ord(char) + offset
            if new_ord > LOWER_MAX:
                new_ord -= 26
            elif new_ord < LOWER_MIN:
                new_ord += 26
            new_string = new_string + (chr(new_ord))

        elif ord(char) in UPPER:
            new_ord = ord(char) + offset
            if new_ord > UPPER_MAX:
                new_ord -= 26
            elif new_ord < UPPER_MIN:
                new_ord += 26
            new_string = new_string + (chr(new_ord))
        else:
            new_string = new_string + char

    print(new_string)
    return new_string

