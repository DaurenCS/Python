import sqlite3
from models.task import Task as t
from views import view

class TaskController:
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY,text TEXT, status INTEGER DEFAULT 0)')
    
    def add_task(self,text,index):
        try:
            self.cursor.execute('INSERT INTO tasks (id, text) VALUES (?,?)',(index, text))
            self.conn.commit()
            return view.TaskView.add_succesfully()
        except sqlite3.Error as e:
            return view.TaskView.invalid()


    def delete_task(self, id):
        try:
            self.cursor.execute('DELETE FROM tasks WHERE id=?',(id,))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                return view.TaskView.invalid()
            else:
                return view.TaskView.task_removed_succesfully(id)
                
        except sqlite3.Error as e:
            return view.TaskView.invalid()
    
    
    def task_list(self):
        self.cursor.execute('SELECT id,text,status FROM tasks')
        tasks = self.cursor.fetchall()

        if not tasks:
            return 'there no task'
        
        task_list = [t(index=task[0],text = task[1],status = task[2]) for task in tasks]
        return view.TaskView.task_list(task_list)
    
    def done_task(self, task_id):
        try:
            self.cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (1, task_id))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                return view.TaskView.invalid()
            else:
                return view.TaskView.task_done_succesfully(task_id)
        except sqlite3.Error as e:
            return view.TaskView.invalid()
        
    def __del__(self):
        self.cursor.close()
        self.conn.close()
            