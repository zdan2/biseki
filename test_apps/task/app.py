class Task:
    def __init__(self,todo,finished=None):
        self.todo=todo
        self.finished=finished
    
    def task_finished(self,finished=True):
        self.finished=finished
    
class TaskList:
    task_list=[]
    def add(self,task):
        self.task=task
        self.task_list.append(self.task)
    
    def show(self):
        for tsk in self.task_list:
            print(tsk)

t=Task('read poem')
print(t)
tl=TaskList()
tl.add(t)
tl.show()
