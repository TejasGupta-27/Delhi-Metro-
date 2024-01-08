import csv
# MetroStop class


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

class MetroLine:
    def __init__(self, name):
        self.line_name = name
        self.node = None
        self.stops=[]

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
        stop = self.node
        count=0
        while stop is not None:
            count+=1
            
            stop=stop.get_next_stop()
           
        return count 

    def get_stop(self,stop_name):
        current=self.node
        while current is not None:
            if current.get_stop_name()==stop_name:
                return current
            current=current.get_next_stop()    
        return None             

    def populate_line(self, filename):
        
        with open(filename) as csv_file:
            csv_reader=csv.reader(csv_file,delimiter="\n")
            temp=[]
            for i in csv_reader:
                
                for j in i:
                    
                    data=j.split()
                   
                    name=""
                    
                    metroname=data[0:-1]
                    for k in range(len(metroname)):

                        name+=metroname[k]
                        if k!=len(metroname)-1:
                            name+=" "

                    fare=data[-1].replace(",","")
                    z=MetroStop(name,self,int(fare))
                    temp.append(z)   
                    self.stops.append(z.get_stop_name()) 
                        
        for i in range(len(temp)):
            if i==0:
                self.node=temp[0]
                temp[0].set_next_stop(temp[1])
            else:
                if(i!=len(temp)-1):
                    temp[i].set_next_stop(temp[i+1])
                temp[i].set_prev_stop(temp[i-1])    


          # Implement this method

# AVLNode class
class AVLNode:
    def __init__(self, name):
        self.stop_name = name
        self.stops = []
        self.left = None
        self.right = None
        self.parent = None

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
    def is_junction(self):
        if len(self.stops)>1:
            return True 
        return False    


# AVLTree class
class AVLTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def height(self,root):
            if root is None:
                return 0
            else:
                left=self.height(root.left)
                right=self.height(root.right)
                return max(left,right)+1

    def string_compare(self, s1, s2):
        if (s1 > s2): return 1
        if (s1 == s2): return 0
        if (s1 < s2 ): return -1

    def balance_factor(self, node):

        
        return self.height(node.left)-self.height(node.right)

            

    def rotate_left(self, node):
        x = node
        y = node.right

        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, node):
        x = node
        y = node.left

        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y

        

    def balance(self, node):
        while node:
            
            if self.balance_factor(node)<-1 and node.right:
                if self.balance_factor(node.right)>0:
                    self.rotate_right(node.right)
                    self.rotate_left(node)
                else:
                    self.rotate_left(node)    
            elif self.balance_factor(node)>1 and node.left:
                if self.balance_factor(node.left)<0:
                    self.rotate_left(node.left)
                    self.rotate_right(node)
                else:
                    self.rotate_right(node)
            node=node.parent
       
    def insert(self, node, metro_stop):
        
        search=self.search_stop(node.get_stop_name())
        if search:
            search.add_metro_stop(metro_stop)
        else: 
            node.add_metro_stop(metro_stop)   
            currrent=self.root 
            
            if self.root is None:
                self.root=node 
            else:
                current=self.root
                while current is not None:
                    node_name=node.get_stop_name()
                    
                    current_name=current.get_stop_name()
                    if self.string_compare(node_name,current_name)==-1 or self.string_compare(node_name,current_name)==0:
                        if current.get_left() is None:
                            current.set_left(node)
                            node.set_parent(current)
                            break 
                        current=current.get_left()
                    else:
                        if current.get_right() is None:
                            current.set_right(node)
                            node.set_parent(current)
                            break 

                        
                        current=current.get_right()


            self.balance(node.parent)        
        # Implement this method

    def populate_tree(self, metro_line):
        metro_stop_node=metro_line.get_node()
        while metro_stop_node is not None:
            
            self.insert(AVLNode(metro_stop_node.get_stop_name()),metro_stop_node)
            metro_stop_node=metro_stop_node.get_next_stop()

          # Implement this method

    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.get_left())
        
        self.in_order_traversal(node.get_right())
        

    def get_total_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.get_total_nodes(node.get_left()) + self.get_total_nodes(node.get_right())

    def search_stop(self, stop_name):
        if self.root is None:
            return False 
        else:
            current=self.root
            while current is not None:
                if stop_name==current.get_stop_name():
                    return current 
                elif stop_name<=current.get_stop_name():
                    current=current.get_left()
                else:
                    current=current.get_right()       

        return False

        

# Trip class
class Trip:
    def __init__(self, metro_stop, previous_trip):
        self.node = metro_stop
        self.prev = previous_trip
        self.direction="forward"
        if previous_trip is not  None:
            self.fare=abs(metro_stop.get_fare()-previous_trip.get_node().get_fare())
        else:
            self.fare=0  
    def get_node(self):
        return self.node

    def get_prev(self):
        return self.prev
    def set_direction(self,direction):
        self.direction=direction   
    def get_direction(self):
        return self.direction    
    def get_trip_fare(self):
        return(self.fare)    

# Exploration class
class Exploration:
    def __init__(self):
        self.trips = []

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
        self.total_fare = 0

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
        for i in self.lines:
            self.tree.populate_tree(i)
            
          
    def trip_maker(self,stop,prev_trip,explore):
        current_forward=stop.get_next_stop()
        current_backward=stop.get_prev_stop() 
        current_trip_forward=Trip(stop,prev_trip)
        current_trip_backward=Trip(stop,prev_trip)
        while current_forward is not None:
            z=Trip(current_forward,current_trip_forward)
            
            explore.enqueue(z)
            current_forward=current_forward.get_next_stop()
            current_trip_forward=z
        while current_backward is not None:
            z=Trip(current_backward,current_trip_)
            
            explore.enqueue(z)
            current_forward=current_forward.get_next_stop()
            current_trip_forward=z

        
    def forward_traversal(self,metro_stop,explore,trip_object,trips,tree):
        current=metro_stop.get_next_stop()
        
        current_trip=trip_object

        while current is not None:
            
            if tree.search_stop(current.get_stop_name()).is_junction():
                
                
                for i in tree.search_stop(current.get_stop_name()).stops:
                    if i!=current:
                        if i.get_line().get_line_name()+"forward" not in lines:
                            if i.get_next_stop() is not None:
                                self.forward_traversal(i.get_next_stop(),explore,current_trip,trips,tree)
                                lines.append(i.get_line().get_line_name()+"forward")
                           
            z=Trip(current,current_trip)
            explore.enqueue(z)
            
            current=current.get_next_stop()
            current_trip=z





    def backward_traversal(self,metro_stop,explore,trip_object,trips,tree):
        current=metro_stop.get_prev_stop()
        current_trip=trip_object
        while current is not None:
            if tree.search_stop(current.get_stop_name()).is_junction():
                
                
                for i in tree.search_stop(current.get_stop_name()).stops:
                    if i!=current:
                       
                        if i.get_line().get_line_name()+"backward"  not in lines:
                            if i.get_prev_stop() is not None :

                                self.backward_traversal(i.get_prev_stop(),explore,current_trip,trips,tree)
                                lines.append(i.get_line().get_line_name()+"backward")
            z=Trip(current,current_trip)

            explore.enqueue(z)
            current=current.get_prev_stop()
            current_trip=z



    def find_path(self, origin, destination):
        trips=[]
        line=[]
        origin_node=self.tree.search_stop(origin)
        explore=Exploration()

        
            
            
        for i in origin_node.stops:

            
            current_stop=i
            current_line=current_stop.get_line()
            line.append(current_line.get_line_name()+"forward")
            line.append(current_line.get_line_name()+"backward")
            # current_stop=current_line.get_stop(origin)
            
            origin_trip_forward=Trip(current_stop,None)
            origin_trip_backward=Trip(current_stop,None)

            explore.enqueue(origin_trip_forward)
            explore.enqueue(origin_trip_backward)
            self.forward_traversal(current_stop,explore,origin_trip_forward,trips,self.tree)
            self.backward_traversal(current_stop,explore,origin_trip_backward,trips,self.tree)
       
                


        

        
        while not  explore.is_empty():
                current_trip=explore.dequeue()
        
                current_node=current_trip.get_node()
                if current_node.get_stop_name()==destination:
                    path=Path()
                    fare=0
                    while current_trip is not None:
                        
                        fare+=current_trip.get_trip_fare()
                        path.add_stop(current_trip.get_node())
                        current_trip=current_trip.get_prev()
                    
                    path.set_total_fare(fare)

                    return path        
        
           
                    
        

lines = []