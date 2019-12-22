![GNU GPL 3.0](https://img.shields.io/github/license/EpycZen/VenoDB)
![Python 3.8](https://img.shields.io/badge/python-3.8-green.svg)
![Repo Size](https://img.shields.io/github/repo-size/EpycZen/VenoDB)

[VenoDB](https://EpycZen.GitHub.io/VenoDB)

# VenoDB
A Python based **CSV DBMS**.
It has basic DBMS functionalities. 
A table is called a **file**(.csv file).
A **database** is a folder which contains files.
Support for linux will be made(soon) with slight changes to the main program and with a Linux.py module.
Commands are used as input.
Users, Security and Network Connectivity will be implemented in version 2.

Don't forget to change the INSTALLATION_DIRECTORY.txt

Structure Tree:
**VenoDB**
- *data* # database folder
- *log* # to save logs
- *programs*
  - *VenoDBv1.py* # main program
  - *Windows.py* # windows shell command handler
  - *INSTALLATION_DIRECTORY.txt* # to put the installation directory
  
# VenoDB Commands:

## help command:
    help
 shows help for all commands

## exit command:
    exit
exits the program

## license command:
    license
shows the GNU GPL 3.0 License

## list commands:
    list
lists all the databases(folders)

    list files <database>
    example: list files employee_db
lists all the files(tables) in a database

## show command:
    show <file> <database>
    example: show grade_8 school_db
shows all the records in a file

## version command:
    version
shows the version of the program

## create commands:
    create database <database>
    example: create database db_1
creates a new database(folder)

    create table <file> <database>
    example: create table grade_9 school_db
creates a new file(table) in a database

## insert command:
    insert [value list] <file> <database>
    example: insert [1, John Doe, M] employee office_db
inserts values in a file

## alter commands:
    alter add <column name> <file> <database>
    example: alter add age employee office_db
adds a new column

    alter delete <column name> <file> <database>
    example: alter delete email grade_6 school_db
deletes an existing column

    alter rename <old column> <new column> <file> <database>
    example: alter rename mail email employee office_db
renames an existing column

## search command:
    search <column name> <value> <file> <database>
    example: search id 5 employee office_db
shows all the records with matching column name and the value

## delete command:
    delete [value list] <file> <database>
    delete [3, Jeff Bezos] blue_origin world
deletes all records matching the input

## drop commands:
    drop table <file> <database>
    drop table blue_origin world
deletes a file(table)
        
    drop database <database>
    drop database flat_earth
deletes a database(folder)

## replace command:
    replace [old values] [new values] <file> <database>
    replace [1, Intel] [1, AMD] company world
replaces old values with new values
