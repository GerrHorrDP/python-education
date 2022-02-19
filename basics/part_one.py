"""This module contains solutions for 1-12 exercises"""


def hello_world():

    """solutions for 1 exercise
    printing 'Hello, World!'"""
    print("Hello, World!")


def variables_and_types():

    """solutions for 2 exercise
    checking types"""
    my_string = "hello"
    my_float = 10.0
    my_int = 20

    if my_string == "hello":
        print("String: %s" % my_string)
    if isinstance(my_float, float) and my_float == 10.0:
        print("Float: %f" % my_float)
    if isinstance(my_int, int) and my_int == 20:
        print("Integer: %d" % my_int)


def lists():
    """solutions for 3 exercise
    appending lists"""
    numbers = []
    strings = []
    names = ["John", "Eric", "Jessica"]

    second_name = names[1]
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    strings.append('hello')
    strings.append('world')

    print(numbers)
    print(strings)
    print("The second name on the names list is %s" % second_name)


def basic_operators():
    """solutions for 4 exercise
    using operators with lists"""
    x = object()
    y = object()

    x_list = ([x] * 10)
    y_list = ([y] * 10)
    big_list = x_list + y_list

    print("x_list contains %d objects" % len(x_list))
    print("y_list contains %d objects" % len(y_list))
    print("big_list contains %d objects" % len(big_list))

    # testing code
    if x_list.count(x) == 10 and y_list.count(y) == 10:
        print("Almost there...")
    if big_list.count(x) == 10 and big_list.count(y) == 10:
        print("Great!")


def string_formatting():
    """solutions for 5 exercise
    formatting strings"""
    data = ("John", "Doe", 53.44)
    print(f"Hello {data[0]} {data[1]}. Your current balance is ${data[2]}.")


def basic_string_operations():
    """solutions for 6 exercise
    string operations"""

    s = "Hey there! what should this string be?"
    # Length should be 20
    s = s[:20]
    print("Length of s = %d" % len(s))

    # First occurrence of "a" should be at index 8
    s = s[:8] + "a" + s[8:]
    print("The first occurrence of the letter a = %d" % s.index("a"))

    # Number of a's should be 2
    print("a occurs %d times" % s.count("a"))

    # Slicing the string into bits
    print("The first five characters are '%s'" % s[:5])  # Start to 5
    print("The next five characters are '%s'" % s[5:10])  # 5 to 10
    print("The thirteenth character is '%s'" % s[12])  # Just number 12
    print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing)
    print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

    # Convert everything to uppercase
    print("String in uppercase: %s" % s.upper())

    # Convert everything to lowercase
    print("String in lowercase: %s" % s.lower())

    # Check how a string starts
    if s.startswith("Hey"):
        print("String starts with 'Hey'. Good!")

    # Check how a string ends
    if s.endswith("hou!"):
        print("String ends with 'hou!'. Good!")

    # Split the string into three separate strings,
    # each containing only a word
    hey_list = s.split(" ")
    hey_list.pop()
    print("Split the words of the string: %s" % hey_list)


def conditions():
    """solutions for 7 exercise
    conditions operations"""
    number = 16
    second_number = 0
    first_array = [1, 2, 3]
    second_array = [1, 2]

    if number > 15:
        print("1")

    if first_array:
        print("2")

    if len(second_array) == 2:
        print("3")

    if len(first_array) + len(second_array) == 5:
        print("4")

    if first_array and first_array[0] == 1:
        print("5")

    if not second_number:
        print("6")


def loops():
    """solutions for 8 exercise
    loop exercise with break"""
    numbers = [
        951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
        615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
        743, 527
    ]

    for x in numbers:
        if not x % 2 == 0:
            print(x)
        elif x == 237:
            break


def functions():
    """solutions for 9 exercise
    how to use functions"""

    def list_benefits():
        return [
            "More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together"
        ]

    def build_sentence(benefit):
        return benefit + " is a benefit of functions!"

    def name_the_benefits_of_functions():
        list_of_benefits = list_benefits()
        for benefit in list_of_benefits:
            print(build_sentence(benefit))

    name_the_benefits_of_functions()


def docstrings():
    """solutions for 10 exercise
    it`s about docstrings
    seems like I did it"""
    print(docstrings.__doc__)


def dictionaries():
    """solutions for 11 exercise
    adding and removing from dict"""
    phonebook = {
        "John": 938477566,
        "Jack": 938377264,
        "Jill": 947662781
    }
    phonebook["Jake"] = 938273443
    phonebook.pop("Jill")

    if "Jake" in phonebook:
        print("Jake is listed in the phonebook.")

    if "Jill" not in phonebook:
        print("Jill is not listed in the phonebook.")


def sets():
    """solutions for 12 exercise
    printing set of difference
    between two lists"""
    a = ["Jake", "John", "Eric"]
    b = ["John", "Jill"]
    print((set(a)).difference(set(b)))


# hello_world()
# string_formatting()
# basic_operators()
# basic_string_operations()
# conditions()
# loops()
# functions()
# docstrings()
# dictionaries()
# sets()
