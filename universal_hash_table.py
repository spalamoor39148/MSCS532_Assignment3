import random

class UniversalHash:
    """
    Universal hash function family for integers:
    h(k) = ((a * k + b) mod p) mod m
    where:
    - a, b are random integers,
    - p is a prime number,
    - m is the table size.
    """
    def __init__(self, table_size, prime):
        self.m = table_size
        self.p = prime
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def __call__(self, key):
        int_key = hash(key)
        return ((self.a * int_key + self.b) % self.p) % self.m

def next_prime(n):
    """Find next prime number greater than or equal to n."""
    def is_prime(x):
        if x < 2:
            return False
        if x in (2, 3):
            return True
        if x % 2 == 0:
            return False
        r = int(x**0.5)
        for i in range(3, r + 1, 2):
            if x % i == 0:
                return False
        return True

    while not is_prime(n):
        n += 1
    return n

class HashTable:
    def __init__(self, size=10, prime=101, load_factor_threshold=0.7):
        self.size = size
        self.prime = prime
        self.load_factor_threshold = load_factor_threshold
        self.table = [[] for _ in range(self.size)]
        self.hash_function = UniversalHash(self.size, self.prime)
        self.num_elements = 0

    def _get_index(self, key):
        return self.hash_function(key)

    def _resize(self):
        old_table = self.table
        old_size = self.size

        # Increase size and prime
        new_size = next_prime(self.size * 2)
        self.size = new_size
        self.prime = next_prime(self.prime * 2)
        self.table = [[] for _ in range(self.size)]
        self.hash_function = UniversalHash(self.size, self.prime)
        self.num_elements = 0

        # Rehash existing elements
        for chain in old_table:
            for key, value in chain:
                self.insert(key, value)

    def insert(self, key, value):
        index = self._get_index(key)

        # Update if key exists
        for i, (existing_key, _) in enumerate(self.table[index]):
            if existing_key == key:
                self.table[index][i] = (key, value)
                return

        # Insert new key-value pair
        self.table[index].append((key, value))
        self.num_elements += 1

        # Resize if load factor exceeded
        if self.num_elements / self.size > self.load_factor_threshold:
            self._resize()

    def search(self, key):
        index = self._get_index(key)
        for existing_key, value in self.table[index]:
            if existing_key == key:
                return value
        return None

    def delete(self, key):
        index = self._get_index(key)
        for i, (existing_key, _) in enumerate(self.table[index]):
            if existing_key == key:
                del self.table[index][i]
                self.num_elements -= 1
                return

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Bucket {i}: {chain}")

if __name__ == "__main__":
    ht = HashTable(size=5, prime=11)

    print("Inserting key-value pairs:")
    for i in range(20):
        ht.insert(f"key{i}", i)
    ht.display()

    print("\nSearch results:")
    print(f"Search 'key10': {ht.search('key10')}")
    print(f"Search 'key19': {ht.search('key19')}")
    print(f"Search 'nonexistent_key': {ht.search('nonexistent_key')}")

    print("\nDeleting 'key10' and 'key19':")
    ht.delete('key10')
    ht.delete('key19')
    ht.display()
