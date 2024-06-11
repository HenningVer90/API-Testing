import sqlite3

# Function to create a new database and table
def create_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, surname TEXT)''')
    conn.commit()
    conn.close()

# Function to insert a new user into the database
def create_user(name, surname):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users (name, surname) VALUES (?, ?)''', (name, surname))
    conn.commit()
    conn.close()

# Function to update an existing user in the database
def update_user(id, name, surname):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''UPDATE users SET name=?, surname=? WHERE id=?''', (name, surname, id))
    conn.commit()
    conn.close()

# Function to delete a user from the database
def delete_user(id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''DELETE FROM users WHERE id=?''', (id,))
    conn.commit()
    conn.close()

# Function to display all users in the database
def display_users():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    users = c.fetchall()
    print("ID\tName\tSurname")
    for user in users:
        print("{}\t{}\t{}".format(user[0], user[1], user[2]))
    conn.close()

# Main function
def main():
    create_database()

    while True:
        print("\nOptions:")
        print("1. Create user")
        print("2. Update user")
        print("3. Delete user")
        print("4. Display all users")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            create_user(name, surname)
        elif choice == '2':
            id = input("Enter ID of the user to update: ")
            name = input("Enter new name: ")
            surname = input("Enter new surname: ")
            update_user(id, name, surname)
        elif choice == '3':
            id = input("Enter ID of the user to delete: ")
            delete_user(id)
        elif choice == '4':
            display_users()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
