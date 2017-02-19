class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)

# Create class Child which inherits from class Parent
class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Number of toys - "+str(self.number_of_toys))

# Note - Normally class definitions and general programs should
# be in separate files.  This is done for illustrative convenience:
billy_cyrus = Parent('Cyrus','blue')
#print(billy_cyrus.last_name)
billy_cyrus.show_info()

miley_cyrus = Child('Cyrus','blue',5)
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)
# Call of method show_info via inheritance (if no show_info in Child)
# Also shows show_info in Child which overrides/shadows Parent version
miley_cyrus.show_info()

