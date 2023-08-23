import math

class HashTable:
    def __init__(self, nbuckets=5):
        # Creates a list of "nbuckets" empty lists (list comprehension)
        # self.buckets is a list of lists (one list for each bucket)
        # The list for EACH bucket would be a list of tuples (one tuple for each key-value pair stored in the bucket)
        self.buckets = [[] for i in range(nbuckets)]

    # put() - adds a key,value pair to the hash table
    def put(self, key, value):
        hash = self.calcHashCode(key) % len(self.buckets)
        self.buckets[hash].append((key, value))

    # get() - retrieve a value corresponding to a given key
    def get(self, key):
        hash = self.calcHashCode(key) % len(self.buckets)

        for findKey in self.buckets[hash]:
            if key == findKey[0]:
                return findKey[1]

    # return the value corresponding to that key
    def calcHashCode(self, key):
        # should calculate and return the hash code of "key"
        # Initially, just sum the ascii codes of the characters of the key
        hash = 0
        for char in key:
            hash += ord(char)
        return hash

    def __str__(self):
        output = ""
        for bucket in self.buckets:
            output += f"{bucket}\n"
        return output


def binary_search(num_list, search_term):
    left = 0
    right = len(num_list) - 1

    while left <= right:
        midpoint = math.floor((left + right)/2)
        if num_list[midpoint] == search_term:
            return True
        elif num_list[midpoint] < search_term:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return False


# Test code
ht = HashTable()

# Add some data to it
ht.put("vicar street", ("venue", "A venue in dublin"))
print(ht.get("vicar street"))

print(ht)
