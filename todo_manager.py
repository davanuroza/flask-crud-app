import sqlite3

class ToDoManager:
    def __init__(self, db_name='todo.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute('SELECT id, task FROM todos')
        todos = [{'id': row[0], 'task': row[1]} for row in cursor.fetchall()]
        return todos

    def add(self, task):
        self.conn.execute('INSERT INTO todos (task) VALUES (?)', (task,))
        self.conn.commit()

    def update(self, todo_id, new_task):
        self.conn.execute('UPDATE todos SET task = ? WHERE id = ?', (new_task, todo_id))
        self.conn.commit()

    def delete(self, todo_id):
        self.conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
        self.conn.commit()
