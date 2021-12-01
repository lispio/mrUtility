# mrUtility
> mrUtility is a project for (re)configure, status, basic debug etc. "Manny's recipes (mr)" project 
## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [TO DO](#to-do)

<!-- * [License](#license) -->


## General Information
mrUtility is a tool for "Manny's recipes (mr)"
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- python3
- bash


## Setup 
requirements:
- Python3
- postgresql 13

insall:
run install.sh

## Usage
Display help 
`./mrUtility.py -h `

Display options for db module 
`./mrUtility.py db -h  ` 

Examples:

create empty database with name 'mr'
`./mrUtility.py db -cdb mr  ` 

apply migrations to database
`./mrUtility.py db -am <path to migrations>  -db <database name>  ` 

Service status 
`./mrUtility.py -services_status  ` 


## Project Status
Project is: _in progress_

## To Do
- module for moc data 
- test runner
- ...


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->