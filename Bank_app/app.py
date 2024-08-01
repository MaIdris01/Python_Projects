from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'bank_app.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row

    return g.db

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# conn = sqlite3.connect('bank_app.db')
# cursor = conn.cursor()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_user', methods=['GET', 'POST'])

# # Creating a user here....

def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()

        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            db.commit()
            message = f"User {username} created successfully.\n"
            # return render_template('access_html/message.html', message=message)
            
        except sqlite3.IntegrityError:
            message = f"Unable to create user. Username '{username}' already exists."
        return render_template('mutation_html/create_user.html', message=message)
    return render_template('mutation_html/create_user.html')
 

@app.route('/sign_in_user', methods=['GET', 'POST'])

# Authenticate the user
def sign_in_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))   
        user = cursor.fetchone()

        if user:
            message = f"Welcome, {username}!"
        else:
            message = "Invalid username or password."
        return render_template('access_html/message.html', message=message)
    return render_template('access_html/sign_in_user.html')


@app.route('/view_users')
# View all users
def view_users():
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT id, username FROM users')
    users = cursor.fetchall()
    return render_template('access_html/view_users.html', users=users)


@app.route('/update_user', methods=['GET', 'POST'])
# Update user's password here
def update_user():
    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['new_password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute('UPDATE users SET password=? WHERE username=?', (new_password, username))
        db.commit()
        if cursor.rowcount > 0:
            message = f"Password updated successfully for {username}."
        else:
            message = f"User '{username}' not found."
        return render_template('access_html/message.html', message=message)
    return render_template('mutation_html/update_user.html')


@app.route('/delete_user', methods=['GET', 'POST'])
# Delete user here
def delete_user():
    if request.method == 'POST':
        username = request.form['username']
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM users WHERE username=?', (username,))
        db.commit()
        
        if cursor.rowcount > 0:
            message = f"User '{username}' deleted successfully."
        else:
            message = f"User '{username}' not found."
        return render_template('access_html/message.html', message=message)
    return render_template('mutation_html/delete_user.html')

@app.route('/success', methods=['POST', 'GET'])
def success():
    if request.method == 'POST':
        res = "success"
    return render_template('success.html', res=res)
    

if __name__ == "__main__":
    app.run(debug=True)