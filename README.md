# TaskQueue
============
This module is designed to store system commands for later use. The module contains the 
following classes:

Task
------------
A Task object represents an OS command which has the following members:

- GUID		A unique identifier
- description 	A description of the Task
- command	An executable command line task eg. echo
- execute()	A method to run the stored command

**CAUTION: execute() will run unsanitized input**

TaskQueue
------------
A FIFO list of Task objects. This will allow us to store commands for
later execution. A TaskQueue has the following members:

- push(Task)	Pushes a Task to the end of the queue
- pop()		Removes and returns the next Task
- peek_all()	Looks at all of the Tasks in the queue
- peek_next()	Looks at the next Task in the queue
- count()	Returns the number of Tasks left in the queue
- is_empty()	Tells us if there is any more Tasks left in the queue


##Example
````Python
>>> from taskQueue import Task
>>> from taskQueue import TaskQueue
>>> t1 = Task(description="Hello World", command="echo Hello World")
>>> t2 = Task(description="list directory", command="ls")
>>> queue = TaskQueue()
>>> queue.push(t2)
>>> queue.push(t1)
>>> t = queue.pop()
>>> print ("Running task %s\n" % t.GUID)
Running task bb05e165-84ec-4eee-8065-799320223197
>>> t.execute()
Hello World
>>> t = queue.pop()
>>> t.execute()
___init__.py  README.md  taskQueue.py
>>>
````
