"""
Problem 3: Task Scheduling Problem (Optimization)

You are given a list of tasks where each task has a deadline (day by which it must be completed) and a duration (how many days it takes).
The goal is to determine the maximum number of tasks that can be completed without missing any deadlines.

Approach:
- Sort tasks by deadline (earliest first).
- Use a greedy algorithm with a min-heap to keep track of durations of selected tasks.
- If total time exceeds current task's deadline, remove the task with the largest duration to optimize.
"""

import heapq

def max_tasks_schedule(tasks):
    # Sort tasks by their deadline
    tasks.sort(key=lambda task: task['deadline'])
    
    total_time = 0
    min_heap = []  # Will store durations (as negative to simulate max-heap)

    for task in tasks:
        duration = task['duration']
        total_time += duration
        heapq.heappush(min_heap, -duration)
        
        # If total time exceeds the deadline, remove the most time-consuming task
        if total_time > task['deadline']:
            removed = -heapq.heappop(min_heap)
            total_time -= removed

    return len(min_heap)

# Example Input
tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

# Output Result
result = max_tasks_schedule(tasks)
print(f"Maximum number of tasks that can be completed: {result}")
