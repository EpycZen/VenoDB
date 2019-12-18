###################################################################################################
# Windows.py is a module for executing windows commands for VenoDB

# Author : EpycZen ~ GitHub | StackOverFlow | Twitter | Instagram
# With fixes/improvements from :

###################################################################################################
import os
import subprocess

installation_dir = ""


def clear():  # clears the command prompt screen
    os.system("cls")


def installation_directory():  # to set the installation directory from a file
    try:
        os.chdir("programs")
        print(subprocess.check_output("dir", shell=True))
        f = open("INSTALLATION_DIRECTORY.txt", "r")
        lines = f.readlines()
        for line in lines:
            if "installation_dir" in line:
                startq = line.find("`") + 1

                endq = line.find("\'")

                global installation_dir
                installation_dir += line[startq:endq]
                break

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
        headings += "\n"
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
        try:
            result = subprocess.check_output("dir /b /a-d", shell=True)  # returns all the files in "data" folder
            return str(result.decode('utf-8'))

        except subprocess.CalledProcessError:
            return -1


def list_directories():  # returns the directories as a string
    cddir("data")
    result = subprocess.check_output("dir /b/ ad", shell=True)  # returns all the directories inside a parent directory

    return str(result.decode('utf-8'))


def init():
    installation_directory()
    print(installation_dir)
    try:
        os.chdir(installation_dir)

    except OSError:
        print("Please check INSTALLATION_DIRECTORY.txt")
        pause()
        exit()

    folders = ["data", "log", "programs"]
    files_in_programs = ["VenoDBv1.py", "Windows.py", "INSTALLATION_DIRECTORY.txt"]

    folder_list = str(subprocess.check_output("dir /b /ad", shell=True).decode('utf-8'))

    os.chdir(installation_dir + "\\programs")
    file_list = str(subprocess.check_output("dir /b /a-d", shell=True).decode('utf-8'))

    for folder in folders:
        if folder not in folder_list:
            os.chdir(installation_dir)
            os.mkdir(folder)

    p = 0
    for file in files_in_programs:
        if file in file_list:
            p += 1
        
        else:
            p = 0

    if p == 3:
        return True
