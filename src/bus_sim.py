"""
This module demonstrates how to run a task in a separate thread 
at regular intervals using Python's threading module.
"""

import threading
import time

from bus_messages import AIRCRAFT_1_HT_ESCM_DAC

def init_values():
    message = AIRCRAFT_1_HT_ESCM_DAC()
    message.randomize()
    return message

def task():
    """The function that will run in a separate thread."""
    print("Task executed!")
    message = init_values()

def schedule_task():
    """Schedules the task to run repeatedly."""
    # Create a Timer to run the task again after 20 ms (0.02 seconds)
    threading.Timer(0.02, schedule_task).start()
    # Execute the task
    task()

# Start the initial scheduling
schedule_task()
    
