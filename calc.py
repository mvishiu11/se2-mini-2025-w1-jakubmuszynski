import re


def calc(s: str) -> int:
    """
    A simple calculator function that:
      - Returns 0 if the input is an empty string.
      - Returns the integer value of a single number string.
      - Uses comma and newline as default delimiters.
      - Supports custom delimiter(s) defined at the beginning.
        * A single custom delimiter: e.g. "//;\n1;2"
        * Multiple custom delimiters: e.g. "//[*][%]\n1*2%3"
    """
    if s == "":
        return 0

    custom_delimiters = []
    if s.startswith("//"):
        if s[2] == "[":
            newline_index = s.find("\n")
            header = s[2:newline_index]
            custom_delimiters = re.findall(r'\[([^]]+)\]', header)
            s = s[newline_index+1:]
        else:
            custom_delimiters = [s[2:3]]
            s = s[3:]
            if s.startswith("\n"):
                s = s[1:]

    regex = r'\n|,'
    for delim in custom_delimiters:
        regex += f'|{re.escape(delim)}'

    parts = [part for part in re.split(regex, s) if part != ""]
    numbers = [int(n) for n in parts]

    if any(n < 0 for n in numbers):
        raise ValueError("Negatives not allowed")

    numbers = [n for n in numbers if n <= 1000]

    return sum(numbers)


if __name__ == "__main__":
    print(calc("//[*][%%]\n1*2%%3,4"))
