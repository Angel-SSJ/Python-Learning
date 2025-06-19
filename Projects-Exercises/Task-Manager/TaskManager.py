'''
# Add a task

# Remove a task

# Edit a task

# Add a description

# Edit a description

# Initial tasks list
tasks = []

# Auxiliar functions
def displayTask(all_task):
    print('\n Your tasks:')
    for index, task in enumerate(all_task):
        print(f'{index+1}: {task}')



def newOperatoin(all_tasks):
    operation = str(input("Press 'A' to add a new task, 'E' to edit a task, 'R' to remove a task or 'F' to quit he application "))

    match operation:
        case 'A':
            addTask(all_tasks)
        case 'E':
            pass
        case 'R':
            pass
        case 'F':
            pass
        case _:
            newOperatoin(all_tasks)


def addTask(all_tasks):
    new_task=str(input('Add a task: '))
    all_tasks.append(new_task)

    displayTask(all_tasks)
    newOperatoin(all_tasks)


def removeTasks(all_tasks):


addTask(tasks)
'''

class Task:
    def __init__(self, title, description, status='Incomplete'):
        self.title = title
        self.description = description
        self.status = status

    def mark_complete(self):
        self.status = 'Complete'

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task= Task(title, description, status='Imcomplete')
        self.tasks.append(task)
        print('Task Added Successfully')
    def mark_task_complete(self,title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return print(f' Task {title} marked as complete.')
            else:
                print(f' The task: {title} was not found. \n Make sure you have spelled the title correctly')
    def view_all_tasks (self):
        if self.tasks:
            print('All tasks: ')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}: Title: {task.title}, Description: {task.description}, Status: {task.status} \n')

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return print(f'Task {title} had deleted successfully.')
            else:
                return print( 'Task was not found :(')
    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f'{task.title},{task.description},{task.status}\n')
        print('Task data saved successfully.')

    def load_tasks(self, filename):
        try:
            with open(filename,'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) == 3:
                        title = data[0]
                        description = data[1] if len(data) >1 else ' '
                        status= data[2] if len(data) >2 else ' '
                        self.tasks.append(Task(title, description, status))
                    else:
                        return print('Invalid Text format ')
        except FileNotFoundError:
            print('No existing task data found. Starting with an empty task list.')

def main():
    task_manager = TaskManager()
    task_manager.save_tasks('tasks.txt')
    print('Welcome to the Task Manager :D')
    while True:
        print('1. Add Task \n2. Mark Task as Complete \n3. View all Tasks \n4. Delete Task \n5. Exit')

        choice = input('Enter your choice (1-5): ')
        match choice:
            case '1':
                title = str(input('Enter task title: '))
                description = str(input('Enter task description: '))
                #status = str(input('Enter task status: '))
                task_manager.add_task(title, description)
            case '2':
                title = str(input('Enter task to complete: '))
                task_manager.mark_task_complete(title)
            case '3':
                task_manager.view_all_tasks()
            case '4':
                title = str(input('Enter task title: '))
                task_manager.delete_task(title)
            case '5':
                break
            case _:
                return print('Invalid Choice')
        task_manager.save_tasks('tasks.txt')

if __name__ == '__main__':
    main()
