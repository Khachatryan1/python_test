import  json
from random import randint as rd,choice as ch
from pprint import pprint


def write(data,filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open (filename,'w',encoding='utf-8') as file:
        json.dump(data,file,indent=4)

def read(filename):
    with open (filename,'r',encoding='utf-8') as file:
        return json.load(file)

class User:
    def __init__(self):
        self.name = ch(['bob','boni','mikhael','leo'])
        self.age = rd(0,100)
        self.id = rd(10,100000)
        self.number = ch(['first','second','third'])

data = {
    'users' : []
}

for i in range(100):
    data['users'].append(User().__dict__)
pprint(data)

write(data,'test.json')



