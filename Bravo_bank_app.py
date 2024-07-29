import sqlite3
import os
import sys


print("Current directory:", os.getcwd())

try:
    conn = sqlite3.connect('bank_app.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,  -- Ensure username is unique
            password TEXT NOT NULL
        )
    ''')

except sqlite3.Error as e:
    print(f"SQLite error: {e}")

# Creating a user here....
def create_user(username, password):
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print(f"User {username} created successfully.")

    except sqlite3.IntegrityError as e:
        print(f"Unable to create user: {e} Username '{username}' already exists.")
 
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        sys.exit()


# Authenticate the user
def sign_in_user(username, password):
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))   
    user = cursor.fetchone()

    if user:
        print(f"Welcome, {username}!")
    else:
        print("Invalid username or password.")

    sys.exit()

# View all users
def view_users():
    try:
        cursor.execute('SELECT id, username FROM users')
        users = cursor.fetchall()
        if users:
            print("\nList of users:")
            for user in users:
                print(f"ID: {user[0]}, Username: {user[1]}")
        else:
            print("No users found.")
            
    except sqlite3.Error as e:
        print(f"Error fetching users: {e}")

    finally:
        sys.exit()

# Update user's password here
def update_user(username, new_password):
    try:
        cursor.execute('UPDATE users SET password=? WHERE username=?', (new_password, username))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Password updated successfully for {username},")
        else:
            print(f"User '{username}' not found.")

    except sqlite3.Error as e:
        print(f"Error updating password: {e}")

    finally:
        sys.exit()

# Delete user here
def delete_user(username):
    try:
        cursor.execute('DELETE FROM users WHERE username=?', (username,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"User '{username}' deleted successfully.")
        else:
            print(f"User '{username}' not found.")
    
    except sqlite3.Error as e:
        print(f"Error deleting user: {e}")

    finally:
        sys.exit()

def main():
    while True:

        print("\n1. Create User\n2. Sign in User\n3. View Users\n4. Update User\n5. Delete User\n6. Exit")
        
        choice = input("Enter number (1/2/3/4/5/6): ").strip()

        if choice == '1':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            create_user(username, password)
            
        elif choice == '2':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            sign_in_user(username, password)


        elif choice == '3':
            view_users()


        elif choice == '4':
            username = input("Enter username to update: ").strip()
            password = input("Enter new password: ").strip()
            update_user(username, password)


        elif choice == '5':
            username = input("Enter username to delete: ").strip()
            delete_user(username)

        elif choice == '6':
            break

        else:
            print("Abeg enter correct option.")


if __name__ == "__main__":
    try:
        main()

    finally:
        conn.close()