def all_characters(string, text):
  counts = {}
  total = len(string)
  for char in string:
    if (char in counts):
      counts[char] = counts[char] + 1
    else:
      counts[char] = 1

  for char in text:
    if (char in counts and counts[char] > 0):
      counts[char] = counts[char] - 1
      total = total - 1
    if (total == 0):
      break

  return total == 0

print(all_characters('aabbcc', 'abcdefabcdef'))
