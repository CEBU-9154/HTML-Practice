class Robot:
    def __init__(self, name, model, purpose, language):
        self.name=name
        self.model=model
        self.purpose=purpose
        self.language=language

    def introduce(self):
        print(f"Hello! I'm {self.name}.")
        print(f"I'm model {self.model}.")
        print(f"My main purpose is {self.purpose}.")
        print(f"I can communicate in {self.language}.")
r1=Robot("RobotHelper", "RH-101", "assisting with daily tasks", "English")
r2=Robot("MediBot", "YB-202", "medical assistance", "English and Hindi")

print("Robot 1 Introduction: ")
r1.introduce()
print("\nRobot 2 Introduction: ")
r2.introduce()