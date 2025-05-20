import os
import platform

OS_TYPE = platform.system()

def list_processes():
    print("\nListing all processes...\n")
    if OS_TYPE == "Windows":
        os.system("tasklist")  
    else:
        os.system("ps aux")

def search_process(name):
    print(f"\nSearching for process: {name}...\n")
    if OS_TYPE == "Windows":
        os.system(f'tasklist | findstr {name}')
    else:
        os.system(f'ps aux | grep {name} | grep -v grep')

def kill_process(pid):
    print(f"\nAttempting to terminate process ID: {pid}...\n")
    if OS_TYPE == "Windows":
        os.system(f'taskkill /PID {pid} /F')
    else:
        os.system(f'kill -9 {pid}')

def show_buffer_processes():
    print("\nTop memory-consuming (buffer-heavy) processes:\n")
    if OS_TYPE == "Windows":
        os.system("wmic process get Name,ProcessId,WorkingSetSize /FORMAT:TABLE")
    else:
        os.system("ps -eo pid,comm,%mem --sort=-%mem | head -10")

def show_process_hierarchy():
    print("\nShowing process hierarchy (PPID):\n")
    if OS_TYPE == "Windows":
        os.system("wmic process get Name,ProcessId,ParentProcessId /FORMAT:TABLE")
    else:
        os.system("ps -eo pid,ppid,comm --sort=ppid")

while True:
    print("\n=== CLI-Based Process Manager ===")
    print("1. List Processes")
    print("2. Search Process by Name")
    print("3. Kill Process by PID")
    print("4. Show Buffer-heavy Processes")
    print("5. Show Process Hierarchy(Parent & Child Info)")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        list_processes()
    elif choice == "2":
        process_name = input("Enter process name: ")
        search_process(process_name)
    elif choice == "3":
        process_id = input("Enter PID to terminate: ")
        kill_process(process_id)
    elif choice == "4":
        show_buffer_processes()
    elif choice == "5":
        show_process_hierarchy()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
