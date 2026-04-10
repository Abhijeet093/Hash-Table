"""
Assignment 7: Exploring Hash Tables and Their Practical Applications
This script demonstrates:
1. Custom hash functions
2. Separate chaining (linked list buckets)
3. Open addressing (linear probing)
4. Basic performance comparison
"""

# -------------------------------
# 1. Simple Hash Function
# -------------------------------

def simple_hash(key, table_size):
    """
    Basic hash function using modulo.
    Works well for integers, but may cause clustering.
    """
    return key % table_size


def better_hash(key, table_size):
    """
    Improved hash function using multiplication method.
    Helps distribute keys more uniformly.
    """
    A = 0.618033  # Knuth's constant
    return int(table_size * ((key * A) % 1))


# -------------------------------
# 2. Separate Chaining Hash Table
# -------------------------------

class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        index = simple_hash(key, self.size)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update
                return

        bucket.append((key, value))

    def search(self, key):
        index = simple_hash(key, self.size)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = simple_hash(key, self.size)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# -------------------------------
# 3. Open Addressing (Linear Probing)
# -------------------------------

class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key, value):
        index = simple_hash(key, self.size)
        start_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("Hash table is full")

        self.table[index] = (key, value)

    def search(self, key):
        index = simple_hash(key, self.size)
        start_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                break

        return None

    def delete(self, key):
        index = simple_hash(key, self.size)
        start_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return True
            index = (index + 1) % self.size
            if index == start_index:
                break

        return False

    def display(self):
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")


# -------------------------------
# 4. Performance Demonstration
# -------------------------------

if __name__ == "__main__":
    print("=== Separate Chaining Example ===")
    ht_chain = HashTableChaining(10)

    keys = [10, 20, 30, 15, 25]
    for k in keys:
        ht_chain.insert(k, f"Value{k}")

    ht_chain.display()

    print("\nSearch key 20:", ht_chain.search(20))

    print("\n=== Open Addressing Example ===")
    ht_open = HashTableOpenAddressing(10)

    for k in keys:
        ht_open.insert(k, f"Value{k}")

    ht_open.display()

    print("\nSearch key 25:", ht_open.search(25))

    print("\n=== Collision Demonstration ===")
    collision_keys = [5, 15, 25]  # All hash to same index in modulo 10

    ht_collision = HashTableChaining(10)
    for k in collision_keys:
        ht_collision.insert(k, f"Value{k}")

    ht_collision.display()
