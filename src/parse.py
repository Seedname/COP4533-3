import pathlib


def read_input(file_name: str) -> tuple[int, dict[str, int], str, str]:
    """Reads input file and returns the parsed contents

    Args:
        file_name: File name (without path or .in)

    Returns:
        A tuple with the number of characters, a map of the characters to their values, A, and B

    Raises:
        ValueError: Raises an exception when the input file is invalid
    """

    parent_dir = pathlib.Path(__file__).parent
    input_directory = parent_dir.parent / "inputs"

    input_file = input_directory / f"{file_name}.in"

    if not input_file.exists():
        raise ValueError(f"Input file {file_name}.in does not exist")

    with open(input_file) as f:
        # read the lines of the input file
        lines: list[str] = f.readlines()

    # remove whitespace and empty lines
    lines = [line.strip() for line in lines if line.strip()]

    # checks that the file isn't empty
    if len(lines) == 0:
        raise ValueError("Empty file")
    
    # check that the first line contains a single number
    num_characters: str = lines[0]

    if not num_characters.isdigit():
        raise ValueError("First line must be the number of characters in the alphabet")
    
    # convert it to an integer
    num_characters: int = int(num_characters)

    # check that there are 1 + num_characters + 2 rows
    if len(lines) != num_characters + 3:
        raise ValueError("invalid number of rows")
    
    # check that the next num_characters lines are in the proper format (xi vi)
    if not all(len(lines[i].split(" ")) == 2 for i in range(1, num_characters+1)):
        raise ValueError("Character map in improper format")

    character_map: list[tuple[str, str]] = [lines[i].split(" ") for i in range(1, num_characters+1)]

    # make sure that the first character in the map is a letter and the second is a number
    if not all(x.isalpha() and len(x) == 1 and v.isdigit() for x, v in character_map):
        raise ValueError("Character map in improper format")
    
    character_map: dict[str, int] = {x: int(v) for x, v in character_map}

    # check if the A, B strings contain only letters
    A = lines[-2]
    B = lines[-1]

    if not A.isalpha() or not B.isalpha():
        raise ValueError("A or B not alphabetic strings")

    return num_characters, character_map, A, B


def read_output(file_name: str) -> tuple[int, str]:
    """Reads output file and returns the parsed contents

    Args:
        file_name: File name (without path or .out)

    Returns:
        A tuple with the highest value, and the optimal subsequence

    Raises:
        ValueError: Raises an exception when the output file is invalid
    """

    parent_dir = pathlib.Path(__file__).parent
    output_directory = parent_dir.parent / "outputs"

    output_file = output_directory / f"{file_name}.out"

    if not output_file.exists():
        raise ValueError(f"Output file {file_name}.output does not exist")

    with open(output_file, 'r') as f:
        lines = f.readlines()

    # remove whitespace and empty lines
    lines: list[str] = [line.strip() for line in lines if line.strip()]

    # make sure that theres 2 lines
    if len(lines) != 2:
        raise ValueError("Invalid output format")

    # make sure that the first line is an integer
    value: str = lines[0]

    if not value.isdigit():
        raise ValueError("First line is not an integer")
    
    value: int = int(value)

    # make sure the output is a character string
    string: str = lines[1]

    if not string.isalpha():
        raise ValueError("Second line not alphabetic")
    
    # return value and string
    return value, string


def write_output(file_name: str, value: int, string: str) -> str:
    """Write output to a file

    Args:
        file_name: File name (without path or .out)

    Returns:
        The outputted string
    """

    parent_dir = pathlib.Path(__file__).parent
    output_directory = parent_dir.parent / "outputs"

    output_file = output_directory / f"{file_name}.out"

    # construct the output string
    output_string = f"{value}\n{string}"

    with open(output_file, 'w') as f:
        f.write(output_string)

    return output_string


if __name__ == "__main__":
    # testing reading files
    file_name = "file1"

    k, character_map, A, B = read_input(file_name)
    print(f"{k = }")
    print(f"{character_map = }")
    print(f"{A = }")
    print(f"{B = }")

    print()

    value, string = read_output(file_name)
    print(f"{value = }")
    print(f"{string = }")

    # print()

    # result = write_output("file1", value, string)
    # print(result)
