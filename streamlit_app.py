import streamlit as st
import json

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def main():
    st.title("📝 To-Do App with Streamlit")
    st.subheader("Manage your tasks easily!")
    
    tasks = load_tasks()
    
    # Add New Task
    new_task = st.text_input("Add a new task:")
    if st.button("Add Task"):
        if new_task:
            tasks.append({"task": new_task, "completed": False})
            save_tasks(tasks)
            st.rerun()  # <-- Updated here
    
    # Show Tasks
    st.subheader("Your Tasks")
    if tasks:
        for index, task in enumerate(tasks):
            col1, col2, col3 = st.columns([0.7, 0.2, 0.1])
            with col1:
                st.write("✔️" if task["completed"] else "❌", task["task"])
            with col2:
                if st.button("Complete", key=f"complete_{index}"):
                    tasks[index]["completed"] = True
                    save_tasks(tasks)
                    st.rerun()  # <-- Updated here
            with col3:
                if st.button("❌", key=f"delete_{index}"):
                    del tasks[index]
                    save_tasks(tasks)
                    st.rerun()  # <-- Updated here
    else:
        st.write("No tasks available.")

if __name__ == "__main__":
    main()
