import unittest

from orders.orders import TaskList


class TestListTasks(unittest.TestCase):
    def test_take_a_break_when_no_orders(self):

        order_list = TaskList()

        self.assertEqual(
            order_list.list_tasks(),
            [{"task_number": 1, "time": "00:00:00", "description": "Take a break"}],
        )

    def test_list_displays_correct_time_to_make_and_serve_order(self):

        order_list = TaskList()

        order_list.add_order("John")

        self.assertEqual(
            order_list.list_tasks(),
            [
                {
                    "task_number": 1,
                    "time": "00:00:00",
                    "description": "Make sandwich for John",
                },
                {
                    "task_number": 2,
                    "time": "00:02:30",
                    "description": "Serve sandwich for John",
                },
                {"task_number": 3, "time": "00:03:30", "description": "Take a break"},
            ],
        )

    def test_works_as_expected_with_mulitple_orders_from_same_name(self):

        order_list = TaskList()

        order_list.add_order("John")
        order_list.add_order("John")

        self.assertEqual(
            order_list.list_tasks(),
            [
                {
                    "task_number": 1,
                    "time": "00:00:00",
                    "description": "Make sandwich for John",
                },
                {
                    "task_number": 2,
                    "time": "00:02:30",
                    "description": "Serve sandwich for John",
                },
                {
                    "task_number": 3,
                    "time": "00:03:30",
                    "description": "Make sandwich for John",
                },
                {
                    "task_number": 4,
                    "time": "00:06:00",
                    "description": "Serve sandwich for John",
                },
                {"task_number": 5, "time": "00:07:00", "description": "Take a break"},
            ],
        )

    def test_time_rolls_over_to_hours_with_many_orders(self):

        order_list = TaskList()

        for n in range(20):
            order_list.add_order(f"order{n}")

        tasks = order_list.list_tasks()

        self.assertEqual(tasks[40]["time"], "01:10:00")
