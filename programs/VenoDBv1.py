###################################################################################################
# A Python based CSV DBMS
# Copyright (C) 2019 EpycZen
# https://github.com/EpycZen/VenoDB

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

###################################################################################################
# VenoDBv1.py is a python-based DBMS.
# Project is in development stage.
# Has basic DBMS functionalities with some features.
# Here, a table is referred as a file(.csv file).
# a database is a folder which contains the files
# Support for linux will be made with slight changes to the code
# support commands to query the database
# A GUI version may come in version 3(probably)
# Some security and concept of users will be implemented in version 2
# Network access will also be introduced in version 2. Still searching for fancy port number :)
# 50% of profits will be donated for planting tress :) [if i get any]

# Creator : EpycZen ~ GitHub | StackOverFlow | Twitter
# With fixes/improvements from (add GitHub Username):
#
###################################################################################################

# Importing required libraries/modules
import csv
import sys
from datetime import datetime
from Windows import *


# WORKS
def current_time():
    time_now_1 = datetime.now()  # to get the current time. format : YYYY-MM-DD HH:MM:SS.MSMSMS
    time_now_2 = str(time_now_1)  # to convert the datetime into str for removing date and milliseconds
    current_time_now = time_now_2[11:19]  # to slice the string to get the final HH:MM:SS

    return current_time_now  # return that value


# WORKS
def current_date():
    current_date_now = datetime.now()  # to get the current time. format : YYYY-MM-DD HH:MM:SS.MSMSMS
    current_date_now = str(current_date_now)  # to convert it into a string for slicing
    current_date_now = current_date_now[0:10]  # to slice the date in YYYY-MM-DD format

    return current_date_now  # return that value


# WORKS
def log_activity(activity):  # to log activity to a file. New file for each day.
    cddir("log")
    name_of_log_file = "log" + current_date() + ".log"
    log_file = open(name_of_log_file, "a")
    log_line = current_time() + ": " + activity
    print(log_line, file=log_file)
    log_file.close()


# WORKS
def create_folder(database_name):
    if folder_check(database_name):
        folder_create(database_name)
        print(database_name, "created")
        log1 = "Database " + database_name + " created"

    else:
        print("Database " + database_name + " already exists")
        log1 = "Failed to create database " + database_name + " : Already exists"

    log_activity(log1)


# WORKS
def create_file(file_name, database_name, headings):  # to create a file
    direc = "data\\" + database_name
    cddir(direc)
    file_name += ".csv"

    headings_final = headings.replace("(", "").replace(")", "")

    file_create(file_name, database_name, headings_final)
    print(file_name, "created in", database_name)
    log1 = "File " + file_name + " created in " + database_name
    log_activity(log1)


# WORKS
def show(comm_list):  # to show all the records in a file
    database_name = comm_list[-1]
    file_name = comm_list[-2] + ".csv"
    cddir("data\\" + database_name)
    csv.register_dialect('myDialect', skipinitialspace=True)

    try:
        with open(file_name, "r", newline='') as src:
            rdr = csv.reader(src, dialect='myDialect')
            lines = list(rdr)

        if len(lines) == 0:
            print("No rows exist")
            return

        else:
            q = -1
            for row in lines:
                if str(row) != "[]":
                    i = 1
                    for element in row:
                        if i < len(row):
                            print(element, end=', ')
                            i += 1

                        else:
                            print(element)

                    q += 1

            print(q, "row(s) in file")

    except FileNotFoundError:
        print("No such file " + file_name + " exists")

    log1 = "Show all records in " + file_name + "\\" + database_name
    log_activity(log1)


# WORKS
def replace_record(comm_list, cmd):  # to replace values in a row
    # replace [old values] [new values] file_name database_name
    database_name = comm_list[-1]
    file_name = comm_list[-2] + ".csv"
    cddir("data\\" + database_name)

    old_start = 8
    new_thing = ""
    new_start = 0

    old_end = cmd.find("]")
    old_values = list(cmd[old_start:old_end+1].replace("[", "").replace("]", "").replace(", ", ",").split(","))

    new_thing += cmd[:old_end+1].replace("]", "*") + cmd[old_end+1:]

    new_start += old_end + 2
    new_end = new_thing.find("]")
    new_values = list(cmd[new_start:new_end+1].replace("[", "").replace("]", "").replace(", ", ",").split(","))

    csv.register_dialect('myDialect', skipinitialspace=True)

    try:
        with open(file_name, "r", newline='') as src:
            rdr = csv.reader(src, dialect='myDialect')
            lines = list(rdr)

        for key, row in enumerate(lines):
            if row == old_values:
                lines.pop(key)
                lines.insert(key, new_values)

        res = open(file_name, "w", newline='')
        wtr = csv.writer(res, dialect='myDialect')
        wtr.writerows(lines)

        res.close()

        ch = str(old_values).replace("\'", "") + " replaced with " + str(new_values).replace("\'", "") + " in "
        ch += file_name + "\\" + database_name
        print(ch)
        log_activity(ch)

    except FileNotFoundError:
        print("No such file " + file_name + " exists")
        return


# WORKS
def list_db_files(cmd, comm):  # to list the databases/the files inside them
    database_name = cmd[-1]

    if "files" == comm[5:10]:
        log1 = "List files in " + database_name
        ch = list_files(database_name)
        if ch != -1:
            list_file = list_files(database_name)

            file_list = list(list_file.replace("\r", "").replace(".csv", "").split("\n"))
            file_list.pop(-1)

            print("Files in " + database_name + " :")
            print(*file_list, sep='\n')
            print(len(file_list), "file(s)")

        elif ch == -1:
            print("0 file(s)")

    else:
        log1 = "List databases"
        list_database = list_directories()

        database_list = list(list_database.replace("\r", "").split("\n"))
        database_list.pop(-1)

        print("Databases :")
        if len(database_list) == 0:
            print("0 database(s)")
        
        else:
            print(*database_list, sep='\n')

    log_activity(log1)


# WORKS
def insert(cmd1, cmd):  # to insert values into a file
    ###################################################################################################
    # Syntax:
    # insert [values] table_name db_name
    # Example:
    # insert [100, 'John Doe'] employee office
    # the values must be given in a list and strings must be enclosed within quotes 
    ###################################################################################################
    # insert a row to the file and save it

    database_name = str(cmd1[-1])
    file_name = database_name + "\\" + str(cmd1[-2]) + ".csv"

    values = cmd[cmd.find("[") + 1:cmd.find("]")]

    values_list = values.strip("][").split(",")  # to convert string representation of list to list
 
    cddir("data")
    if os.path.isfile(file_name):
        fle = open(file_name, 'a', newline='')  # open the file
        fl = csv.writer(fle)  # create an instance
        fl.writerow(values_list)  # and insert(append) the values_list
        fle.close()  # close the file
        print(values, "inserted into", file_name)
        log1 = "Values " + values + " inserted into " + file_name

    else:
        print(file_name , "does not exist")
        log1 = file_name + " insertion failed"

    log_activity(log1)  # write to the logger


# WORKS
def alter_file(cmd1):  # to alter the file according to the options and parameters
    # alter add column table db
    # alter delete column table db
    # alter rename column1 column2 table db
    file_name = cmd1[-2] + ".csv"
    database_name = cmd1[-1]
    csv.register_dialect('myDialect', skipinitialspace=True)  # create a new dialect to skip initial space after comma

    if "rename" == cmd1[1]:
        old_name = str(cmd1[2])  # get the old value
        new_name = str(cmd1[3])  # get the new value

        cddir("data\\" + database_name)

        src = open(file_name, "r", newline='')  # open the file for reading
        rdr = csv.reader(src, dialect='myDialect')  # read the file
        lines = list(rdr)  # store the details as a list

        p = 0
        old_line = lines[0]
        for i, v in enumerate(old_line):
            if v == old_name:
                old_line[i] = new_name  # replace the old name with the new one
                p += 1

        if p == 0:
            print("No such column exists")
            return

        with open(file_name, "w", newline='') as res:  # now open a file for writing
            wtr = csv.writer(res, dialect='myDialect')
            wtr.writerows(lines)  # write the lines into the file

        src.close() # close the source file

        ch = old_name + " renamed to " + new_name + " in " + file_name + "\\" + database_name
        print(ch)
        log1 = ch

    elif "delete" == cmd1[1] or "add" == cmd1[1]:  # because they share the first 8 lines
        cddir("data\\" + database_name)

        src = open(file_name, "r", newline='')
        rdr = csv.reader(src, dialect='myDialect')
        lines = list(rdr)

        q = 0
        p = 0
        column_name = lines[0]
        src.close()

        if "delete" == cmd1[1]:
            ctbd = cmd1[2]  # column to be deleted

            for i, v in enumerate(column_name):  # to find position of column
                if v == ctbd:
                    q = i
                    p += 1

            if p == 0:
                print("No such column exists")
                return

            with open(file_name, "w", newline='') as res:
                wtr = csv.writer(res, dialect='myDialect')
                new_lines = lines

                for i in new_lines:  # to remove the column
                    try:
                        i.pop(q)

                    except IndexError:
                        continue

                wtr.writerows(new_lines)
                ch = "Column " + ctbd + " deleted from " + file_name + "\\" + database_name

        else:
            ctba = cmd1[2]

            with open(file_name, "w", newline='') as res:
                wtr = csv.writer(res, dialect='myDialect')
                column_name = lines[0]

                column_name.append(ctba)

                lines[0] = column_name
                wtr.writerows(lines)  # adding the column
                ch = "Column " + ctba + " added to " + file_name + "\\" + database_name

        print(ch)
        log1 = ch

    else:
        return -1

    log_activity(log1)


# WORKS
def search_file(cmd, comm_list):  # to search for a particular record
    # search column value file_name database_name
    database_name = comm_list[-1]
    file_name = comm_list[-2] + ".csv"
    just_file_name = comm_list[-2]
    cddir("data\\" + database_name)

    column_name = comm_list[1]

    value_start = cmd.find(column_name) + len(column_name) + 1
    value_end = cmd.find(just_file_name) - 1

    svalue = cmd[value_start:value_end]
    column_pos = 0

    found_rows = []
    clean_found_rows = []

    csv.register_dialect("myDialect", skipinitialspace=True)

    with open(file_name, "r", newline='') as src:
        rdr = csv.reader(src, dialect='myDialect')
        lines = list(rdr)

    headings = lines[0]

    p = 0
    for k, v in enumerate(headings):
        if v == column_name:
            column_pos = k
            p += 1

    if p == 0:
        print("No column named " + column_name + " in " + file_name + "\\" + database_name)
        return

    for row in lines:
        if row[column_pos] == svalue:
            found_rows.append(row)

    if len(found_rows) == 0:
        print("0 rows having " + column_name + " = " + svalue + " in " + file_name + "\\" + database_name)

    for row in found_rows:
        clean_found_rows.append(str(row).replace("[", "").replace("]", ""))

    print(*clean_found_rows, sep='\n')

    log1 = "Search " + column_name + " = " + svalue + " in " + file_name + "\\" + database_name
    log_activity(log1)


# WORKS
def drop_database(database_name):  # to drop a database(including the files)
    cddir("data")
    os.system("rmdir /s /q " + database_name)
    print(database_name, "Dropped")
    log1 = database_name + " Dropped"
    log_activity(log1)


# WORKS
def drop_file(file_name, database_name):  # to drop a file(including the structure)
    file_name += ".csv"
    cddir("data\\" + database_name)
    os.system("del " + file_name)
    print(file_name, "deleted from", database_name)
    log1 = "Dropped " + file_name + " from " + database_name
    log_activity(log1)


# PARTIAL
def delete_record(comm, comm_list):  # to delete a record using a provided condition
    # delete [*, *, value, *, value] file_name database_name
    database_name = comm_list[-1]
    file_name = comm_list[-2]


    values = str_to_list(comm)

    log1 = cmd
    log_activity(log1)


# WORKS
def program_exit():  # to exit the dbms
    log1 = "Exit"
    log_activity(log1)
    exit()


# WORKS
def show_version():  # to print the version
    version_number = "1.0a"  # a - alpha, b - beta
    print("Version : ", version_number)
    log1 = "Version requested"
    log_activity(log1)


# WORKS
def show_license():  # to show the GNU General Public License Version 3 from the LICENSE file
    cddir(".")  # . represents the current directory
    with open("LICENSE", 'r') as f:
        lic = f.readlines()
        for row in lic:
            print(row)


# WORKS
def command_parser():  # to parse the commands and call the appropriate functions
    try:
        print()
        comm = input("VenoDB> ")
        comm = comm.strip()
        comm_list = comm.split(" ")

        # comm = true_comm

        # take the first token of the command and check if it matches any command
        token1 = comm_list[0]

        if "list" == token1[0:4]:
            list_db_files(comm_list,comm)
            pass

        elif "version" == token1[0:7]:
            show_version()

        elif "create" == token1[0:6]:
            if comm_list[1] == "database":
                create_folder(comm_list[-1])

            elif comm_list[1] == "table":
                paren_start = comm.find("(")
                paren_end = comm.find(")")
                headings = comm[paren_start+1:paren_end]
                create_file(comm_list[-2], comm_list[-1], headings)

            else:
                syntax_error(comm)

        elif "show" == token1[0:4]:
            show(comm_list)

        elif "insert" == token1[0:6]:
            insert(comm_list, comm)

        elif "alter" == token1[0:5]:
            w = alter_file(comm_list)
            if w == -1:
                syntax_error(comm)
            pass

        elif "search" == token1[0:6]:
            search_file(comm, comm_list)
            pass

        elif "delete" == token1[0:6]:
            delete_record(token1[7:])
            pass

        elif "drop" == comm[0:4]:
            # drop file file_name database_name
            if "database" in comm[5:13]:
                drop_database(database_name=comm_list[-1])

            elif "table" in comm[5:10]:
                drop_file(file_name=comm_list[-2], database_name=comm_list[-1])

            else:
                syntax_error(comm)

        elif "replace" == token1[0:7]:
            replace_record(comm_list, comm)

        elif "exit" == token1[0:4]:
            program_exit()

        elif "license" == token1[0:7]:
            show_license()

        else:  # else display syntax error
            syntax_error(comm)

    except KeyboardInterrupt:
        clear()
        program_exit()


# WORKS
def syntax_error(comm):
    print("Check your syntax for the command:", comm)


# WORKS
def main():
    if init():
        # display some info on the screen and do some preparations to the program :)
        clear()
        print("\n###################################################################################################")
        print(" VenoDB - Copyright (C) 2019 EpycZen")
        print(" This program comes with ABSOLUTELY NO WARRANTY; for details type `license\'.")
        print(" This is free software, and your are welcome to redistribute it under certain conditions;")
        print()
        print(" All commands are CaSe-SeNsItIvE")
        print(" View README.md for some info")
        print("###################################################################################################")
        while True:
            command_parser()

    else:
        program_exit()


main()
