import math

# Hash table class
# Contains methods to initialise, add, remove, calculate hash code, and print formatted.
class HashTable:
    #
    # !!!! better way of specifying number of buckets? !!!!
    #
    def __init__(self, nbuckets=5):
        # buckets is a list of lists
        # The innermost lists store the key-pair values
        self.buckets = [[] for i in range(nbuckets)]

    # Adds key-value pair to hash table
    def put(self, key, value):
        # Calculate hash code - this will be the index of its bucket
        hash = self.calc_hash_code(key)
        # Add the key-value pair to the appropriate bucket
        self.buckets[hash].append((key, value))

    """ (this code might be redundant! does it serve the same purpose as the binary search? !
    # retrieve a value corresponding to a given key
    #def get(self, key):
        hash = self.calc_hash_code(key)

        for findKey in self.buckets[hash]:
            if key == findKey[0]:
                return findKey[1]
    """

    # Removes key-value pair from the hash table
    def remove(self, key):
        # Calculate hash value of the POI name
        hash = self.calc_hash_code(key) % len(self.buckets)

        # Checks if the name specified exists based on its hash code
        if self.buckets[hash] is not None:
            # If it exists, it is removed from the list
            self.buckets[hash].pop()
            print("Successfully deleted")
        else:
            print("POI does not exist.")

    # Calculates hash code by summing up ASCII characters,
    # Then takes the modulus of the length of the hash table
    def calc_hash_code(self, key):
        hash = 0
        # Loops through each character and sums their ASCII values
        for char in key:
            hash += ord(char)
        # Takes the modulus of hash by the length of the hash table (keeps it within range of the table)
        hash = hash % len(self.buckets)
        return hash

    # Prints the hash table contents in a user-friendly format
    def __str__(self):
        output = ""
        # Prints each bucket on a new line
        for bucket in self.buckets:
            output += f"{bucket}\n"
        return output


# Binary search for a POI name
def binary_search_name(num_list, search_term):
    # Initialises the pointers - the start and end of the hash table
    left = 0
    right = len(num_list.buckets) - 1

    # Calculates hash code of the POI name
    hashCode = ht.calc_hash_code(search_term)

    # Begins loop
    while left <= right:
        # Find midpoint of list to search
        midpoint = math.floor((left + right)/2)
        # Checks if midpoint matches hashCode
        if midpoint == hashCode:
            # If true, the POI should be within the bucket
            foundItem = num_list.buckets[midpoint]

            # Checks for collisions on the index
            if len(foundItem) > 1:
                #
                # !!!! THIS NEEDS FIXING!!!!
                #
                for i in foundItem:
                    if i[0] == search_term:
                        return i
                    else:
                        return "NEED TO FIX !!"
            # If no collisions, simply return foundItem
            else:
                return foundItem

        # If hashCode is greater than the midpoint,
        elif midpoint < hashCode:
            # Set left to midpoint +1, then loop again
            left = midpoint + 1
        # If hashCode is less than the midpoint,
        else:
            # Set right to midpoint - 1, then loop again
            right = midpoint - 1
    # If left > right, the end of the list is reached, POI does not exist.
    return "Point of Interest not found."


# for quick sort
# Params: entire set of data; start index of current run; end index of
# current run

def hoare(data, start, end):
    i = start
    j = end

    # Pivot value
    pivot = data[math.floor((0 + len(ht.buckets))/2)]

    # Loop infinitely...
    while True:
        # Increase i until it's pointing to something greater than or equal to the pivot
        while i[0:] < pivot[0]:
            i += 1

        # Similarly decrease j until it's pointing to something less than or equal to the pivot
        while j[0] > pivot:
            j -= 1

        # now we test to see if i and j have crossed over, in which case
        # the partitioning is finished
        if j <= i:
            return i # can return either i or j

        # swap the two values at i and j round, because they will be in
        # the wrong place relative to the pivot
        data[0][i],data[0][j] = data[0][j],data[0][i]


# This will carry out the recursive aspect of quicksort
# same parameters as hoare()

def quicksort(data, start, end):
    # if the section of list has at least 2 members, it needs to be partitioned
    if end > start:
        pivot_index = hoare(data, start, end)

        # Recursion comes in here...
        # Recursively call quicksort twice on:
        # a) the section before pivot_index
        # b) the section after pivot_index
        quicksort(data,start,pivot_index-1)
        quicksort(data,pivot_index+1,end)


# Method to print the menu
def menu():
    print("""POINTS OF INTEREST:
    1. Add new Point of Interest
    2. Search for type of Point of Interest
    3. Display all Points of Interest
    4. Search for Point of Interest (by name)
    5. Delete Point of Interest
    6. Save current Point of Interest list
    7. Load stored Point of Interest list
    """)


# User selection options
def menu_select():
    menu()
    selected = 0

    # Ensure user enters valid entry
    while selected > 7 or selected < 1:
        selected = int(input("Enter menu selection: "))

    if selected == 1:
        add_poi()
    elif selected == 2:
        search_for_type()
    elif selected == 3:
        display_hash_table()
    elif selected == 4:
        search_for_name()
    elif selected == 5:
        delete_poi()
    elif selected == 6:
        save_to_file()
    else:
        load_from_file()


# User inputs the name, type, and description of POI
def add_poi():
    poi_name = input("Enter POI name: ")
    poi_type = input("Enter POI type: ")
    poi_desc = input("Enter POI description: ")

    # Type and Description are added to a tuple
    type_desc_tuple = (poi_type, poi_desc)

    # These are passed to the put() method in HashTable
    ht.put(poi_name, type_desc_tuple)
    print(poi_name + " successfully added.")

    menu_select()

    # add inputs validation. user should enter value for each.


#
# !!!!! should search and return every POI with the 'type' specified? i think?
#
def search_for_type():
    search_term = input("Enter type of POI to search for: ")
    binary_search(ht, search_term)
    # fix this so it returns multiple values. maybe add them to a list to return
    # then format that list so they print on different rows
    # i dont super understand this step in the assignment brief
    menu_select()


#
# !!!! this should sort the results alphabetically using a sorting algorithm!!!!
#
def display_hash_table():
    print("\nPoints of Interest\n")
    print(ht)
    menu_select()
    #this needs to be sorted alphabetically


# Uses binary search to search for user-specified POI, returns its key-value pair
def search_for_name():
    search_term = input("Enter name of POI to search for: ")
    print(binary_search_name(ht, search_term))
    menu_select()


# Deletes user-specified POI from the hash table
def delete_poi():
    to_delete = input("Enter name of POI to delete: ")
    ht.remove(to_delete)
    menu_select()


#
# !!!! need to clarify best way to save this!!!!
# because it should probably be written in a specific format so it can be read back in the hash table
#
def save_to_file():
    file = open("saved_pois.txt", "w")

    file.close()
    menu_select()

#
# !!!! this depends on the save_to_file method above!!!! should these values get read then added to table one by one?
#
def load_from_file():
    file = open("saved_pois.txt", "r")
    print(file.read())

    file.close()
    menu_select()


# Test code
ht = HashTable()


# test data for convenience. remove before submitting.
ht.put("alton towers", ("theme park", "A theme park Staffordshire"))
ht.put("pyle street", ("highstreet", "A street in Newport"))
ht.put("vicar street", ("venue", "A venue in dublin"))
ht.put("tower of london", ("landmark", "landmark in london"))
ht.put("coronation street", ("film set", "A street in London"))

menu_select()


#print("quicksort")
#print(quicksort(ht.buckets, ht.buckets[0], ht.buckets[len(ht.buckets)-1]))
