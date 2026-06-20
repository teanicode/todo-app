class Task:
    def __init__(self, title, description):
        self.title=title
        self.description=description
        self.completed=False

    def mark_done(self):
        self.completed=True

    def __str__(self):
        status = "[Done]" if self.completed else "[TODO]"
        return f"{status} {self.title} : {self.description}"

class TodoManager:
    def __init__(self):
        self.tasks = []
    
    
    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"✓ Added: {title}")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
    
    def complete_task(self, task_num):
        if 0 < task_num <= len(self.tasks):
            self.tasks[task_num - 1].mark_done()
            print("✓ Task marked complete!")
        else:
            print("Invalid task number")

    def save_tasks(self):
        import json
        tasks_data = [
            {
                "title": task.title,
                "description": task.description,
                "completed": task.completed
            }
            for task in self.tasks
        ]
        with open("tasks.json", "w") as f:
            json.dump(tasks_data, f, indent=2)
        print("✓ Tasks saved!")
    
    def load_tasks(self):
        import json
        try:
            with open("tasks.json", "r") as f:
                tasks_data = json.load(f)
                for task_data in tasks_data:
                    task = Task(task_data["title"], task_data["description"])
                    task.completed = task_data["completed"]
                    self.tasks.append(task)
            print(f"✓ Loaded {len(self.tasks)} tasks!")
        except FileNotFoundError:
            print("No saved tasks yet.")

if __name__ == "__main__":
    manager = TodoManager()
    manager.load_tasks()  # ← ADD THIS LINE (load saved tasks)
    
    while True:
        print("\n========== TODO APP ==========")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task complete")
        print("4. Save & Exit")
        print("==============================")
        
        choice = input("Choose (1-4): ")
        
        if choice == "1":
            title = input("Task name: ")
            description = input("Description: ")
            manager.add_task(title, description)
        
        elif choice == "2":
            print()
            manager.view_tasks()
        
        elif choice == "3":
            manager.view_tasks()
            try:
                task_num = int(input("Task number to complete: "))
                manager.complete_task(task_num)
            except:
                print("Invalid input!")
        
        elif choice == "4":
            manager.save_tasks()  # ← SAVE BEFORE EXIT
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Try again.")