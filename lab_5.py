# MetroStop class
import csv
lines = []
class MetroStop:
    def __init__(self, name, metro_line, fare):
        self.stop_name = name
        self.next_stop = None
        self.prev_stop = None
        self.line = metro_line
        self.fare = fare

    def get_stop_name(self):
        return self.stop_name

    def get_next_stop(self):
        return self.next_stop

    def get_prev_stop(self):
        return self.prev_stop

    def get_line(self):
        return self.line

    def get_fare(self):
        return self.fare

    def set_next_stop(self, next_stop):
        self.next_stop = next_stop

    def set_prev_stop(self, prev_stop):
        self.prev_stop = prev_stop

# MetroLine class
class MetroLine:
    def __init__(self, name):
        self.line_name = name
        self.stops =[]
        self.node = None

    def get_line_name(self):
        return self.line_name

    def get_node(self):
        return self.node

    def set_node(self, node):
        self.node = node

    def print_line(self):
        stop = self.node
        while stop is not None:
            print(stop.get_stop_name())
            stop = stop.get_next_stop()

    def get_total_stops(self):
        return len(self.stops)

    def populate_line(self, filename):
        with open(filename,'r') as file:
            track = csv.reader(file,delimiter=' ')
            j = 0
            prev = None
            for row in track:
                j+=1
                fare = None
                stop_name = ''
                row[-1]= row[-1].replace(',','')
                fare = (row[-1])
                for i in range(len(row)-1):
                    stop_name+=row[i]
                    if(i!=len(row)-2):
                        stop_name+=' '
                if(j!=1):
                    stop = MetroStop(stop_name,self,fare)
                    stop.set_prev_stop(prev)
                    prev.set_next_stop(stop)
                    prev = stop
                    self.stops.append(stop_name)
                else:
                    stop = MetroStop(stop_name,self.line_name,fare)
                    prev = stop
                    self.node = stop
                    self.stops.append(stop_name)
# AVLNode class
class AVLNode:
    def __init__(self, name):
        self.stop_name = name
        self.stops = []
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
    def get_stop_name(self):
        return self.stop_name

    def get_stops(self):
        return self.stops

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def add_metro_stop(self, metro_stop):
        self.stops.append(metro_stop)

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_parent(self, parent):
        self.parent = parent

# AVLTree class
class AVLTree:
    def __init__(self):
        self.root = AVLNode(None)

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def height(self, node):
        if(node==None):
            return 0
        else:
            return max(self.height(node.left),self.height(node.right))+1
    def string_compare(self, s1, s2):
        if (s1 > s2):
            return 1
        if (s1 == s2):
            return 0
        if (s1 < s2 ):
            return -1
    def find_suitable(self,stop):
        v = AVLNode(None)
        v = self.root
        w = AVLNode(None)
        while(v!=None):
            w = v
            i = self.string_compare(v.stop_name,stop.stop_name)
            if(i==1):
                v = v.left
            elif(i==-1):
                v = v.right
            else:
                v.stops.append(stop)
                return None
        return w
    def balance_factor(self, node):
        if(node!=None):
            a = self.height(node.left)
            b = self.height(node.right)
            return a-b
        return "Not"
    def rotate_left(self, node):
        p = node.parent
        y = node.right
        t = y.left
        #if(node.stop_name=="Dwarka Sec-12"):
        #    print(p.stop_name)
        y.left = node
        y.parent = p
        node.parent = y
        node.right = t
        if(t!=None):
            t.parent = node
        if(y.parent==None):
            self.root = y
        else:
            if(y.parent.stop_name>y.stop_name):
                y.parent.left = y
            else:
                y.parent.right = y
    def rotate_right(self, node):
        p = node.parent
        y = node.left
        t = y.right
        y.right = node
        y.parent = p
        node.left = t
        if(t!=None):
            t.parent = node
        node.parent = y
        if(y.parent==None):
            self.root = y
        else:
            if(y.parent.stop_name>y.stop_name):
                y.parent.left = y
            else:
                y.parent.right = y
    def double_rotate(self,node,case):
        if(case ==1):
            self.rotate_left(node.left)
            self.rotate_right(node)
        else:
            self.rotate_right(node.right)
            self.rotate_left(node)
    def balance(self, node):
        z = None
        y = None
        x = node
        flag = 0
        a = 0
        while(x.parent!=None):
            y = x.parent
            z = x.parent.parent
            a = self.balance_factor(z)
            l = [-1,0,1]
            if(a!="Not" and a not in l):
                flag = 1
                break
            else:
                x = x.parent
        if(flag == 1):
            if(y == z.left and x== y.left):
                self.rotate_right(z)
            elif(y == z.right and x == y.right):
                self.rotate_left(z)
            elif(y== z.left and x  == y.right):
                self.double_rotate(z,1)
            elif(y==z.right and x == y.left):
                self.double_rotate(z,2)
                
    def insert(self, node, metro_stop):
        if(self.root.stop_name==None):
            self.root = node
            #print(self.root.stop_name,self.height(self.root))
            return True
        Node  = self.find_suitable(metro_stop)
        if(Node!=None):
            i = self.string_compare(Node.stop_name,node.stop_name)
            if(i==1):
                Node.set_left(node)
            else:
                Node.set_right(node)
            node.set_parent(Node)
            node.stops.append(metro_stop)
            self.balance(node)
            #print(self.root.stop_name, node.stop_name,self.get_total_nodes(self.root))
    def populate_tree(self, metro_line):
        current = metro_line.node
        while(current!=None):
            Node = AVLNode(current.stop_name)
            self.insert(Node,current)
            current = current.next_stop
    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.get_left())
        print(node.get_stop_name())
        self.in_order_traversal(node.get_right())

    def get_total_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.get_total_nodes(node.get_left()) + self.get_total_nodes(node.get_right())

    def search_stop(self, stop_name):
        w = AVLNode(None)
        w = self.root
        while(w!=None):
            if(w.stop_name>stop_name):
                w =w.left
            elif(w.stop_name<stop_name):
                w = w.right
            else:
                return w

# Trip class
class Trip:
    def __init__(self, metro_stop, previous_trip):
        self.node = metro_stop
        self.prev = previous_trip
        self.type = None
        self.start_node = metro_stop
    def get_node(self):
        return self.node

    def get_prev(self):
        return self.prev

# Exploration class
class Exploration:
    def __init__(self):
        self.trips = []
        self.visited = []

    def get_trips(self):
        return self.trips

    def enqueue(self, trip):
        self.trips.append(trip)

    def dequeue(self):
        if not self.trips:
            return None
        trip = self.trips.pop(0)
        print("Dequeued:", trip.get_node().get_stop_name())
        return trip

    def is_empty(self):
        return not bool(self.trips)

# Path class
class Path:
    def __init__(self):
        self.stops = []
        self.total_fare = int(0)

    def get_stops(self):
        return self.stops

    def get_total_fare(self):
        return self.total_fare

    def add_stop(self, stop):
        self.stops.append(stop)

    def set_total_fare(self, fare):
        self.total_fare = fare

    def print_path(self):
        for stop in self.stops:
            print(stop.get_stop_name())

# PathFinder class
class PathFinder:
    def __init__(self, avl_tree, metro_lines):
        self.tree = avl_tree
        self.lines = metro_lines

    def get_tree(self):
        return self.tree

    def get_lines(self):
        return self.lines

    def create_avl_tree(self):
        self.tree = AVLTree()
        for i in self.lines:
            self.tree.populate_tree(i)
            
    def modify_prev_trip(self,current_trip):
        for i in self.lines:
            k = 0
            if(i==current_trip.prev.node.line):
                node = i.node
                while(node.next_stop!=None):
                    if(node.stop_name==current_trip.node.stop_name):
                        if(current_trip.prev.type == -1):
                            current_trip.prev.node = node.next_stop
                            k = 1
                            break
                        else:
                            current_trip.prev.node = node.prev_stop
                            k = 1
                            break

                    node = node.next_stop
            if(k==1):
                return current_trip
    def back_trace(self,trip):
        path = Path()
        current_trip = trip
        while(current_trip!=None):
            start_fare = int(current_trip.node.fare)
            while(current_trip.node!=current_trip.start_node):
                path.stops.append(current_trip.node)
                if(current_trip.type == 1):
                    current_trip.node = current_trip.node.prev_stop
                elif(current_trip.type == -1):
                    current_trip.node = current_trip.node.next_stop
            path.stops.append(current_trip.node)
            final_fare = int(current_trip.node.fare)
            path.total_fare+=max(final_fare,start_fare)-min(final_fare,start_fare)
            if(current_trip.prev!=None):
                    current_trip = self.modify_prev_trip(current_trip)
            current_trip = current_trip.prev
            if(current_trip!=None):
                if(current_trip.node.next_stop!=None):
                    path.total_fare+=(int(current_trip.node.next_stop.fare)-int(current_trip.node.fare))
                else:
                    path.total_fare+=(int(current_trip.node.fare)-int(current_trip.node.prev_stop.fare))
        return path
        
    def find_path(self, origin, destination):
        paths = []
        exp = Exploration()
        path = Path()
        flag = 0
        start = self.tree.search_stop(origin)
        if(start==None):
            print("Such station doesn't exist")
            return None
        for i in range(0,len(start.stops)):
            trip2f = Trip(start.stops[i],None)
            trip2b = Trip(start.stops[i],None)
            trip2f.type = 1
            trip2b.type = -1
            exp.enqueue(trip2f)
            exp.enqueue(trip2b)
            exp.visited.append(trip2f.node.line)
        while(exp.trips!=[]):
            trip = exp.trips[0]
            while(trip.node!=None):
                stop = self.tree.search_stop(trip.node.stop_name)
                if(stop.stop_name == destination):
                    path = self.back_trace(trip)
                    paths.append(path)
                    break
                if(len(stop.stops)>1 and stop.stop_name!=origin):
                    for i in stop.stops:
                        if(i.line not in exp.visited):
                            trip3f = Trip(i,trip)
                            trip3f.type = 1
                            trip3b = Trip(i,trip)
                            trip3b.type = -1
                            exp.enqueue(trip3f)
                            exp.enqueue(trip3b)
                            exp.visited.append(trip3f.node.line)
                if(trip.type==1):
                    if(trip.node.get_next_stop()==None):
                        break
                    trip.node = trip.node.get_next_stop()
                else:
                    if(trip.node.get_prev_stop()==None):
                        break
                    trip.node = trip.node.get_prev_stop()
            if(flag == 0):
                exp.dequeue()
        for i in paths:
            stop_length = 1000000000
            if(len(i.stops) <= stop_length):
                path = i
                stop_length = len(i.stops)
        return path
