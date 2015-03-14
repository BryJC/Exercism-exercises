from collections import defaultdict, OrderedDict

class School(object):
    
    def __init__(self, school):
        self.school = school
        self.db = defaultdict(set)
        
    def add(self, name, grade):
        self.db[grade].add(name)
            
    def grade(self, key):
        return self.db[key]
            
    def sort(self):
        return OrderedDict({grade: tuple(sorted(names)) for grade, names in (self.db.items())})
        #need OrderedDict in order to guarantee ordered grade as well as names
<<<<<<< HEAD

=======
>>>>>>> b0a6b5a2d94e9b8a7bc751c1b38cfd849a03f8d5