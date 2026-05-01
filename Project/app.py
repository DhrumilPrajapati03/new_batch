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
        break

task()