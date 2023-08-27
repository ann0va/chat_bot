import sqlite3

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_roles (
                user_id INTEGER PRIMARY KEY,
                role TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_user_role(self, user_id, role):
        self.cursor.execute('''
            INSERT INTO user_roles (user_id, role)
            VALUES (?, ?)
        ''', (user_id, role))
        self.conn.commit()

    def get_user_role(self, user_id):
        self.cursor.execute('''
            SELECT role FROM user_roles WHERE user_id = ?
        ''', (user_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def close_connection(self):
        self.conn.close()

# Example usage
if __name__ == '__main__':
    db = Database('/home/josan/Desktop/projekt/db/bot_database.db')
    db.create_table()

   ''' # Insert user roles (you can run this part for each of your users)
    db.insert_user_role(123456, 'user')  # Replace 123456 with the actual user IDs

    # Get user role (replace 123456 with the user ID you want to query)
    user_role = db.get_user_role(123456)
    print(f'User role: {user_role}')

    db.close_connection()'''