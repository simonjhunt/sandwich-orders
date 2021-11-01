# sandwich-orders

A library for submitting and listing sandwich orders

## To use

   * Install using `pip install git+https://github.com/simonjhunt/sandwich-orders.git`
   * Import Tasklist `from orders.orders import TaskList`
   * Add and list orders:

```
        task_list = TaskList()

        task_list.add_order("John")
        task_list.add_order("Sue")

        task_list.list_tasks()
```
