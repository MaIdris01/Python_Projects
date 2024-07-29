from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
import sys

app = Flask(__name__)


conn = sqlite3.connect('bank_app.db')
cursor = conn.cursor()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_user', methods=['GET', 'POST'])

# # Creating a user here....

def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            message = f"User {username} created successfully."

        except sqlite3.IntegrityError:
            message = f"Unable to create user. Username '{username}' already exists."
        return render_template('message.html', message=message)
    return render_template('create_user.html')
 

@app.route('/sign_in_user', methods=['GET', 'POST'])

# Authenticate the user
def sign_in_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))   
        user = cursor.fetchone()

        if user:
            message = f"Welcome, {username}!"
        else:
            message = "Invalid username or password."
        return render_template('message.html', message=message)
    return render_template('sign_in_user.html')


@app.route('/view_users')
# View all users
def view_users():
    
    cursor.execute('SELECT id, username FROM users')
    users = cursor.fetchall()
    return render_template('view_users.html', users=users)


@app.route('/update_user', methods=['GET', 'POST'])
# Update user's password here
def update_user():
    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['new_password']
        cursor.execute('UPDATE users SET password=? WHERE username=?', (new_password, username))
        conn.commit()
        if cursor.rowcount > 0:
            message = f"Password updated successfully for {username},"
        else:
            message = f"User '{username}' not found."
        return render_template('message.html', message=message)
    return render_template('update_user.html')


@app.route('/delete_user', methods=['GET', 'POST'])
# Delete user here
def delete_user():
    if request.method == 'POST':
        username = request.form['username']
        cursor.execute('DELETE FROM users WHERE username=?', (username,))
        conn.commit()
        if cursor.rowcount > 0:
            message = f"User '{username}' deleted successfully."
        else:
            message = f"User '{username}' not found."
        return render_template('message.html', message=message)
    return render_template('delete_user.html')
    

if __name__ == "__main__":
    app.run(debug=True)