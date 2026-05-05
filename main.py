from pyscript import display, document

# Lists for pre-existing classmates - Names updated as requested
classmate_list = ["Aria", "Benny", "Cassel", "Dante", "Elara", "Felix"]
section_list = ["Emerald", "Ruby", "Sapphire", "Topaz", "Jade", "Onyx"]
subject_list = ["PE", "Science", "English", "Social Studies", "Filipino", "ICT"]

class Classmate:
        # Gives the attributes of the class
        def __init__(self, name, section, subject):
            self.name = name # Attribute
            self.section = section # Attribute
            self.subject = subject # Attribute

        # Creates the "introduce" function, which is supposed to display each of the students
        def introduce(self):
            display(f"Hi! My name is {self.name}. I am from the section of {self.section}, and my favorite subject is {self.subject}. Nice to meet you!", target="output1")

def showclasslist(e):
    # Leaves the HTML blank at first. 
    document.getElementById("output1").innerHTML = ""

    student = []

    for i in range(len(classmate_list)):
        student.append(Classmate(
            name=classmate_list[i],
            section=section_list[i],
            subject=subject_list[i]
        ))
    
    # Introducing each of the students
    for s in student:
        s.introduce()


def addstudent(e):
    # Append the values to the list
    classmate_list.append(document.getElementById("name").value)
    section_list.append(document.getElementById("sec").value)
    subject_list.append(document.getElementById("subj").value)