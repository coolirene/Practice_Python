# Class and Inheritance

# Super Class - Mogakko
class Mogakko:
    # initialization
    name = ''
    cName = ''
    session = ''
    # Constructor - name, course, session
    def __init__(self, memberName, className, attendingSession):
        self.name = memberName
        self.cName = className
        self.session = attendingSession
    
    def showName(self): # Display name
        print(self.name)
    
    def showClass(self): # Display Course
        print(self.cName)

    def showSession(self): # Display session
        print(self.session) 

    
# Sub-Class - Manager
class Manager(Mogakko):
    managerId = '' # added variable in this Class
    # Initializing of Manager Class
    def __init__(self, managerName, managerClass, managerSession, managerId):
        # Call the Mogakko Class (Super Class)
        Mogakko.__init__(self, managerName, managerClass, managerSession)
        self.managerId = managerId # Assigned managerId
    # return managerId Value
    def getId(self):
        return self.managerId


# Create Mogakko Obj & Call a member method to Display the Name
print()
manager1 = Mogakko('KoMyu', 'C', '1') 
manager1.showName() 
print()
# Create Manager Obj & Display Id added in this Class
manager2 = Manager('YoungTak', 'Python Basic', '1', '201')
print(manager2.getId())
manager2.showName() # Display Manager Name - Overriding
print()
        