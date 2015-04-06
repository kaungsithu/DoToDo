__author__ = 'group-4'

class Storage:

    def __init__(self, file_location):
        '''file_location -> text file location for storage'''
        self.fl = file_location

    def save(self, objects):
        '''Save the attributes from a list of objects in a text file
           as a list of dictionaries.
           Each dictionary is save as a line for easier editing by an advance user'''
        f = open(self.fl, 'w')
        f.write(str([obj.__dict__ for obj in objects]).replace('},', '}\n'))
        f.close()

    def load(self):
        '''
        Retrieve back the saved strings of dictionaries
        '''
        try:
        #try opening file and evaluate string into list of dictionaries
            f = open(self.fl, 'r')
            content = f.read()
            content = eval(content.replace('\n', ',')) if len(content) > 1 else []
            f.close()
        except:
        #if file can't be opened, most likely the file is not there,
        #return empty list
            content = []
        finally:
            return content

#test codes
if __name__ == '__main__':
    pass