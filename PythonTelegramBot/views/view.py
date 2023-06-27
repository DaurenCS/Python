class TaskView:
    
    @staticmethod
    def start_message():
        return(
            'Hi there, it is the to-do list bot. \n'
            '/start  - start the bot \n'
            '/add  -   add the new task \n'
            '/list  -  list of all task \n'
            '/done  -  done the task \n'
            '/remove - remove task from list \n'
        )
    
    
    @staticmethod
    def add_succesfully():
        return 'Task added succesfully'
    
    @staticmethod
    def empty_list():
        return 'Task list is empty'

    @staticmethod
    def invalid():
        return "Something is wrong"

    @staticmethod
    def task_removed_succesfully(id):
        return f"Task '{id}' removed succesfully."
    
    @staticmethod
    def task_done_succesfully(id):
        return f"Task '{id}' done succesfully."


    @staticmethod
    def task_list(tasks):
        str = ""
        for task in tasks:
            if task.status == 0:
                str += f"\n{task.index}   {task.text}   In process" 
            else:
                str += f"\n{task.index}   {task.text}   Done" 
                
        
        return f"Task list:\n{str}" 
