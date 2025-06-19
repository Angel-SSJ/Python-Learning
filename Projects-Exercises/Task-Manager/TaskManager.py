import os.path

filename = 'tasks.txt'
from datetime import datetime


class Task:
    def __init__(self, title, description, status, date):
        self.title = title
        self.description = description
        self.status = status
        self.date = date

    def modify_field(self, field, new_value):
        if field == 'title':
            self.title = new_value
        if field == 'description':
            self.description = new_value
        if field == 'status':
            self.status = new_value
        if field == 'date':
            self.date = new_value


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, status, date=None):
        task = Task(title, description, status, date)
        self.tasks.append(task)
        print('Task Added Successfully')

    def modify_task(self, title, field, new_value):
        valid_contents = ['title', 'description', 'status', 'date']

        if field not in valid_contents:
            print('Field is not valid')
            return

        for task in self.tasks:
            if task.title == title:
                if field == 'title':
                    self.change_title_task(title, new_value)
                if field == 'description':
                    self.change_description_task(title, new_value)
                if field == 'status':
                    self.change_status_task(self, title, new_value)
                if field == 'date':
                    self.change_date_task(self, title, new_value)
                return

        print('The task not exists')

    def change_date_task(self, title, new_value, field='date'):
        if not self.validate_date_format(new_value):
            print('Invalid date format. Use MM-DD-YY')
            return

        for task in self.tasks:
            if task.title == title:
                task.modify_field(field, new_value)
                print('date Changed Successfully')
                return

        print('The task not exists')

    @staticmethod
    def validate_date_format(date_str):
        try:
            datetime.strptime(date_str, '%m-%d-%Y')
            return True
        except ValueError:
            return False

    def change_title_task(self, title, new_value, field='title'):
        for task in self.tasks:
            if task.title == title:
                task.modify_field(field, new_value)
                print('Title Changed Successfully')
                return
        print('The task not exists')

    def change_description_task(self, title, new_value, field='description'):
        for task in self.tasks:
            if task.title == title:
                task.modify_field(field, new_value)
                print('Description Changed Successfully')
                return

        print('The task not exists')

    def change_status_task(self, title, new_value, field='status'):
        allowed_status = ['Not Started', 'Planning', 'In progress', 'Done', 'Canceled']

        if new_value not in allowed_status:
            print('The status is not valid')
            return

        for task in self.tasks:
            if task.title == title:
                task.modify_field(field, new_value)
                print('Status Changed Successfully')
                return

        print('The task not exists')

    def view_all_tasks(self):
        if self.tasks:
            print('All tasks: ')
            for i, task in enumerate(self.tasks, start=0):
                if i == 0:
                    continue
                print(f'{i}: Title: {task.title} \n   Description: {task.description} \n   Status: {task.status}\n   Date: {task.date}\n')

        return

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f'Task {title} had deleted successfully.')
                return

        print('Task was not found :(')

    def save_tasks(self, file):
        with open(file, 'w') as f:
            for task in self.tasks:
                f.write(f'{task.title},{task.description},{task.status},{task.date}\n')

        print('Task data saved successfully.')

    def load_tasks(self, file):
        try:
            with open(file, 'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) == 4:
                        title = data[0]
                        description = data[1] if len(data) > 1 else ' '
                        status = data[2] if len(data) > 2 else ' '
                        date = data[3] if len(data) > 3 else None
                        self.tasks.append(Task(title, description, status, date))
                    else:
                        return print('Invalid Text format ')
        except FileNotFoundError:
            print('No existing task data found. Starting with an empty task list.')


def main():
    task_manager = TaskManager()
    task_manager.load_tasks(filename)
    if os.path.exists(filename):

        print('Welcome to the Task Manager :D')
        while True:
            print('1. Add Task \n2. Modify any Tasks \n3. View all Tasks \n4. Delete Task \n5. Exit')

            choice = input('Enter your choice (1-5): ')
            match choice:
                case '1':
                    title = str(input('Enter task title: '))
                    description = str(input('Enter task description: '))
                    status = str(input('Enter task status (Not Started, Planning, In progress, Done): '))
                    date = str(input('Enter task date (format YYYY-MM-DD): '))
                    task_manager.add_task(title, description, status, date)
                case '2':
                    title = str(input('Enter task title: '))
                    field = str(input('Enter task field: '))
                    new_value = ''
                    if field == 'title':
                        new_value = str(input('Enter new task title: '))
                    elif field == 'description':
                        new_value = str(input('Enter new task description: '))
                    elif field == 'status':
                        new_value = str(input('Enter new status task(Not Started, Planning, In progress, Done): '))
                    elif field == 'date':
                        new_value = input('Enter task date (format MM-DD-YYYY): ')
                    else:
                        print('Invalid field entered. Please try again.')
                    task_manager.modify_task(title, field, new_value)
                case '3':
                    task_manager.view_all_tasks()
                case '4':
                    title = str(input('Enter task title: '))
                    task_manager.delete_task(title)
                case '5':
                    task_manager.save_tasks(filename)
                    break
                case _:
                    return print('Invalid Choice')
            task_manager.save_tasks(filename)


if __name__ == '__main__':
    main()
