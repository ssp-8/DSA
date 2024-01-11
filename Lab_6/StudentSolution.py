import csv
class HybridNode:
    def __init__(self, key, element):
        self.key = key
        self.color = "black"
        self.element = element
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.next_node = None


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.count = 0
    def find_suitable(self,key):
        v = self.root
        w = None
        while(v!=None):
            w = v
            if(v.key>key):
                v = v.left_child
            elif(v.key<key):
                v = v.right_child
        return w
    
    def no_child_deletion(self,node):
        Node = node.parent
        if(node.parent.key>node.key):
            node.parent.left_child = None
        else:
            node.parent.right_child =None
        return None
    
    def one_child_deletion(self,node):
        x = None
        if(node.left_child==None):
            x = node.right_child
        else:
            x = node.left_child
        if(node.parent.key>node.key):
            if(node.left_child !=None):
                node.parent.left_child = node.left_child
                node.left_child.parent = node.parent
            else:
                node.parent.left_child = node.right_child
                node.right_child.parent = node.parent
        else:
            if(node.left_child !=None):
                node.parent.right_child = node.left_child
                node.left_child.parent = node.parent
            else:
                node.parent.right_child = node.right_child
                node.right_child.parent = node.parent
        return x
    
    def sibling(self,node):
        if(node==None):
            return
        if(node.parent!=None):
            if(node.parent.left_child!=node):
                return node.parent.left_child
            else:
                return node.parent.right_child
            
    def find_successor(self,node):
        root = HybridNode(None,None)
        w = node.right_child
        v = None
        root = node.parent
        if(w==None):
            while(root!=None):
                v = root
                if(root.key>=node.key):
                    return root
                else:
                    root = root.parent
            return v
        else:
            while(w!=None):
                root = w
                w = w.left_child
            return root
        
    def deal_overflow(self,node):
        while(node!=None and node.color=="red" and node.parent!=None and node.parent.color == "red"):
            if(self.sibling(node.parent)!=None and self.sibling(node.parent).color == "red"):
                node = self.recolor(node.parent)
            else:
                self.restructure(node)
                return
                        
    def recolor(self,node):
         node.color = "black"
         self.sibling(node).color = "black"
         if(node.parent!=self.root and node.parent!=None):
             node.parent.color = "red"
         return node.parent
        
    def nodes(self,node):
        if(node==None):
            return 0
        else:
            print(node.key,self.height(node))
            return 1+self.nodes(node.left_child)+self.nodes(node.right_child)
        
    def right_rotate(self,node):
        z = node
        y = node.left_child
        p = z.parent
        t = y.right_child
        y.right_child = z
        z.parent = y
        y.parent = p
        z.left_child = t
        if(t!=None):
            t.parent = z
        if(y.parent == None):
            y.color = "black"
            self.root = y
        else:
            if(y.parent.key>y.key):
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.color = "red"
        y.color = "black"
        
    def right_rotate_delete(self,node):
        z = node
        y = node.left_child
        p = z.parent
        t = y.right_child
        z.left_child = t
        if(t!=None):
            t.parent = z
        y.parent = node.parent
        if(y.parent == None):
            self.root = y
        else:
            if(node == node.parent.left_child):
                node.parent.left_child = y
            else:
                node.parent.right_child = y
                y.parent = p
        y.right_child = node
        node.parent = y
        

    def left_rotate(self,node):
        z = node
        y = node.right_child
        p = z.parent
        t = y.left_child
        y.left_child = z
        z.parent = y
        y.parent = p
        z.right_child = t
        if(t!=None):
            t.parent = z
        if(y.parent == None):
            y.color = "black"
            self.root = y
        else:
            if(y.parent.key>y.key):
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.color = "red"
        y.color = "black"
        
                            
    def double_rotate(self,node,direction):
        if(direction == 1):
            self.right_rotate(node.right_child)
            self.left_rotate(node)
        else:
            self.left_rotate(node.left_child)
            self.right_rotate(node)
            
    def restructure(self,node):
        x = node
        y = node.parent
        z = y.parent
        if(z!=None):
            if(z.left_child == y and y.left_child == x):
                self.right_rotate(z)
            elif(z.right_child == y and y.right_child == x):
                self.left_rotate(z)
            elif(z.right_child == y and y.left_child == x):
                self.double_rotate(z,1)
            else:
                self.double_rotate(z,2)
        
    def deal_underflow(self,node):
        v = node
        while(v!=None):
            if(self.black_height(node.left_child)!=self.black_height(node.right_child)):
                subtree = None
                if(self.black_height(node.left_child)<self.black_height(node.right_child)):
                    subtree = node.left_child
                else:
                    subtree = node.right_child
                if(node.color == "red"):
                    self.red_handle(node,subtree)
                else:
                    v = self.black_handle(node,subtree)
            else:
                v = v.parent

    def red_handle(node,subtree):
        if(node==None):
            return
        b = self.sibling(subtree)
        if(b!=None):
            left = b.left_child
            right = b.right_child
            if(left==None and right==None):
                b.color = "red"
                node.color = "black"
            elif(left!=None and right==None and left.color == 'black'):
                b.color = "red"
                node.color = "black"
            elif(right!=None and left == None and right.color == 'black'):
                b.color = 'red'
                node.color = 'black'
            elif(left.color == 'black' and right.color == 'black'):
                b.color = 'red'
                node.color = 'black'
            elif(node.left_child == b):
                c = None
                l = self.height(left)
                r = self.height(right)
                if(l>r):
                    c = left
                else:
                    c = right
                if(c == left):
                     self.right_rotate(node)
                     b.color = 'red'
                     node.color = 'black'
                     left.color = 'black'
                else:
                     self.double_rotate(node,2)
                     b.color = 'black'
                     node.color = 'black'
                     right.color = 'red'

            elif(node.right_child == b):
                    c = None
                    l = self.height(left)
                    r = self.height(right)
                    if(l>r):
                        c = left
                    else:
                        c = right
                    if(c == right):
                        self.left_rotate(node)
                        b.color = 'red'
                        node.color = 'black'
                        right.color = 'black'
                    else:
                        self.double_rotate(node,1)
                        b.color = 'black'
                        node.color = 'black'
                        left.color = 'red'
                    
                        
    def black_handle(self,node,subtree):
        b = self.sibling(subtree)
        if(b!=None):
            left = b.left_child
            right = b.right_child
            if(b.color == 'black'):
                if(left==None and right==None):
                    b.color = "red"
                    node.color = "black"
                elif(left!=None and right==None and left.color == 'black'):
                    b.color = "red"
                    node.color = "black"
                elif(right!=None and left == None and right.color == 'black'):
                    b.color = 'red'
                    node.color = 'black'
                elif(left.color == 'black' and right.color == 'black'):
                    b.color = 'red'
                    node.color = 'black'
                elif(node.left_child == b):
                    if(right!=None and left==None):
                        self.double_rotate(node,2)
                        left.color = 'black'
                        node.color = 'black'
                        b.color = 'black'
                    if(left != None and right==None):
                        self.right_rotate(node)
                        b.color = 'black'
                        node.color = 'black'
                        left.color = 'black'
                    elif(node.right_child == b):
                        if(right==None and left!=None):
                            self.double_rotate(node,1)
                            left.color = 'black'
                            node.color = 'black'
                            b.color = 'black'
                        if(left == None and right!=None):
                            self.left_rotate(node)
                            b.color = 'black'
                            node.color = 'black'
                            left.color = 'black'
                            
            else:
                c= None
                l = self.height(left)
                r = self.height(right)
                if(l>r):
                    c = left
                else:
                    c = right
                if(c==right):
                    if(c.left_child == None and c.right_child==None):
                        self.right_rotate(node)
                        b.color = 'black'
                        node.color = 'black'
                        right.color = 'red'
                    elif(c.left_child!=None and c.left_child.color == 'black' and c.right_child==None):
                        self.right_rotate(node)
                        b.color = 'black'
                        node.color = 'black'
                        right.color = 'red'
                    elif(c.right_child!=None and c.right_child.color == 'black' and c.left_child==None):
                        self.right_rotate(node)
                        b.color = 'black'
                        node.color = 'black'
                        right.color = 'red'
                    elif(c.right_child.color == 'black' and c.left_child.color == 'black'):
                        self.right_rotate(node)
                        b.color = 'black'
                        node.color = 'black'
                        right.color = 'red'
                    else:
                        d = None
                        c_left = c.left_child
                        c_right = c.right_child
                        l = self.height(c.left_child)
                        r = self.height(c.right_child)
                        if(l>r):
                            d = c.left_child
                        else:
                            d = c.right_child
                        if(d==c.left_child):
                            self.double_rotate(node,2)
                            right.color = 'black'
                            node.color = 'black'
                            b.color = 'red'
                            d.color = 'black'
                        else:
                            self.double_rotate(node,2)
                            right.color = 'black'
                            node.color = 'black'
                            b.color = 'red'
                            d.color = 'red'
                            c_left.color = 'black'
                
                if(c==left):
                    if(c.left_child == None and c.right_child==None):
                        self.right_rotate(node)
                        b.color = 'black'
                        node.color = 'black'
                        left.color = 'black'
                    elif(c.left_child!=None and c.left_child.color == 'black' and c.right_child==None):
                        self.right_rotate(node)
                        b.color = 'black'
                        node.color = 'black'
                        left.color = 'black'
                    elif(c.right_child!=None and c.right_child.color == 'black' and c.left_child==None):
                        self.right_rotate(node)
                        b.color = 'black'
                        node.color = 'black'
                        left.color = 'black'
                    elif(c.right_child.color == 'black' and c.left_child.color == 'black'):
                        self.right_rotate(node)
                        b.color = 'black'
                        node.color = 'black'
                        left.color = 'black'
                    else:
                        d = None
                        c_left = c.left_child
                        c_right = c.right_child
                        l = self.height(c.left_child)
                        r = self.height(c.right_child)
                        if(l>r):
                            d = c.left_child
                        else:
                            d = c.right_child
                        if(d==c.left_child):
                            self.double_rotate(node,2)
                            right.color = 'black'
                            node.color = 'black'
                            b.color = 'red'
                            d.color = 'black'
                        else:
                            self.double_rotate(node,2)
                            right.color = 'black'
                            node.color = 'black'
                            b.color = 'red'
                            d.color = 'red'
                            c_left.color = 'black'

                          
    def two_child_deletion(self,node):
        Node = node.parent
        succ = self.find_successor(node)
        node.key = succ.key
        node.element = succ.element
        if(succ.left_child == None and succ.right_child == None):
            self.no_child_deletion(succ)
        else:
            self.one_child_deletion(succ)
        return Node
    
    def insert(self, key, element):
        if(self.root==None):
            self.root = HybridNode(key,element)
            self.root.color = "black"
            return self.root
        node = HybridNode(key,element)
        node.color = "red"
        Node = self.find_suitable(key)
        node.parent = Node
        if(Node.key>node.key):
            Node.left_child = node
        elif(Node.key<node.key):
            Node.right_child = node
        self.deal_overflow(node)
        return node
        
    def delete(self,key):
        Node = self.search(key)
        p = Node.parent
        if(Node==None):
            return
        if(Node.left_child == None and Node.right_child == None):
            self.no_child_deletion(Node)
        elif(Node.left_child == None or Node.right_child ==None):
            self.one_child_deletion(Node)
        else:
            self.two_child_deletion(Node)
        
    def traverse_up(self, node):
        result = []
        while(node!=self.root):
            result.append(node)
            node = node.parent
        return result

    def traverse_down(self, node, bit_sequence):
        result = []
        if(node!=None):
            for i in bit_sequence:
                result.append(node)
                if(i=='1'):
                    node = node.left_child
                elif(i=='0'):
                    node = node.right_child
        return result
    
    def preorder_traversal(self,node,depth,result):
        if(node==None or depth == -1):
            return
        result.append(node)
        self.preorder_traversal(node.left_child,depth-1,result)
        self.preorder_traversal(node.right_child,depth-1,result)
        return result
    
    def black_height(self, node):
        j = 0
        while(node!=None):
            if(node.color == "black"):
                j+=1
            node = node.right_child
            
        return j
    
    def height(self,node):
        if(node==None):
            return 0
        else:  
            return 1+max(self.height(node.left_child),self.height(node.right_child))
        
    def search(self, key):
        v = self.root
        while(v!=None):
            if(v.key>key):
                v = v.left_child
            elif(v.key<key):
                v = v.right_child
            else:
                return v
        return None

class Lexicon:
    def __init__(self):
        self.red_black_tree = RedBlackTree()
        self.index_entries = []
        
    def read_chapters(self, chapter_names):
        punctuations = [',','.','!','?'',',':',';',"'",'"']
        words  = []
        n = -1
        for i in chapter_names:
            n+=1
            words = []
            chapter_name = i.replace('.txt','')
            with open(i,mode='r') as file:
                File = csv.reader(file,delimiter=' ')
                for row in File:
                    for word in row:
                        word = word.lower()
                        for j in punctuations:
                            if(word not in punctuations and word[len(word)-1]!= j and word[0] != j):
                                words.append(word)
                                break
                            elif(word in puncutations):
                                continue
                            else:
                                word.replace(j,'')
                                words.append(word)
                                break
            for word in words:
                if(self.red_black_tree.search(word)==None):
                    self.red_black_tree.insert(word,chapter_name)
                    word_index_entry = IndexEntry(word)
                    word_index_entry.chapter_word_counts = [['name',0]]*len(chapter_names)
                    word_index_entry.chapter_word_counts[n] = [chapter_name,1]
                    self.index_entries.append(word_index_entry)
                else:
                    flag = 0
                    for index in self.index_entries:
                        if(index.word==word):
                            for chapter in index.chapter_word_counts:
                                if(chapter[0] == chapter_name):
                                    chapter[1] = chapter[1]+1
                                    flag = 1
                                    break
                            if(flag == 0):
                                index.chapter_word_counts[n] = [chapter_name,1]
                                break
                            if(flag ==1):
                                break
        self.prune_red_black_tree()
        
    def prune_red_black_tree(self):
        to_remove = []
        for i in self.index_entries:
           
            if(i.chapter_word_counts.count(['name',0])==0):
                self.red_black_tree.delete(i.word)
                to_remove.append(i)
        for i in to_remove:
            self.index_entries.remove(i)
                 

    def build_index(self):        
        return self.index_entries
    
class IndexEntry:
    def __init__(self, word):
        self.word = word
        self.chapter_word_counts = [] # List of (chapter, word_count) tuples
