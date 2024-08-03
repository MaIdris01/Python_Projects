Overview

This application provides a simple command-line interface to manage user data using SQLite. It allows for user creation, authentication, viewing, updating, and deletion.


Requirements

Python 3.x
SQLite3(comes bundled with Python)


How It Works

Initiaization:

    * The script initializes an SQLite database named 'bank_app.db'.
    * A table named 'users' is created if it does not already exist. This table has the following columns:
        > id : An integer primary key that auto-increments.
        > username : A text that must be unique.
        > password : A text field for the user's password.


Features/Function Definitions

    * create_user(username, password) : Inserts a new user into the 'users' table. If the username already exists, an error message is displayed.
    
    * sign_in_user(username, password) : Authenticates a user by checking if the provided username and password match an entry in the database.
    
    * view_users() : Fetches and displays all user IDs and usernames from the database. Displays a message if the user is not found.
    
    * delete_user(username) : Deletes the specified user from the database. Displays a message if the user is not found.



Main Menu

Create User
Sign In User
View User
Update User
Delete User
Exit


Program Exit:
    * The program will exit upon completing an action or if the user chooses to exit from the main menu. 

Usage

    * Run the Script: Execute the script from the command line.
    * Interact with the Menu: Follow the prompts to create, sign in, view, update, or delete users.
    * Exit: Choose the 'Exit' option from the menu to close the application.

