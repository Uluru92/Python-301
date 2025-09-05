# Pick one of the abstract data structures mentioned in this section that you have not yet implemented
# Build a custom Python class that demonstrates its functionality 
# Compare your solution to: https://github.com/david-legend/python-algorithms/tree/main/data-structures/src

# Solution: Hash Table using a size of 10 buckets!

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # each bucket is a list (chain)

    def _hash(self, key):
        """Simple hash function: use Python's built-in hash, then mod by size."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert or update a key-value pair."""
        index = self._hash(key)
        bucket = self.table[index]

        # Check if key already exists → update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        # Otherwise, add new
        bucket.append((key, value))

    def get(self, key):
        """Retrieve value for a key, or None if not found."""
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Remove a key-value pair if it exists."""
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def __repr__(self):
        return str(self.table)


# Example usage
ht = HashTable()

ht.insert("dog", "animal")
ht.insert("cat", "animal")
ht.insert("car", "vehicle")
ht.insert("python", "programming language")

print("HashTable:", ht)

print("Get 'cat':", ht.get("cat"))
print("Get 'python':", ht.get("python"))

ht.delete("car")
print("Hash Table after deleting 'car':", ht)
