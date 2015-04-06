__author__ = 'group-4'

import Storage
from Task import Appointment, Deadline, Unbound
from os import path

class DataContext:

    def __init__(self, task_type='Task'):
        '''
        task_type can be 'Appointment' or 'Deadline' or 'Unbound'.
        If task_type is not given, task_type will be 'Task'

        Appointment -> Appointments.txt
        Deadline    -> Deadlines.txt
        Unbound     -> Unbounds.txt
        Task        -> Tasks.txt
        '''
        self.task_type = task_type
        self.data = []
        self.storage_location = (self.task_type == 'Appointment' and 'Appointments.txt') or \
                                (self.task_type == 'Deadline'    and 'Deadlines.txt')    or \
                                (self.task_type == 'Unbound'     and 'Unbounds.txt')     or 'Tasks.txt'
        self.storage_location = path.join('Data/', self.storage_location)
        self.load()

    def load(self):
        '''
        read the data from text file using Storage class,
        instantiate objects accordingly and store them in a list - self.data
        :return: list of data objects stored in self.data
        '''
        for data in Storage.Storage(self.storage_location).load():
            if self.task_type == 'Appointment':
                task = Appointment(data['id'])
            elif self.task_type == 'Deadline':
                task = Deadline(data['id'])
            elif self.task_type == 'Unbound':
                task = Unbound(data['id'])
            else:
                return
            for k, v in data.items():
                if k != 'id':
                    setattr(task, k, v)
            self.data.append(task)

    def commit_changes(self):
        '''
        save changes made to self.data to text files accordingly.
        This is relatively expensive task - shouldn't overuse
        '''
        Storage.Storage(self.storage_location).save(self.data)

    def get(self, paged=False, skip=0, count=10, sort_by='id', reverse=False):
        '''
        :param paged: True or False - return paged data if True
        :param skip: Number of data objects to skip when paged data are returned
        :param count: Number of data objects to be returned when paged is True
        :param sort_by: Attribute name to use when sorting data
        :param reverse: Sort the data in descending order
        :return: paged and sorted copy of self.data
        '''
        data = sorted(self.data, key=lambda k: getattr(k, sort_by), reverse=reverse)
        if paged:
            skip = len(self.data) - count if skip + count > len(self.data) else skip
            return data[skip:(skip+count)]
        else:
            return data

    def get(self, id):
        '''
        :param id: select an data object using id
        :return: an object with given id
        '''
        return [data for data in self.data if data.id == id][:1]

    def update(self, task):
        '''
        The object data will only be updated in memory.
        It will not be saved to disk until commit_changes is called.
        :param task: an object to be saved
        :return: True if updated successfully
        '''
        for index, data in enumerate(self.data):
            if data.id == task.id:
                task.modified_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.data[index] = task
                return True
        else:
            return False

    def insert(self, task):
        '''
        The object data will only be created in memory.
        It will not be saved to disk until commit_changed is called.
        :param task: an object to be created
        :return:True if created successfully
        '''
        for index, data in enumerate(self.data):
            if data.id == task.id:
                return False
        else:
            task.created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task.modified_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.data.append(task)
            return True

#test codes
if __name__ == '__main__':
    import Task
    import datetime

    dc_appointment = DataContext('Unbound')
    print dc_appointment.data


    ap1 = Task.Appointment();
    ap1.title = 'test appointment'
    dc_appointment.insert(ap1)
    dc_appointment.commit_changes()

    print dc_appointment.data





