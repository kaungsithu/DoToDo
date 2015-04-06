__author__ = 'group-4'

class Task(object):

    #a number to keep track of latest available id
    # to be assigned to newly created object
    latest_id = 0

    def __init__(self, id=None, title=None, description=None,
                 status=None, created_date=None, modified_date=None):
        '''
        If an id is not give, it will be created automatically.
        If an id is given and the value is greater than latest_id,
        latest_id will be incremented according to given id
        :param id: a unique number to be assigned to newly created object
        :param title:
        :param description:
        :param status: done or pending
        :param created_date:
        :param modified_date:
        :return:
        '''
        if id:
            self.id = id
            Task.latest_id = id+1 if id >= Task.latest_id else Task.latest_id
        else:
            self.id = Task.latest_id
            Task.latest_id += 1
            self.title = title
            self.description = description
            self.status = status
            self.created_date = created_date
            self.modified_date = modified_date

    def get_latest_id(self):
        return Task.latest_id

class Appointment(Task):

    def __init__(self, id=None, title=None, description=None,
                 status=None, created_date=None, modified_date=None,
                 start_time=None, end_time=None):
            super(Appointment, self).__init__(id, title, description,
                                              status, created_date, modified_date)
            self.start_time = start_time
            self.end_time = end_time


class Deadline(Task):

    def __init__(self, id=None, title=None, description=None,
                 status=None, created_date=None, modified_date=None,
                 by_time=None):
            super(Deadline, self).__init__(id, title, description,
                                              status, created_date, modified_date)
            self.by_time = by_time

class Unbound(Task):

    def __init__(self, id=None, title=None, description=None,
                 status=None, created_date=None, modified_date=None,
                 priority=None):
            super(Unbound, self).__init__(id, title, description,
                                              status, created_date, modified_date)
            self.priority = priority

#test codes
if __name__ == '__main__':
    a = Appointment(1)
