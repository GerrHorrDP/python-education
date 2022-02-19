"""This file contains solutions for exercise 14-16"""
import datetime
import time
import os
import sys
import part_one


def imported_functions():
    """solutions for 14 exercise
    printing sorted list of
    imported functions"""
    function_list = [x for x in dir(part_one)]
    print(sorted(function_list))


def date_time_info():
    """Show current date, time and timezone"""
    today = datetime.datetime.now()
    print(today.strftime("%d.%m.%Y %H:%M"))
    timezones = time.tzname
    print(f"My timezones are {timezones[0]} and {timezones[1]}")


def my_setup_ifo():
    """Shows information about system and python"""
    print(f"My name is {os.getlogin()} and i am on {os.name}")
    print(f"My platform is {sys.platform.upper()} and my python version is {sys.version}")


def read_write_file():
    """Reads and rewrites file hello.txt"""

    def write_file():
        """Writes wrong text in file hello.txt on purpose"""
        hello = open('/home/gerrhorr/PycharmProjects/python-education/basics/hello.txt', 'w')
        hello.write("Hello darkness, my old friend")

    write_file()  # can be commented

    file = open('/home/gerrhorr/PycharmProjects/python-education/basics/hello.txt')
    text = file.read()
    print(text)
    if text == "Hello, World!":
        file.close()
    else:
        print("\nHold on...that`s ain`t right!")
        file.close()
        file = open('/home/gerrhorr/PycharmProjects/python-education/basics/hello.txt', 'w')
        file.write('Hello, World!')
        file.close()
        file = open('/home/gerrhorr/PycharmProjects/python-education/basics/hello.txt')
        print(file.read())
        file.close()


# imported_functions()
# what_timezone_is_it()
# date_time_info()
# my_setup_ifo()
# read_write_file()
