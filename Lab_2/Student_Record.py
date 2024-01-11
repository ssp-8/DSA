import csv
EntityArray = []
Students = []
class StudentRecord:
    def __init__(self):
        self.studentName = ""
        self.rollNumber = ""

    def get_studentName(self):
        return self.studentName

    def set_studentName(self, name):
        self.studentName = name

    def get_rollNumber(self):
        return self.rollNumber

    def set_rollNumber(self, rollnum):
        self.rollNumber = rollnum
class Node:
    def __init__(self):
        self.next = None
        self.element = None

    def get_next(self):
        return self.next

    def get_element(self):
        return self.element

    def set_next(self, value):
        self.next = value

    def set_element(self, student):
        self.element = student
class Entity:
    def __init__(self):
        self.name = ""
        self.iterator = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_iterator(self):
        return self.iterator

    def set_iterator(self, iter):
        self.iterator = iter
class LinkedList(Entity):
    def __init__(self,name,s):
        self.set_name(name)
        self.iterator = Node()
        self.iterator.set_element(s)
        self.tail = Node()
        self.tail = self.iterator
    def add_student(self,s):
        s1 = Node()
        self.tail.next = s1
        s1.set_element(s)
        s1.set_next(None)
        self.tail = s1
    def delete_student(self,s):
        flag = 0
        if(self.iterator.get_element().studentName==s):
            self.iterator = self.iterator.get_next()
        else:
            p = Node()
            p = self.get_iterator()
            while(p.next.get_element().studentName!=s):
                p=p.next
            p.next = p.next.next
def read_input_file(filename) :
    with open(filename,'r') as file:
        File = csv.reader(file,delimiter =',')
        j = 0
        for row in File:
            j = j+1
            flag = 0
            i = 0
            s = StudentRecord()
            name = row[0]
            rollnum = row[1]
            department = row[2]
            clubs = []
            courses = []
            s.set_studentName(name)
            s.set_rollNumber(rollnum)
            Students.append(s)
            k = 3
            while(not(']' in row[k])):
                courses.append(row[k])
                k+=1
            courses.append(row[k])
            courses[0] = courses[0].replace('[','')
            courses[len(courses)-1] = courses[len(courses)-1].replace(']','')
            k+=1
            hostel = row[k]
            k+=1
            while(not(']' in row[k])):
                clubs.append(row[k])
                k+=1
            clubs.append(row[k])
            clubs[0] = clubs[0].replace('[','')
            clubs[len(clubs)-1] = clubs[len(clubs)-1].replace(']','')
            if(not(j==1)):
                for i in range(0,len(EntityArray)):
                    if(EntityArray[i].name==department):
                               flag = 1
                               d1 = EntityArray[i]
                               break;
                    else:
                        flag = 0
            if ((flag == 0 or j==1)):
                d1 = LinkedList(department,s)
                EntityArray.append(d1)
            elif(j!=1):
                d1.add_student(s)
            for a in range(0,len(courses)):
                flag  = 0
                if(not(j==1)):
                    for b in range(0,len(EntityArray)):
                        if(EntityArray[b].name==courses[a]):
                                   flag = 1
                                   c1 = EntityArray[b]
                                   break;
                        else:
                            flag = 0
                if ((flag == 0 or j==1)):
                    c1 = LinkedList(courses[a],s)
                    EntityArray.append(c1)
                elif(j!=1or flag == 1):
                    c1.add_student(s)
            if(not(j==1)):
                flag = 0
                for i in range(0,len(EntityArray)):
                    if(EntityArray[i].name==hostel):
                               flag = 1
                               h1 = EntityArray[i]
                               break;
                    else:
                        flag = 0
            if ((flag == 0 or j==1)):
                h1 = LinkedList(hostel,s)
                EntityArray.append(h1)
            elif(j!=1):
                h1.add_student(s)
            for a in range(0,len(clubs)):
                flag  = 0
                if(not(j==1)):
                    for b in range(0,len(EntityArray)):
                        if(EntityArray[b].name==clubs[a]):
                                   flag = 1
                                   cl1 = EntityArray[b]
                                   break;
                        else:
                            flag = 0
                if ((flag == 0 or j==1)):
                    cl1 = LinkedList(clubs[a],s)
                    EntityArray.append(cl1)
                elif(j!=1):
                    cl1.add_student(s)
