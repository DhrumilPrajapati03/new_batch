def task():
    tasks = []
    print("---Welcome to the Task Management App---")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1,total_task+1):#(1,6)
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop/"))
        if operation == 1:
            add = input("Enter the task you want to add =") #hangout
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            update_val = input("Enter the taks name you want to update = ")
            if update_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(update_val)#2
                tasks[ind] = up
                print(f"Updated Task {up}")

        elif operation == 3:
            del_val = input("Enter the task name you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been successfully deleted")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("Closing the process...")
            break
        
        else:
            print("Invalid Input")

task()
# task()