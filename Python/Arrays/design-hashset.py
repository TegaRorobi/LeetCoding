
class MyHashSet:

	def __init__(self):
		self.n_buckets = 1<<13
		self.stack = [[] for _ in range(self.n_buckets)]

	def add(self, key:int):
		bucket = self.stack[key%self.n_buckets]
		if key not in bucket:
			bucket.append(key)

	def remove(self, key:int):
		bucket = self.stack[key%self.n_buckets]
		if key in bucket: 
			bucket.remove(key)

	def contains(self, key:int) -> bool:
		return key in self.stack[key%self.n_buckets]

h = MyHashSet()
h.add(123)
h.add(29234)
print(h.contains(123))
h.remove(123)
print(h.contains(123))