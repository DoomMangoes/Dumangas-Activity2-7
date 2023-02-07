import os

class Student():
    
    def __init__(self,studID,firstName,lastName,course,yrLvl):
        self.studID = studID
        self.firstName = firstName
        self.lastName = lastName
        self.course = course
        self.yrLvl = yrLvl

    def willGraduate(self):
        
        if self.yrLvl == '4':
            self.printOut("can graduate")
        else:
            self.isDelayed()
    
    def isDelayed(self):

        if self.yrLvl > '4':
           self.printOut("is delayed")
        elif self.yrLvl < '4':
            self.printOut("is not a 4th year student")

    def hasOOP(self):
        
        output = "has OOP."

        if self.yrLvl != '2':
             output = "does not have OOP."

        self.printOut(output)
        
    def printOut(self,output):

        print ("[" + str(self.studID) + "] " 
                + self.lastName + ", " 
                + self.firstName 
                +" (" + self.course
                + "-" 
                + str(self.yrLvl) + ") " 
                + output)
    
    # Override
    def __str__(self):
        return str(self.studID) + ' ' + self.firstName + ' ' + self.lastName + ' ' + self.course + ' ' + str(self.yrLvl)

          
def enroll(studentList):
   
   #Input Student ID
    while True:

        check = False

        while True:
            try:
                studID = int(input("Enter Student ID:"))
            except:
                print("Student ID must be a number")
                continue
            break

        for tempStudent in studentList:
            if tempStudent.studID == studID:
                check = True
                break

        if check == True:
            print("ID already in use! Input another ID")
            continue  
        else:    
            break 
        
    
    firstName = input("Enter First Name:")
    lastName = input("Enter Last Name:")
    course = input("Enter Course:")

    while True:

        yrLvl = input("Enter Year Level:")

        if yrLvl not in ('1', '2', '3', '4', '5', '6', '7', '8'):
            print("Year Level must be a number between (1-8)")
            continue
        break

    studentList.append(Student(studID, firstName, lastName, course, yrLvl))

    return studentList
       
def printStudentList(studentList):
    
    if not studentList:
        print("Student List Is Empty!")
    else:
        print("Student List\n")

        for element in studentList:
            print(element)

def findStudent(studentList):

    tempStudent = "Not Found"

    #Input Student ID
    while True:
        try:
           studID = int(input("Enter Student ID:"))
        except:
            print("Student ID must be a number")
            continue
        break

    for tempStudent in studentList:
        if tempStudent.studID == studID:
            return tempStudent

    return tempStudent    

def main():
    os.system('cls')

    studentList = []

    while True:

        print("Menu:")
        print("=========================")
        print("1.) Enroll Student")
        print("2.) View Student List")
        print("3.) Will Student Graduate?")
        print("4.) Does Student Have OOP?")
        print("\n")
    
        #take input1
        choice = input("Enter Choice: ")

        #check choice
        if choice in ('1', '2', '3', '4'):

            if choice == '1':
                enroll(studentList)

            elif choice == '2':
                printStudentList(studentList)

            elif choice in ('3', '4'):
                student = findStudent(studentList)

                if student == "Not Found":
                    print("Student Does Not Exist")
                else:

                    if choice == '3':
                        student.willGraduate()
                    elif choice == '4':
                        student.hasOOP()

            
                
            while True:
                check = input("Do you want to do another operation? ([1]Yes/[0]No):")
                
                if check not in ('0','1'):
                    continue
                else:
                    break
            
            if check == '0':
                break
        else:
            print("Invalid Option!")

    


if __name__ == '__main__':
    main();