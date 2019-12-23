from collections import defaultdict

words_file = open("linuxwords.txt")
#words_file = open("collins_scrabble.txt")

words = words_file.read().split()

patterns = defaultdict(list)

def check_word_property(word1, word2):
  xfrm = []
  swaps = 0

  for a, b in zip(word1.lower(), word2.lower()):
    if a != b: 
      xfrm.append((a,b)) 
      swaps += 1
    if len(set(xfrm)) > 1:
      return False
  
  if swaps > 1:
    return True

def word_distance(first, second):
  count = 0
  for a, b, in zip(first.lower(),second.lower()):
    if a!=b: count += 1
  return count

for word in words:
  sequence = []
  for character in word.lower():
    sequence.append(word.lower().find(character))
  tup = tuple(sequence)
  patterns[tup].append(word)

def search(vals):
  for val in vals:
    compare(val)

def join(list):
  new_list = []
  for item in list:
    new_list.extend(item)
  return set(new_list)

def compare(val):
  for index in range(len(val)):
    word1 = val[index]

    for index2 in range(index,len(val)):
      word2 = val[index2]
      if word1 != word2:
        if word_distance(word1, word2) > 1:
          if check_word_property(word1,word2):
            count = 0
            descriptor = []
            for a, b in zip(word1.lower(), word2.lower()):
              if a != b:
                descriptor.append(count)
              else:
                descriptor.append(a)
              count += 1
            results[tuple(descriptor)].append([word1,word2])


vals = patterns.values()

results = defaultdict(list)

search(vals)

for s in results.values():
  s = join(s)
  print(s)
