import csv
import unittest
import time
class PhoneRecord:
    def __init__(self, name, organisation, phone_numbers):
        self.name = name
        self.organisation = organisation
        self.phone_numbers = phone_numbers

    def get_name(self):
        return self.name

    def get_organisation(self):
        return self.organisation

    def get_phone_numbers(self):
        return self.phone_numbers
class HashTableRecord:
    def __init__(self, key, record):
        self.key = key
        self.record = record
        self.next = None

    def get_key(self):
        return self.key

    def get_record(self):
        return self.record

    def get_next(self):
        return self.next

    def set_next(self, nxt):
        self.next = nxt
class PhoneBook:
    HASH_TABLE_SIZE = 263

    def __init__(self):
        self.hash_table = [None] * PhoneBook.HASH_TABLE_SIZE
    class LinkedList:
        def __init__(self,name,s):
            self.iterator = HashTableRecord(name,s)
            self.tail = HashTableRecord(None,None)
            self.tail = self.iterator
        def add_record(self,name,record):
            s1 = HashTableRecord(name,record)
            self.tail.next = s1
            s1.set_next(None)
            self.tail = s1
        def delete_record(self,s):
            if(self.iterator.get_record().name==s):
                self.iterator = self.iterator.get_next()
            else:
                p = self.iterator
                while(p.next.get_record().name!=s):
                    p=p.next
                p.next = p.next.next
    def compute_hash(self, string):
        h = 0
        for i in range(len(string)):
            h = h+(ord(string[i])*((self.HASH_TABLE_SIZE)**i)%(1000000007))
        h = h%(self.HASH_TABLE_SIZE) 
        return h
    def add_contact(self, record):
        name = record.get_name()
        name = list(name.split(' '))
        for i in name:
            h = self.compute_hash(i)
            if(self.hash_table[h]==None):
                    ll = self.LinkedList(i,record)
                    self.hash_table[h]=ll
            else:
                    self.hash_table[h].add_record(i,record)
    def delete_contact(self, name):
        if(not self.fetch_contacts(name)):
            return False
        c = self.fetch_contacts(name)
        d = c[0]
        if(d):
            k = d.get_name().split(' ')
            for i in k:
                self.hash_table[self.compute_hash(i)].delete_record(d.get_name())
            return True
    def fetch_contacts(self, query):
        start_time = time.time()
        n = query.split(' ')
        d = dict()
        l = list()
        for i in n:
            h = self.compute_hash(i)
            ll = self.hash_table[h]
            if(ll!=None):
                p = HashTableRecord(None,None)
                p = ll.iterator
                while(p!=None):
                    if(p.get_key()==i):
                        l.append(p.get_record())
                    p = p.get_next()
        for j in l:
            d[j] = l.count(j)
        result = []
        d = dict(sorted(d.items(), key=lambda item: item[1],reverse= True))
        for j in d:
            result.append(j)
        return result
    def read_records_from_file(self,filepath):
        with open(filepath,'r') as file:
            File = csv.reader(file)
            for row in File:
                name = row[0]
                org = row[len(row)-1]
                phone_number = row[1:-1]
                contact = PhoneRecord(name,org,phone_number)
                self.add_contact(contact)
    def create_phone_record(self, contact_info):
        name, num, org = contact_info.split(",")
        return PhoneRecord(name.strip(), org.strip(), [num.strip()])
