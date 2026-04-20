


import os

class TaskManager:
    def __init__(self):
        self.filename = "my_tasks.txt"
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()

    def add_task(self, task_id, desc):
        with open(self.filename, "a") as file:
            file.write(f"{task_id}|{desc}|Pending\n")
        print("Task saved successfully.")

    def view_tasks(self):
        with open(self.filename, "r") as file:
            records = file.readlines()
            if len(records) == 0:
                print("Your to-do list is empty.")
                return
            
            print("\n--- ALL TASKS ---")
            for rec in records:
                parts = rec.strip().split("|")
                print(f"ID: {parts[0]} | Desc: {parts[1]} | Status: {parts[2]}")
            print("-----------------\n")

    def update_task(self, task_id, new_status):
        with open(self.filename, "r") as file:
            records = file.readlines()
        
        updated = False
        with open(self.filename, "w") as file:
            for rec in records:
                parts = rec.strip().split("|")
                if parts[0] == task_id:
                    file.write(f"{parts[0]}|{parts[1]}|{new_status}\n")
                    updated = True
                else:
                    file.write(rec)
        
        if updated:
            print("Task updated successfully.")
        else:
            print("Task ID not found.")

    def delete_task(self, task_id):
        with open(self.filename, "r") as file:
            records = file.readlines()
        
        found = False
        with open(self.filename, "w") as file:
            for rec in records:
                if not rec.startswith(task_id + "|"):
                    file.write(rec)
                else:
                    found = True
        
        if found:
            print("Task deleted.")
        else:
            print("Task ID not found.")

    def search_task(self, keyword):
        print("\n--- SEARCH RESULTS ---")
        found = False
        with open(self.filename, "r") as file:
            for rec in file:
                if keyword.lower() in rec.lower():
                    parts = rec.strip().split("|")
                    print(f"ID: {parts[0]} | Desc: {parts[1]} | Status: {parts[2]}")
                    found = True
        if not found:
            print("No matching tasks found.")
        print("----------------------\n")

def main():
    app = TaskManager()
    
    while True:
        print("\n1. Add New Task")
        print("2. View All Tasks")
        print("3. Update Task Status")
        print("4. Delete a Task")
        print("5. Search Task")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            t_id = input("Enter Task ID: ")
            desc = input("Enter Description: ")
            app.add_task(t_id, desc)
        elif choice == '2':
            app.view_tasks()
        elif choice == '3':
            t_id = input("Enter Task ID to update: ")
            status = input("Enter new status (Pending/Completed): ")
            app.update_task(t_id, status)
        elif choice == '4':
            t_id = input("Enter Task ID to delete: ")
            app.delete_task(t_id)
        elif choice == '5':
            key = input("Enter keyword to search: ")
            app.search_task(key)
        elif choice == '6':
            print("Closing application...")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()