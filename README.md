![Python 3.8](https://img.shields.io/badge/python-3.8-green.svg)
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
        -- shows help for all commands

## exit command:
    exit
        -- exits the program

## license command:
    license
        -- shows the GNU GPL 3.0 License

## list commands:
    list
    -- lists all the databases(folders)
    list file <database>
    -- lists all the files(tables) in a database

## show command:
    show <file> <database>
        -- shows all the records in a file

## version command:
    version
        -- shows the version of the program

## create commands:
    create database <database>
        -- creates a new database(folder)
    create table <file> <database>
        -- creates a new file(table) in a database

## insert command:
    insert [value list] <file> <database>
        -- inserts values in a file

## alter commands:
    alter add <column name> <file> <database>
        -- adds a new column
    alter delete <column name> <file> <database>
        -- deletes an existing column
    alter rename <old column> <new column> <file> <database>
        -- renames an existing column

## search command:
    search <column name> <value> <file> <database>
        -- shows all the records with matching column name and the value

## delete command:
    delete [value list] <file> <database>
        -- deletes all records matching the input

## drop commands:
    drop table <file> <database>
        -- deletes a file(table)
    drop database <database>
        -- deletes a database(folder)

## replace command:
    replace [old values] [new values] <file> <database>
        -- replaces old values with new values
