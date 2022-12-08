class dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

>> > my_dog = dog("phoebe", 10)

>> > my_dog.name
'phoebe'

# delete attribute
>> > del my_dog.name

>> > my_dog.name
Traceback(mostrecentcalllast):
File
"<pyshell#77>", line
1, in < module >
my_dog.name
AttributeError: 'dog'
object
has no attribute
'name'