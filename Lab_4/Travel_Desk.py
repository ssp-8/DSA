import csv
class Vehicle:
    def __init__(self, vehicle_number, seating_capacity):
        self.vehicle_number = vehicle_number
        self.seating_capacity = int(seating_capacity)
        self.trips = []

    def get_vehicle_number(self):
        return self.vehicle_number

    def set_vehicle_number(self, new_vehicle_number):
        self.vehicle_number = new_vehicle_number

    def get_seating_capacity(self):
        return self.seating_capacity

    def set_seating_capacity(self, new_seating_capacity):
        self.seating_capacity = new_seating_capacity

    def get_trips(self):
        return self.trips

    def add_trip(self, trip):
        self.trips.append(trip)
###############################################################################

class Trip:
    def __init__(self, vehicle, pick_up_location, drop_location, departure_time):
        self.vehicle = vehicle
        self.pick_up_location = pick_up_location
        self.drop_location = drop_location
        self.departure_time = departure_time
        self.booked_seats = 0

    def get_vehicle(self):
        return self.vehicle

    def get_pick_up_location(self):
        return self.pick_up_location

    def set_pick_up_location(self, new_pick_up_location):
        self.pick_up_location = new_pick_up_location

    def get_drop_location(self):
        return self.drop_location

    def set_drop_location(self, new_drop_location):
        self.drop_location = new_drop_location

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_booked_seats(self):
        return self.booked_seats

    def set_booked_seats(self, new_booked_seats):
        self.booked_seats = new_booked_seats
###############################################################################

class Location:
    def __init__(self, name, service_ptr=None):
        self.name = name
        self.service_ptrs = []
        self.trips = []

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_service_ptr(self,drop_location):
        for i in self.service_ptrs:
            if i.get_location_ptr().get_name()==drop_location:
                return i

    def set_service_ptr(self,drop_location):
        j  = 0
        for i in self.service_ptrs:
            if(i.get_location_ptr().get_name()==drop_location):
                j = 1
                print("The transport Service you are trying to add already exists")
                break
        if(j==0):
            drop = Location(drop_location)
            drop = TransportService(drop_location,drop)
            self.service_ptrs.append(drop)

    def add_trip(self, trip):
        d = BinaryTreeNode(None,None,None)
        if trip.get_pick_up_location() != self.name:
            return
        else:
            self.trips.append(trip)
        j = 0
        if(self.service_ptrs!=None):
            for i in self.service_ptrs:
                if(i.get_location_ptr().get_name()==trip.drop_location):
                    i.add_trip(trip.departure_time,trip)
                    j = 1
                    break
        if(j==0 or self.service_ptrs==None):
            drop = Location(trip.drop_location)
            drop = TransportService(drop)
            self.service_ptrs.append(drop)
            drop.add_trip(trip.departure_time,trip)
        return d
###############################################################################

class BinaryTreeNode:
    def __init__(self, departure_time=0, trip_node_ptr=None, parent_ptr=None):
        self.left_ptr = None
        self.right_ptr = None
        self.parent_ptr = parent_ptr
        self.departure_time = departure_time
        self.trip_node_ptr = trip_node_ptr

    def get_left_ptr(self):
        return self.left_ptr

    def set_left_ptr(self, new_left_ptr):
        self.left_ptr = new_left_ptr

    def get_right_ptr(self):
        return self.right_ptr

    def set_right_ptr(self, new_right_ptr):
        self.right_ptr = new_right_ptr

    def get_parent_ptr(self):
        return self.parent_ptr

    def set_parent_ptr(self, new_parent_ptr):
        self.parent_ptr = new_parent_ptr

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_trip_node_ptr(self):
        return self.trip_node_ptr

    def set_trip_node_ptr(self, new_trip_node_ptr):
        self.trip_node_ptr = new_trip_node_ptr
    def delete_leaf(self):
        if(self.parent_ptr.left_ptr==self):
            self.parent_ptr.left_ptr=None
        else:
            self.parent_ptr.right_ptr=None
    def delete_one_child(self):
        if(self.parent_ptr==None):
            if(self.left_ptr==None):
                self.trip_node_ptr=self.right_ptr.trip_node_ptr
                self.departure_time = self.right_ptr.departure_time
            else:
                self.trip_node_ptr=self.left_ptr.trip_node_ptr
                self.departure_time = self.left_ptr.departure_time
        elif(self.left_ptr==None):
            if(self.parent_ptr.left_ptr==self):
                self.parent_ptr.left_ptr=self.right_ptr
            else:
                self.parent_ptr.right_ptr=self.right_ptr
        else:
            if(self.parent_ptr.left_ptr==self):
                self.parent_ptr.left_ptr=self.left_ptr
            else:
                self.parent_ptr.right_ptr=self.left_ptr
        
###############################################################################

class BinaryTree:
    def __init__(self):
        self.root = BinaryTreeNode(None,None)
        
    def get_height(self,node):
        if(node==None):
            return 0
        else:
            h = self.get_height(node.left_ptr)
            h2 = self.get_height(node.right_ptr)
        return 1+max(h,h2)

    def get_number_of_nodes(self,node):
        if(node==None):
            return 0
        else:
            return 1+self.get_number_of_nodes(node.left_ptr)+self.get_number_of_nodes(node.right_ptr)
            
###############################################################################

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def get_element_with_minimum_key(self):
        w = None
        v = None
        while(v!=None):
            w = v
            v = v.get_left_ptr()
        return w

    def get_element_with_maximum_key(self):
        w = None
        v = self.root
        while(v!=None):
            w = v
            v = v.get_right_ptr()
        return w
    
    def search_suitable(self,key):
        w = BinaryTreeNode(None,None)
        v = self.root
        while(v!=None):
            w = v
            if(v.departure_time>key):
                v = v.left_ptr
            else:
                v = v.right_ptr
        return w
    
    def search_node_with_key(self, key):
        w = BinaryTreeNode(None,None)
        v = self.root
        while(v!=None):
            w = v
            if(v.departure_time>key):
                v = v.left_ptr
            elif(v.departure_time<key):
                v = v.right_ptr
            else:
                return w
        return w
    
    def get_successor_node(self, node):
        root = BinaryTreeNode(None,None)
        w = node.get_right_ptr()
        v = None
        if(node==self.get_element_with_maximum_key()):
            print("No successor to this")
            return
        root = node.parent_ptr
        if(w==None):
            while(root!=None):
                v = root
                if(root.departure_time>=node.departure_time):
                    return root
                else:
                    root = root.parent_ptr
            return v
        else:
            while(w!=None):
                root = w
                w = w.get_left_ptr()
            return root
        
    def get_predecessor_node(self, node):
        root = BinaryTreeNode(None,None)
        w = node.get_left_ptr()
        if(node==self.get_element_with_minimum_key()):
            return node
        root = node.parent_ptr
        if(w==None):
            while(root!=None):
                v = root
                if(root.departure_time<node.departure_time):
                    return root
                else:
                    root = root.parent_ptr
            return v
        else:
            while(w!=None):
                root = w
                w = w.get_right_ptr()
            return root
###############################################################################
        
class TransportService:
    def __init__(self, location_ptr=None, bst_head=None):
        self.location_ptr = location_ptr
        self.bst_head = BinaryTreeNode(None,None)
        self.bst = BinarySearchTree()
        self.bst.root = self.bst_head

    def get_location_ptr(self):
        return self.location_ptr

    def set_location_ptr(self, new_location_ptr):
        self.location_ptr = new_location_ptr

    def get_bst_head(self):
        return self.bst_head

    def set_bst_head(self, new_bst_head):
        self.bst_head = new_bst_head

    def add_trip(self, key, trip):
        node = BinaryTreeNode(None,None)
        if(self.bst_head.trip_node_ptr==None):
            self.bst_head.set_trip_node_ptr(trip)
            self.bst_head.set_departure_time(key)
            node = self.bst_head
            return self.bst_head
        else:
            node = self.bst.search_suitable(key)
            Node = BinaryTreeNode(key,trip,node)
            if(node.departure_time>=Node.departure_time):
                node.set_left_ptr(Node)
            else:
                node.set_right_ptr(Node)
            return Node.parent_ptr
    def delete_trip(self,key):
        node = self.bst.search_node_with_key(key)
        if(node.left_ptr==None and node.right_ptr==None):
            node.delete_leaf()
            
        elif(node.right_ptr==None or node.left_ptr==None):
            node.delete_one_child()
            
        else:
            Node = self.bst.get_sucessor_node(node)
            node.trip_node_ptr=Node.trip_node_ptr
            node.departure_time=Node.departure_time
            if(Node.left_ptr==None and Node.right_ptr==None):
                Node.delete_leaf()
            else:
                Node.delete_one_child()
################################################################################
class TravelDesk:
    def __init__(self):
        self.vehicles = []
        self.locations = []

    def add_trip(self, vehicle_number, seating_capacity, pick_up_location, drop_location, departure_time):
        location = Location(None)
        vehicle = Vehicle(None,0)
        j = 0
        if (self.vehicles!=[]):
            for i in self.vehicles:
                if(i.vehicle_number==vehicle_number):
                    vehicle = i
                    j = 1
                    break
                else:
                    j = 0
        if(j==0 or self.vehicles==[]):
            v = Vehicle(vehicle_number,seating_capacity)
            vehicle = v
            self.vehicles.append(vehicle)
        trip = Trip(vehicle,pick_up_location,drop_location,departure_time)
        vehicle.trips.append(trip)
        j = 0         
        if(self.locations!=[]):
            for i in self.locations:
                if(i.get_name()==trip.pick_up_location):
                    location = i
                    j=1
                    break
                else:
                    j = 0
        if(j==0 or self.locations==[]):
            l = Location(pick_up_location)
            location = l
            self.locations.append(location)
        return location.add_trip(trip)

    def show_trips(self, pick_up_location, after_time, before_time):
        pick = None
        show = []
        node_show=[]
        if(after_time>before_time):
            t = after_time
            after_time = before_time
            before_time = t
        if(self.locations!=[]):
            for i in self.locations:
                if(i.get_name()==pick_up_location and i.service_ptrs!= None):
                    pick = i.service_ptrs
                    break
        if(not pick or self.locations==[]):
            print("No such trips exists in the time interval shown")
            return show
        for i in pick:
            node = i.bst.search_node_with_key(after_time)
            show.append(node.trip_node_ptr)
            node_show.append(node)
            while(node!=None and node.departure_time<before_time):
                node = i.bst.get_successor_node(node)
                if(node not in node_show and node!=None and node.departure_time<before_time):
                    show.append(node.trip_node_ptr)
                    node_show.append(node)
        del node_show
        return show
    def show_tripsbydestination(self, pick_up_location, destination,after_time, before_time):
        pick = Location(None,None)
        show = []
        if(after_time>before_time):
            t = after_time
            after_time = before_time
            before_time = t
        if(self.locations!=[]):
            for i in self.locations:
                if(i.get_name()==pick_up_location and i.service_ptrs!= None):
                    pick = i.service_ptrs
                    break
        if(not pick or self.locations==[]):
            print("No such trips exists in the time interval shown")
            return show
        for i in pick:
            if(i.get_location_ptr().get_name()==destination):
                node = i.bst.search_node_with_key(after_time)
                show.append(node.trip_node_ptr)
                while(node!=None and node.departure_time<before_time):
                    node = i.bst.get_successor_node(node)
                    if(node not in show and node!=None and node.departure_time<before_time):
                        show.append(node.trip_node_ptr)
                break
        return show

    def book_trip(self, pick_up_location, drop_location, vehicle_number, departure_time):
        vehicle = None
        location = None
        trip = None
        flag = 0
        for i in self.vehicles:
            if(i.vehicle_number==vehicle_number):
                vehicle = i
                break
        if(vehicle!=None):
            for i in vehicle.trips:
                if(i.get_pick_up_location()==pick_up_location
                   and i.get_drop_location()==drop_location
                   and i.departure_time == departure_time):
                    if(i.get_booked_seats()<=vehicle.seating_capacity):
                        i.booked_seats+=1
                        trip = i
                    if(i.booked_seats>vehicle.seating_capacity):
                        print("Maximum capacity reached, no more seats available")
                        flag = 1
                        vehicle.trips.remove(i)
                        break
                    
            if(flag==1):
                for j in self.locations:
                    if(j.get_name()==pick_up_location):
                        for i in j.service_ptrs:
                            if(i.get_location_ptr().get_name()==drop_location):
                                i.service_ptr.delete_trip(departure_time)
                                break
            return trip
    def read_input_file(self,filename):
        with open(filename,'r') as File:
            my_file = csv.reader(File,delimiter=' ')
            for row in my_file:
                operation = row[0]
                if(operation == "ADDTRIP"):
                    i = (self.add_trip(row[1],row[2],row[3],row[4],row[5]))
                   # print(i.trip_node_ptr.vehicle.vehicle_number)
                elif (operation =="SHOWTRIPS"):
                    (self.show_trips(row[1],row[2],row[3]))
                elif operation =="BOOKTRIP":
                   (self.book_trip(row[1],row[2],row[3],row[4]))
                elif operation =="SHOWTRIPSBYDESTINATION":
                    self.show_tripsbydestination(row[1],row[2],row[3],row[4])
