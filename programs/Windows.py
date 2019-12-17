###################################################################################################
# Windows.py is a module for executing windows commands for VenoDB

# Author : EpycZen ~ GitHub | StackOverFlow | Twitter | Instagram
# With fixes/improvements from :

###################################################################################################
import os
import subprocess

installation_dir = ""


def pause():  # just a normal pause. displays "Press any key to continue . . ."
    os.system("pause")


def paus():  # this is also a pause but it doesn't display anything
    os.system("pause > nul")


def clear():  # clears the command prompt screen
    os.system("cls")


def color(str1):  # for selecting the color on the command prompt screen
    os.system("color " + str1)


def installation_directory():  # to set the installation directory from a file
    try:
        f = open("INSTALLATION_DIRECTORY.txt", "r")
        lines = f.readlines()
        for line in lines:
            if "installation_dir" in line:
                startq = line.find("`") + 1

                endq = line.find("\'")

                global installation_dir
                installation_dir += line[startq:endq]

    except FileNotFoundError:
        print("[Error: IDNF] INSTALLATION_DIRECTORY.txt not found. Refer documentation for more help")
        return


def file_create(name, dbname, headings):  # creates an empty file in the current working directory
    cddir("data\\" + dbname)
    try:
        f = open(name, 'x')

    except FileExistsError:
        return -1

    with open(name, 'a') as f1:  # writes the heading (column name)
        f1.write(headings)


def folder_check(database_name):
    if database_name in list_directories():
        return False
    else:
        return True


def folder_create(name):  # creates a folder in the current working directory
    cddir("data")
    try:
        os.mkdir(name)

    except FileExistsError:
        return -1


def cddir(name):  # changes the directory
    os.chdir(installation_dir)  # to switch to the installation directory

    try:  # try switching to the given directory
        os.chdir(name)

    except FileNotFoundError:  # if the directory is not found
        print("No such folder/file exists")
        return -1


def list_files(database_name):  # returns the files in a directory as a string
    if cddir("data\\" + database_name) == -1:
        return -1

    else:
        result = subprocess.check_output("dir /b /a-d", shell=True)  # returns all the files in "data" folder
        return str(result.decode('utf-8'))


def list_directories():  # returns the directories as a string
    cddir("data")
    result = subprocess.check_output("dir /b/ ad", shell=True)  # returns all the directories inside a parent directory

    return str(result.decode('utf-8'))
