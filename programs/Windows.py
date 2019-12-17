###################################################################################################
# Windows.py is a module for executing windows commands more easily

# Author : EpycZen ~ GitHub | StackOverFlow | Twitter | Instagram
# With fixes/improvements from :

###################################################################################################
import os
import subprocess


def pause():  # just a normal pause. displays "Press any key to continue . . ."
    os.system("pause")


def paus():  # this is also a pause but it doesn't display anything
    os.system("pause > nul")


def clear():  # clears the command prompt screen
    os.system("cls")


def color(str1):  # for selecting the color on the command prompt screen
    os.system("color " + str1)


def file_create(name, dbname, headings):  # creates an empty file in the current working directory
    cddir("data\\" + dbname)
    try:
        f = open(name, 'x')

    except FileExistsError:
        return -1

    with open(name, 'a') as f1:  # writes the heading (column name)
        f1.write(headings)


def folder_create(name):  # creates a folder in the current working directory
    cddir("data")
    try:
        os.mkdir(name)

    except FileExistsError:
        return -1


def cddir(name):  # changes the directory
    user_profile = subprocess.check_output("echo %USERPROFILE%", shell=True)  # to get the current username
    user_profile = user_profile.decode('utf-8')  # to decode it to str
    user_profile = user_profile.replace("\r\n", "")

    installation_directory = user_profile + "\\PycharmProjects\\CSQL"  # string containing the installation directory

    try:
        os.chdir(installation_directory)
        os.chdir(name)

    except FileNotFoundError:
        print("No such folder/file exists")
        return -1


def list_files(database_name):  # returns the files in a directory as a string
    if cddir("data\\" + database_name) == -1:
        return -1

    else:
        cddir("data\\" + database_name)
        result = subprocess.check_output("dir /b /a-d", shell=True)  # returns all the files in "data" folder
        return result


def list_directories():  # returns the directories as a string
    cddir("data")
    result = subprocess.check_output("dir /b/ ad", shell=True)  # returns all the directories inside a parent directory

    return result
