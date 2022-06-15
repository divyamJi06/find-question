class Robot():
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce(self):
        print("My name is ",self.name)
    


class Person():
    def __init__(self,name,personality,issitting):
        self.name = name
        self.personality = personality
        self.issitting = issitting
    def standup(self):
        self.issitting = False
    def sitdown(self):
        self.issitting = True
    def intro(self):
        print(f"My anme is - {self.name}, I'm sitting - {self.issitting}")


r1 = Robot("Tom","Red",30)
r2 = Robot("Jerry","Blue",40)
p1 = Person("Alice","Aggressive",False)
p2 = Person("Becky","Talkative",True)
r1.introduce()
r2.introduce()
p1.intro()
p2.intro()
p1.robot = r2
p2.robot = r1
p1.robot.introduce()