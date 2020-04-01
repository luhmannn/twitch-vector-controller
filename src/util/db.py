import os
import json 

class DB(object):
    
    # Minimalistic persistance to file

    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self.db = json.load(open(location, "r"))
        else:
            self.db = {}
        return True

    def set(self, key, value):
        self.db[str(key)]= value
        self.save()

    def get(self, key):
        try:
            return self.db[key]
        except KeyError as err:
            print("Can't find value for key: %s" % key)
            return False

    def save(self):
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except Exception as err:
            print('Error saving db to disk: %s' % err)
            return False

    def resetDB(self):
        self.db = {}
        self.save()
        return True
    
    

        
