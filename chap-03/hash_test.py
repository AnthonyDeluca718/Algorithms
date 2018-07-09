from hash import Hash

hash_map = Hash()

hash_map.set('A', 1)
hash_map.set('B', 2)
hash_map.set('C', 3)
for n in range(100):
  hash_map.set(str(n), n)
hash_map.set('100', 'one hundred')

print(hash_map.count)
print (hash_map.remove('A'))
print(hash_map.get('A'))
print(hash_map.count)
