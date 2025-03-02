import time

EZLists = {}

class EListz:
    """Allow to manage multiple EListz, allowing creation, modification, and deletion of lists."""
    
    def create(self, name):
        """Create a new EListz with the given name."""
        EZLists[name] = []
    
    def append(self, name, item):
        """Append an item to the specified EListz."""
        EZLists[name].append(item)
    
    def insert(self, name, number, item):
        """Insert an item at a specific index in the EListz."""
        EZLists[name].insert(number, item)
    
    def pop(self, name, number):
        """Remove and return an item from a specified index in the EListz."""
        return EZLists[name].pop(number)
    
    def remove(self, name, item):
        """Remove the first occurrence of a specific item from the EListz."""
        EZLists[name].remove(item)
    
    def delete(self, name):
        """Delete the entire EListz."""
        del EZLists[name]
    
    def clear(self, name):
        """Remove all items from the specified EListz."""
        EZLists[name].clear()


class eTime:
    """Allow to measure execution time and introduce delays."""
    
    def __init__(self):
        """Initialize the eTime class with start and end time attributes."""
        self.start_time = None
        self.end_time = None

    def start(self):
        """Start the timer."""
        self.start_time = time.time()

    def end(self):
        """End the timer."""
        self.end_time = time.time()

    def total(self):
        """Return the total elapsed time in seconds."""
        if self.start_time is not None and self.end_time is not None:
            return self.end_time - self.start_time
        return None

    def wait(self, seconds):
        """Pause execution for the specified number of seconds."""
        time.sleep(seconds)
