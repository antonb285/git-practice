def set_priority(task, priority):
    """Set priority level (low, medium, high)"""
    valid_priorities = ['low', 'medium', 'high']
    if priority in valid_priorities:
        task['priority'] = priority
        return True
    return False

def get_high_priority_tasks(tasks):
    """Filter tasks by high priority"""
    return [t for t in tasks if t.get('priority') == 'high']