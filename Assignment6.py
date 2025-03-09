# Question 1: Course Management System
class Course:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits

    def display(self):
        return f"{self.code} - {self.name} ({self.credits} credits)"

class CoreCourse(Course):
    def __init__(self, code, name, credits, required):
        super().__init__(code, name, credits)
        self.required = required

class ElectiveCourse(Course):
    def __init__(self, code, name, credits, elective_type):
        super().__init__(code, name, credits)
        self.elective_type = elective_type

# Example usage
core = CoreCourse("CS101", "Intro to CS", 3, True)
elective = ElectiveCourse("HIST202", "World History", 2, "Liberal Arts")

print(core.display())
print(elective.display())
