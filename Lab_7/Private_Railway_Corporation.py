import csv

# from scratch max heap
class MaxHeap:
    def __init__(self):
        self.array = [1000000000]
    def parent(self, i):
        if(i%2==0):
            return int(i/2)
        else:
            return int((i-1)/2)

    def left(self, i):
        return int(2*i)

    def right(self, i):
        return int(2*i + 1)
    
    def get_max(self):
        return self.array[1]
    
    def extract_max(self):
        if(len(self.array)==1):
            return False
        max_item = self.array[1]
        self.array[1] = self.array[len(self.array)-1]
        self.array.pop(len(self.array)-1)
        i = 1
        maximum = None
        #if(len(self.array)> 2):
            #print(self.array)
        left  = self.left(i)
        right = self.right(i)
        #print((left),right,(len(self.array)))
        if(left <= len(self.array)-1 and right <= len(self.array)-1):
            
            if(self.array[left].priority>self.array[right].priority):
                maximum = left
            else:
                maximum = right
        elif(left <len(self.array)-1):
            maxmimum = left
        elif(right <len(self.array)-1):
            maximum = right
        else:
            return max_item
        if(left<len(self.array)-1 or right<len(self.array)-1):
            while(self.array[i].priority<self.array[maximum].priority):
                    temp = self.array[maximum]
                    self.array[maximum] = self.array[i]
                    self.array[i] = temp
                    i = maximum
                    left = self.left(i)
                    right = self.right(i)
                    if(left <len(self.array)-1 and right <len(self.array)-1):    
                        if(self.array[left].priority>self.array[right].priority):
                            maximum = left
                        else:
                            maximum = right
                    elif(left <len(self.array)-1):
                        maxmimum = left
                    elif(right <len(self.array)-1):
                        maximum = right
                    else:
                        return max_item

        return max_item
    
    def max_heapify(self, i):
        while(self.parent(i)!=0 and self.array[self.parent(i)].priority<self.array[i].priority):
            temp = self.array[self.parent(i)]
            self.array[self.parent(i)] = self.array[i]
            self.array[i] = temp
            i = self.parent(i)
    
    def insert(self, item):
        self.array.append(item)
        
        self.max_heapify(len(self.array)-1)

    def is_empty(self):
        if(len(self.array)==1):
            return True
        else:
            return False


class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []


    def add_edge(self, source, destination, min_freight_cars_to_move, max_parcel_capacity):
        src = None
        dest = None

        if(self.vertices == None or source not in self.vertices.keys()):
            v = Vertex(source,min_freight_cars_to_move,max_parcel_capacity)
            self.vertices[source] = v
        
        if(destination not in self.vertices.keys()):
            u = Vertex(destination,min_freight_cars_to_move,max_parcel_capacity)
            self.vertices[destination] = u
       
        src = self.vertices[source]
        dest = self.vertices[destination]
        src.add_neighbor(dest)
        dest.add_neighbor(src)
        self.edges.append([src,dest])

            
    def print_graph(self): 
        pass

    def bfs(self, source, destination):
        path = []
        path2 = []
        
        for v in self.vertices.values():
            v.bfs_label = 0
            v.bfs_parent = None
        if(self.vertices[source]):
            path = self.bfs_specific(self.vertices[source],destination)
        if(path):
            path.reverse()
            for i in path:
                path2.append(i.name)
        return path2    
        
    
    def bfs_specific(self,v,destination):
        path = []
        queue = []
        flag = 0
        
        queue.append(v)
        while(queue):
            for n in queue[0].neighbors:
                
                if(n.bfs_label == 0 and n.name != destination):
                    if(n.bfs_parent==None):
                        n.bfs_parent = queue[0]
                    queue.append(n)
                    #print(n.name, n.bfs_parent.name)
                elif(n.name == destination):
                    
                    n.bfs_parent = queue[0]
                    #print(n.name, n.bfs_parent.name)
                    flag = 1
                    break
            if(flag == 1):
                break
            else:
                queue[0].bfs_label = 1
                queue.pop(0)     
        if(flag ==1):
            #print(n.name)
            while(n!=None):
                path.append(n)
                n = n.bfs_parent
        return path

        
    def dfs(self, source, destination):
        path = []
        path2 = []
        for v in self.vertices.values():
            v.dfs_label = 0
        if(self.vertices[source]):
            path = self.dfs_specific(self.vertices[source],destination,path)
        if(path):
            path.append(self.vertices[source])
            path.reverse()
            for i in path:
                path2.append(i.name)
        return path2
    
    def dfs_specific(self,v,destination,path):
        v.dfs_label = 1
        neigh = []
        for i in v.neighbors:
            neigh.append(i.name)
        #print(v.name, neigh)
        for n in v.neighbors:
            if(n.dfs_label == 0 and n.name != destination):
                path = self.dfs_specific(n,destination,path)
                #print("out of recursion")
                #print(v.name)
            if(n.name == destination or path!= []):
                path.append(n)
                return path
        return path

    def groupFreightCars(self):
        for vertex in self.vertices.values():
            cars = []
            reached = []
            to_delete = []
            flag1 = 0
            flag2 = 0
            for car in vertex.freight_cars:
                if(car.destination_city!=vertex.name):
                    cars.append(car)
                else:
                    reached.append(car)
            for car in reached:
                for parcel in car.parcels:
                    parcel.delivered = True
                    parcel.current_location = vertex.name
                    
                vertex.freight_cars.remove(car)
            
            for car in cars:
                if(car.can_move()):
                    car.bfs_path = self.bfs(vertex.name,car.destination_city)
                    
                    for node in car.traversed_path:
                        if(node in car.bfs_path):
                           
                            flag1 =1
                            break
                    if(flag1==0):
                        if(not vertex.trains_to_move):
                            vertex.trains_to_move[car.bfs_path[1]] = [car]
                        else:
                            if(car.bfs_path[1] in vertex.trains_to_move.keys()):
                                vertex.trains_to_move[car.bfs_path[1]].append(car)
                            else:
                                vertex.trains_to_move[car.bfs_path[1]] = [car]
                    
            for i in vertex.trains_to_move.keys():
                if(len(vertex.trains_to_move[i])>=vertex.min_freight_cars_to_move):
                    for k in vertex.trains_to_move[i]:
                        k.sealed= True
                        vertex.sealed_freight_cars.append(k)
                else:
                    for k in vertex.trains_to_move[i]:
                        vertex.not_done_cars.append(k)
                    to_delete.append(i)
            
            #print(vertex.name,to_delete)
            for train in to_delete:
                del vertex.trains_to_move[train]
                   
            to_delete = []
            for car in vertex.not_done_cars:
                car.dfs_path = self.dfs(vertex.name,car.destination_city)
                for node in car.traversed_path:
                    if(node in car.dfs_path):
                        flag2 = 1
                        break
                if(flag2==0):
                    if(car.dfs_path[1] in vertex.trains_to_move.keys()):
                        vertex.trains_to_move[car.dfs_path[1]].append(car)
                    else:
                        vertex.trains_to_move[car.dfs_path[1]] = [car]
            for i in vertex.trains_to_move.keys():
                if(len(vertex.trains_to_move[i])>=vertex.min_freight_cars_to_move):
                    for k in vertex.trains_to_move[i]:
                        k.sealed= True
                        vertex.sealed_freight_cars.append(k)
                else:
                    to_delete.append(i)
            
            for train in to_delete:
                del vertex.trains_to_move[train]
            vertex.not_done_cars = []
        

    def moveTrains(self):
        for vertex in self.vertices.values():
            vertex.move_train()
        for vertex in self.vertices.values():
            for stop in vertex.trains_to_move.keys():
                for car in vertex.trains_to_move[stop]:
                    self.vertices[stop].freight_cars.append(car)            
            vertex.trains_to_move = {}
        return


class Vertex:
    def __init__(self, name, min_freight_cars_to_move, max_parcel_capacity):


        self.name = name
        self.freight_cars = []
        self.current_parcels = []
        self.neighbors = []
        self.bfs_label = int(0)
        self.dfs_label = int(0)
        self.bfs_parent = None
        self.trains_to_move = {}
        self.min_freight_cars_to_move = min_freight_cars_to_move
        self.max_parcel_capacity = max_parcel_capacity
        self.parcel_destination_heaps = {}
        self.sealed_freight_cars = []
        self.not_done_cars = []
        
        self.all_parcels = []
        
    def move_train(self):
    
        #print(self.name,self.trains_to_move)
        #for car in self.freight_cars:
            #print(car.parcels[0].origin.name,car.destination_city)

        to_remove = []
        for stop in self.trains_to_move.keys():
            for car in self.trains_to_move[stop]:
                car.move(stop)
                to_remove.append(car)
        for car in to_remove:
            self.freight_cars.remove(car)
        self.clean_unmoved_freight_cars()
        
        
    def add_neighbor(self, neighbor):
        if(neighbor not in self.neighbors):
            self.neighbors.append(neighbor)
            return True
    def add_parcel(self,parcel):
        if(parcel not in self.all_parcels):
            self.all_parcels.append(parcel)
        
    def get_all_current_parcels(self):
        return self.current_parcels
    
    def clean_unmoved_freight_cars(self):
        cars = []
        for car in self.freight_cars:
            if(car.sealed==False):
                cars.append(car)
                parcels = car.parcels
                destination = car.destination_city
                for parcel in parcels:
                    self.parcel_destination_heaps[destination].insert(parcel)
        for car in cars:
            self.freight_cars.remove(car)


            
    def loadParcel(self, parcel):
        heap = None
        if(self.parcel_destination_heaps is None or parcel.destination not in self.parcel_destination_heaps.keys()):
            heap = MaxHeap()
            self.parcel_destination_heaps[parcel.destination] = heap
        else:
            heap = self.parcel_destination_heaps[parcel.destination]
        
        heap.insert(parcel)
        if(parcel not in self.current_parcels):
            self.current_parcels.append(parcel)


    def loadFreightCars(self):
        for i in self.parcel_destination_heaps.keys():
            parcels = []
            arr = self.parcel_destination_heaps[i]
            while(len(arr.array)!=1):
                parcels.append(arr.extract_max())
            for j in range (int(len(parcels)/self.max_parcel_capacity)): 
                f_car = FreightCar(self.max_parcel_capacity)
                f_car.destination_city = i
                f_car.current_location = self.name
                self.freight_cars.append(f_car)        
                a = 0
                while(a!=f_car.max_parcel_capacity and parcels):
                    f_car.load_parcel(parcels.pop(0))
                    a+=1
        
        
        return    


    def print_parcels_in_freight_cars(self):
        # optional method to print parcels in freight cars
        pass
        

class FreightCar:
    def __init__(self, max_parcel_capacity):

        self.max_parcel_capacity = max_parcel_capacity
        self.parcels = []
        self.destination_city = None
        self.next_link = None
        self.current_location = None
        self.sealed = False
        self.bfs_path = []
        self.dfs_path = []
        self.traversed_path = []

    def load_parcel(self, parcel):
        self.parcels.append(parcel)

    def can_move(self):
        
        if(len(self.parcels)==self.max_parcel_capacity):
            return True
        else:
            return False
        
    def move(self, destination):
    
        parcels_reached = []
        self.traversed_path.append(self.current_location)
        self.current_location = destination
        for parcel in self.parcels:
            parcel.current_location = destination
            
        return parcels_reached
                



class Parcel:
    def __init__(self, time_tick, parcel_id, origin, destination, priority):
        self.time_tick = time_tick
        self.parcel_id = parcel_id
        self.origin = origin
        self.destination = destination
        self.priority = priority
        self.delivered = False
        self.current_location = origin

class PRC:
    def __init__(self, min_freight_cars_to_move=5, max_parcel_capacity=5):
        self.graph = Graph()
        self.freight_cars = []
        self.parcels = {}
        self.parcels_with_time_tick = {}
        self.min_freight_cars_to_move = min_freight_cars_to_move
        self.max_parcel_capacity = max_parcel_capacity
        self.time_tick = 1
        self.old_state = []
        self.new_state = []
        self.max_time_tick = 10
    
    def get_state_of_parcels(self):
        return {x.parcel_id:x.current_location for x in self.parcels.values()}
        

    def process_parcels(self, booking_file_path):
        with open(booking_file_path,'r') as file:
            parcels = csv.reader(file,delimiter = ' ')
            for row in parcels:
                src = self.graph.vertices[row[2]]
                dest = self.graph.vertices[row[3]]
                parcel = Parcel(int(row[0]),row[1],row[2],row[3],int(row[4]))
                self.parcels[row[1]]=(parcel)
                src.add_parcel(parcel)
                
                
    
    def getNewBookingsatTimeTickatVertex(self, time_tick, vertex):
        bookings = []
        for parcel in vertex.all_parcels:
            if parcel.time_tick == time_tick:
                bookings.append(parcel)
            #print(bookings)
        #print(bookings)
        return bookings


    def run_simulation(self, run_till_time_tick=None):
        run_till = 0
        if(run_till_time_tick):
            run_till = run_till_time_tick
        else:
            run_till = self.max_time_tick
            
        while(self.time_tick<=run_till and self.time_tick<self.max_time_tick):
            self.parcels_with_time_tick[self.time_tick] = list()
            #print(self.time_tick)
            for stop in self.graph.vertices.values():
                if(stop.all_parcels):
                    bookings = self.getNewBookingsatTimeTickatVertex(self.time_tick,stop)
                    self.parcels_with_time_tick[self.time_tick].extend(bookings)
                    for parcel in bookings:
                        stop.loadParcel(parcel)
                    
                    stop.loadFreightCars()
            
            self.graph.groupFreightCars()
            
            self.graph.moveTrains()
            if(self.old_state==[]):
                for parcel in self.parcels.values():
                   self.old_state.append(parcel.current_location)
            else:
                for parcel in parcels:
                    self.new_state.append(parcel.current_location)
            if(self.convergence_check(self.old_state,self.new_state)):
                
                break
            self.time_tick+=1
            self.old_state = self.new_state
            self.new_state = []
        
    def convergence_check(self, previous_state, current_state):
        if(previous_state == current_state):
            
            return True
        return False

    def all_parcels_delivered(self):
        return all(parcel.delivered for _,parcel in self.parcels.items())
    
    def get_delivered_parcels(self):
        return [parcel.parcel_id for parcel in self.parcels.values() if parcel.delivered]
    
    def get_stranded_parcels(self):
        return [parcel.parcel_id for parcel in self.parcels.values() if not parcel.delivered]

    def status_of_parcels_at_time_tick(self, time_tick):
        return [parcel.parcel_id for parcel in self.parcels.values() if parcel.time_tick <= time_tick and not parcel.delivered]
    
    def status_of_parcel(self, parcel_id):
        return self.parcels[parcel_id].delivered, self.parcels[parcel_id].current_location

    def get_parcels_delivered_upto_time_tick(self, time_tick):
        return [parcel.parcel_id for parcel in self.parcels.values() if parcel.time_tick <= time_tick and parcel.delivered]

    def create_graph(self, graph_file_path):
        with open(graph_file_path,'r') as File:
            stations = csv.reader(File,delimiter = ' ')
            for stop in stations:
                src = stop[0]
                dest = stop[1]
                self.graph.add_edge(src,dest,self.min_freight_cars_to_move,self.max_parcel_capacity)
