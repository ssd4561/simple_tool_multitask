import asyncio
from enum import Enum


class node_statue(Enum):
    node_idle   =1
    node_error  =2
    node_process=3  #use this param for multithreading
    node_stoping=4
    node_end    =5


class async_node():
    def __init__(self,task_cb,async_node_name):
        self.status=node_statue.node_idle
        self.task_cb=task_cb
        self.task_name=async_node_name

    async def task_run(self):

        while True:
            try :
                self.task_cb()

                if task_check_status() is False :
                    self.status=node_statue.node_stoping
            except:
                self.status=node_statue.end

    def task_check_status(self):
        if self.status in node_statue:

            if self.status is not node_statue.node_error:
                return True
            else:
                return False

        else:
            print("%s is error ,status is not in enum"%self.task_name)
            self.status=node_statue.node_error

            return False

    def task_set_status(self,statue):
        if statue is not node_statue.node_error:
            self.status=statue
        else:
            print("Task_name %s ,set status Error "%self.task_name)

    def task_get_status(self):

        return self.status

    def task_get_name(self):
        return self.name




