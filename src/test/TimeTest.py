import time

ss = time.time();

print(ss);

class User:
    'User vo'
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        
    def say(self):
        print"hello: my name is ", self.name;
        
user1 = User("kaka", 22);
user1.say();
print(user1.__doc__);
print(user1.__dict__);

content = dir(time);
print(content);

