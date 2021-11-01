import time


class Task:
    def __init__(self, task_number, task_time, task_description):
        self.output = {
            "task_number": task_number,
            "time": time.strftime("%H:%M:%S", time.gmtime(task_time)),
            "description": task_description,
        }


class TaskList:
    def __init__(self):
        self.orders = []
        self.SECONDS_TO_MAKE_SANDWICH = 150
        self.SECONDS_TO_SERVE_SANDWICH = 60

    def add_order(self, recipient):
        self.orders.append(recipient)

    def list_tasks(self):

        task_list = []
        total_time = 0
        task_number = 1

        for recipient in self.orders:

            order_tasks = [
                {"description": "Make sandwich for", "time": self.SECONDS_TO_MAKE_SANDWICH},
                {"description": "Serve sandwich for", "time": self.SECONDS_TO_SERVE_SANDWICH},
            ]

            for task in order_tasks:
                task_description = " ".join([task["description"], recipient])
                task_list.append(Task(task_number, total_time, task_description).output)

                total_time += task["time"]
                task_number += 1

        task_list.append(Task(task_number, total_time, "Take a break").output)

        return task_list
