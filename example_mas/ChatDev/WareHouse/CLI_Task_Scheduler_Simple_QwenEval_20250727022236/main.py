'''
Main entry point for the CLI task scheduler.
Handles command line arguments and manages the task scheduler.
'''
import argparse
from scheduler import TaskScheduler, TaskFileHandler
from task import Task
import time
import signal
import sys
import logging
# Set up logging
logging.basicConfig(filename='scheduler.log', level=logging.INFO, format='%(asctime)s - %(message)s')
def signal_handler(sig, frame):
    '''
    Signal handler to gracefully stop the scheduler.
    '''
    print("Stopping the scheduler...")
    logging.info("Scheduler stopped by user.")
    sys.exit(0)
def add_task(scheduler, file_handler, date, time, command):
    '''
    Adds a new task to the scheduler and writes it to the file.
    '''
    try:
        task = Task(date, time, command)
        scheduler.add_task(task)
        file_handler.write_tasks(scheduler.tasks)
        print(f"Task added: {task}")
        logging.info(f"Task added: {task}")
    except ValueError as e:
        print(f"Error adding task: {e}")
        logging.error(f"Error adding task: {e}")
def execute_due_tasks(scheduler, file_handler):
    '''
    Executes all due tasks and writes the updated task list to the file.
    '''
    scheduler.execute_tasks()
    file_handler.write_tasks(scheduler.tasks)
    print("Due tasks executed.")
    logging.info("Due tasks executed.")
def main():
    '''
    Main function to parse command line arguments and run the scheduler.
    '''
    parser = argparse.ArgumentParser(description="CLI Task Scheduler")
    parser.add_argument('--add', nargs=3, metavar=('DATE', 'TIME', 'COMMAND'), help='Add a new task')
    parser.add_argument('--execute', action='store_true', help='Execute due tasks')
    args = parser.parse_args()
    scheduler = TaskScheduler()
    file_handler = TaskFileHandler("tasks.txt")
    scheduler.tasks = file_handler.read_tasks()
    if args.add:
        add_task(scheduler, file_handler, *args.add)
    elif args.execute:
        execute_due_tasks(scheduler, file_handler)
    else:
        print("No action specified. Use --add or --execute.")
        return
    # Set up signal handler for graceful termination
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Periodically check for due tasks
    try:
        while True:
            execute_due_tasks(scheduler, file_handler)
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("Stopping the scheduler...")
        logging.info("Scheduler stopped by user.")
if __name__ == "__main__":
    main()