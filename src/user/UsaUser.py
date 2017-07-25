class UsaUser:
    'usa user';

    def __init__(self, name):
        self.name = name;

    def sayHello(self, str) :
        print "my name is ", self.name, " ", str


u = UsaUser("java");
u.sayHello("kava");

print type(u);
print dir(u);