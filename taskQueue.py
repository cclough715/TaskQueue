'''
Author: Chad Clough
Created: 4/24/2015
'''

import sys
import uuid
from subprocess import call

class TaskQueue:
    def __init__(self):
        '''
            Creates an empty TaskQueue
        '''
        self._tasks = []
        
    def push(self, task):
        '''
            Pushes a Task into the queue
        '''
        self._tasks.append(task)
        
    def pop(self):
        '''
            Removes and returns the first Task in the queue
        '''
        return self._tasks.pop()
        
    def peek_all(self):
        '''
            Returns a list of al of the Tasks in the queue
        '''
        return self._tasks
        
    def peek_next(self):
        '''
            Returns the next Task in the queue; None if the
            queue is empty
        '''
        if (not self.is_empty()):
            return self._tasks[0]
        else:
            return None
    
    def count(self):
        '''
            Returns the number of tasks currently in the queue
        '''
        return len(self._tasks)

    def is_empty(self):
        '''
            Returns True if there are no Tasks currently in the 
            queue; False otherwise
        '''
        return len(self._tasks) == 0
      
      
class Task:
    def __init__(self, description, command):
        '''
            Creates a Task with the given description and command
            and generates a GUID for the Task
        '''
        self.description = description
        self.command = command
        self.GUID = uuid.uuid4()
        
    def execute(self):
	'''
            Executes the command

            **WARNING SECURITY HAZARD**
            This code executes shell commands for unsanitized input
	'''
        call(self.command, shell=True)
    
if __name__ == '__main__':
    simple_tasks = TaskQueue()
    simple_tasks.push(Task(description='My first task', 
                      command='ping -c 3 google-public-dns-a.google.com'))
    simple_tasks.push(Task(description='My second task', 
                      command='ping -c 3 google-public-dns-a.google.com'))
    
    while simple_tasks.peek_next():
        t = simple_tasks.pop()
        sys.stdout.write('Running task %s\n' % t.GUID)
        t.execute()
