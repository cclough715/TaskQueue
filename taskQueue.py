import uuid

class TaskQueue:
    def __init__(self):
        self._tasks = []
        
    def push(self, task):
        self._tasks.append(task)
    
    def pop():
        return
        #TODO: implement
    def peek_all():
        return
        #TODO: implement
    def peek_next():
        return
        #TODO: implement
    def count():
        return len(self._tasks)
        
class Task:
    def __init__(self, description, command):
        self.description = description
        self.command = command
        self.GUID = uuid.uuid4()
        
    def execute():
        return
        #TODO: implement
    
if __name__ == '__main__':
    tq = TaskQueue()
    t = Task(description='My first task', 
        command='ping -c 3 google-public-dns-a.google.com')
    tq.push(t)
    print string.format("Length = {}", tq.count())
    print t.GUID