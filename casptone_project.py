import heapq
import uuid
# Universally unique indentifier 128 bit number
from collections import defaultdict
# is similar to regular dictionary but it provides a default value for they key that does not exist


class LinkedListNode:
    def __init__(self , data):
        # initialize the node with data and set the next node to none
        self.data = data
        self.next = None

# linked list to manage patient history
class LinkedList:
    def __init__(self):
        # initialize the linked list with empty head
        self.head = None
    
    def append(self , data):
        # create a new node with the given data
        if not self.head:
            # if list is empty, set the new  node as the head
            self.head = LinkedListNode(data)
        else:
            # traverse the list to find the last node
            current = self.head
            while(current.next):
                current = current.next
            # append the new node at the end of the list
            current.next = LinkedListNode(data)
    
    def get_history(self):
        # initialize the empty list to store the history
        history = []
        # start from the head of the list
        current = self.head

        while current :
            # append each node's data to the history list
            history.append(current.data)
            current = current.next
        # return the collected history
        return history

# patient class to store patient information
class Patient:
    def __init__(self , patient_id , name , age , blood_type) -> None:
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.blood_type = blood_type
        self.history = LinkedList()

# appointment class to store appointment information
class Appointment:
    def __init__(self , appointment_id , patient , date, time) -> None:
        self.appointment_id = appointment_id
        self.patient = patient
        self.date = date
        self.time = time


# binary search treee for efficient patient record search

class BinarySearchTree:
    class Node:
        def __init__(self,key,patient) -> None:
            # intialize the node with key patient and left/right chuldren
            self.key = key
            self.patient = patient
            self.left = None
            self.right = None
        
    def __init__(self) -> None:
        # intialize the bst with an empty root
        self.root = None
    
    def insert(self,key,patient):
        # if the three is empty set the new node as root
        if self.root is None:
            self.root = self.Node(key , patient)
        else:
            # otherwise insert the node at the correct position
            self._insert(self.root , key , patient)
    
    def _insert(self , node , key , patient):
        
        if key < node.key:
            if node.left is None:
                # insert the new node as the left chuld
                node.left = self.Node(key , patient)
            else:
                # recursively insert into left subtree
                self._insert(node.left , key , patient)
        else:
            if node.right is None:
            # insert the new node as the right child
                node.right = self.Node(key , patient)
            else:
                # recursively insert into right subtree
                self._insert(node.right , key , patient)
    
    def search(self, key):
        # search for the node with given key starting from the root
        return self._search(self.root , key)

    def _search(self , node , key):
        # if node is none or node if found return 
        if node is None or node.key == key:
            return node
        # search the left subtree
        if key < node.key:
            return self._search(node.left , key)
        # search the right subtree
        return self._search(node.right , key)
    

# priority queue for handling appointment queues
class PriorityQueue:
    def __init__(self) -> None:
        # intialize the priority queue with an empty heap
        self.heap = []
    
    def push(self,item):
        # add a new item to the priority queue
        heapq.heappush(self.heap , item)
    

    def pop(self):
        # remove and return the item with the highest priority
        return heapq.heappop(self.heap)
    
    def is_empty(self):
        # check if the priority queue is empty
        return len(self.heap) == 0

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False
    
# trie for storing medical terms
class Trie:
    def __init__(self) -> None:
        # intialize the trie with a root node
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        # insert a word into the trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        # mark the final node as the end of the word
        node.is_end_of_word = True
    

    def search(self,word):
        node = self.root

        # searhc for a word in the trie
        for char in word:   
            if char not in node.children:
                return False
            node = node.children[char]
        
        # return true if final node is marked as the end of the word
        return node.is_end_of_word

    def starts_with(self,prefix):
        # check if there is any word in the trie that starts with the given prefix
        node = self.root

        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _collect_terms(self,node,prefix,results):
        # collect all words in the trie that start with given prefix
        if node.is_end_of_word:
            results.append(prefix)
        
        for char, next_node in  node.children.items():
            self._collect_terms(next_node , prefix + char , results)
        
        return results
    
class HealthCareManagementSystem:
    def __init__(self) -> None:
        self.patients = []
        self.appointments = []
        self.inventory = []
        self.patient_bst = BinarySearchTree()
        self.appointment_queue = PriorityQueue()
        self.medical_terms = Trie()
        self.appointments_dict = defaultdict(list)
    
    def add_patient(self , name , age , blood_type):
        patient_id = str(uuid.uuid4())
        patient = Patient(patient_id , name ,age , blood_type)
        self.patients.append(patient)

        self.patient_bst.insert(patient_id , patient)
        print(f"Patient added successfully with ID : {patient_id}")
    
    def schedule_appointment(self , patient_id , date , time):
        appointment_id = str(uuid.uuid4())
        node = self.patient_bst.search(patient_id)
        if node:
            patient = node.patient
            appointment = Appointment(appointment_id , patient , date , time)
            self.appointments.append(appointment)
            self.appointment_queue.push((date , time , appointment))
            self.appointments_dict[date].append(appointment)
            print(f"Appointment scheduled successfully with id: {appointment_id}")
        else:
            print("Patient not found")
    
    def manage_inventory(self , item):
        self.inventory.append(item)
        print("Inventory item added successfully")
        # homework enhance this , handle management part
    
    def get_patient_history(self , patient_id):
        node = self.patient_bst.search(patient_id)

        if node:
            patient = node.patient
            return patient.history.get_history()
        else:
            print("Patient not found")
            return []
    
    def get_appointment_schedule(self):
        schedule = []
        while not self.appointment_queue.is_empty():
            schedule.append(self.appointment_queue.pop()[2])
        
        return schedule
    
    def add_patient_history(self , patient_id , history_entry):
        node = self.patient_bst.search(patient_id)

        if node:
            patient = node.patient

            patient.history.append(history_entry)
            print(f"Patient history added")
        else:
            print("Patient not found")
    

    def insert_medicial_term(self , term):
        self.medical_terms.insert(term)
        print("Medical term inserted")
    
    def search_medical_term(self, term):
        return self.medical_terms.search(term)

    def suggest_medical_terms(self , prefix):
        node = self.medical_terms.starts_with(prefix)

        if node:
            return self.medical_terms._collect_terms(node , prefix , [])
    
        return []
    
    def display_ordered_appointments(self):
        ordered_appointments = sorted(self.appointments , key = lambda x: (x.date , x.time) )

        for appointment in ordered_appointments:
            print(f"Appintment Id : {appointment.appointment_id} , Patient : {appointment.patient.name} , Date : {appointment.date} , Time : {appointment.time} ")

    
    def display_patients(self):
        if not self.patients : 
            print("No patients found")
        else:
            for patient in self.patients:
                print(f"Patient Id : {patient.patient_id}, Name : {patient.name} , Age : {patient.age} , Blood type : {patient.blood_type}")
    
    def display_menu(self):
        print("\nHealthcare Management System Menu")
        print("1. Add Patient")
        print("2. Schedule Appointment")
        print("3. Manage Inventory")
        print("4. Add Patient History")
        print("5. Get Patient History")
        print("6. Get Appointment Schedule")
        print("7. Insert Medical Term")
        print("8. Search Medical Term")
        print("9. Suggest Medical Terms")
        print("10. Display Ordered Appointments")
        print("11. Exit")
    
    def handle_menu(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid input. Please enter a number")
                continue
            

            if choice == 1:
                name = input("Enter patient name")

                try:
                    age = int(input("Enter patient age: "))
                except ValueError:
                    print("Invalid input. Age must be a number")
                    continue

                blood_type = input("Enter blood type: ")

                self.add_patient(name , age , blood_type)
            
            elif choice == 2:

                self.display_patients() 
                patient_id = input("Enter patient id: ")

                # homework add validations for date and time
                date = input("Enter appointment date (YYYY-MM-DD): ")
                time = input("Enter appointment time(HH:MM): ")
                self.schedule_appointment(patient_id , date , time)
            
            elif choice == 3:
                item = input("Enter inventory item")
                self.manage_inventory(item)
            
            elif choice == 4:
                self.display_patients()
                patient_id = input("Enter patient id: ")

                history_entry = input("Enter history entry: ")

                self.add_patient_history(patient_id , history_entry)
            
            elif choice == 5:
                self.display_patients()

                patient_id = input("Enter patient id: ")
                history = self.get_patient_history(patient_id)

                if history:
                    print("Patient history: ",history)
                
            
            elif choice == 6:
                schedule = self.get_appointment_schedule()
                print("Appointment schedule: ")
                for appointment in schedule:
                    print(f"Appointment id: {appointment.appointment_id}, Patient : {appointment.patient.name}, Date: {appointment.date} , Time : {appointment.time}")
            
            elif choice == 7:
                term = input("Enter the medical term")
                self.insert_medicial_term(term)

            elif choice == 8:
                term = input("Enter the medical term to search")
                found = self.search_medical_term(term)
                print("Medical term found" if found else "Medical term not found")

            elif choice == 9:
                prefix = input("Enter prefix to suggest terms: ")
                suggestions = self.suggest_medical_terms(prefix)
                print("Suggestions" , suggestions)
            
            elif choice == 10:
                self.display_ordered_appointments()
            elif choice == 11:
                print("Exiting")
                break
            else :
                print("Invalid choice. Please try again.")

def main():
    system = HealthCareManagementSystem()

    system.handle_menu()

if __name__ == "__main__":
    main()