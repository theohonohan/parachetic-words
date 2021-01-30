from collections import defaultdict

#words_file = open("linuxwords.txt")
words_file = open("collins_scrabble.txt")

words = words_file.read().split()

patterns = defaultdict(list)
results = defaultdict(list)

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

# Initial partition.  Tag each word with the the pattern of repeated
# letters, e.g. HAMMERS -> HA22ERS,  LITTORAL -> 0I22ORA0.
for word in words:
  # First find the repeated letters.  For each letter that's
  # repeated, remember the index of the first time we saw it.
  seen = {}
  dups = {}
  for index, character in enumerate(word.lower()):
    if character in dups:
      pass
    elif character in seen:
      dups[character] = seen[character]
    else:
      seen[character] = index
  # A word with no repeated letters is not interesting at all.
  if len(dups) == 0:
    continue
  # Now replace each duplicated letter with the index of
  # its first occurrence, to get the partition key.
  sequence = []
  for character in word.lower():
    if character in dups:
      sequence.append(dups[character])      
    else:
      sequence.append(character)
  tup = tuple(sequence)
  if len(dups) == 1:
    # There is only one repeated letter, so the set of
    # words with this tag needs no further partitioning:
    results[tup].append(word)
  else:
    # Multiple repeated letters, so we will need a second pass
    # to figure out which words match and which don't.
    patterns[tup].append(word)


def compare(val):
  for index in range(len(val)):
    word1 = val[index]

    for index2 in range(index + 1, len(val)):
      word2 = val[index2]
      if check_word_property(word1,word2):
            count = 0
            descriptor = []
            for a, b in zip(word1.lower(), word2.lower()):
              if a != b:
                descriptor.append(count)
              else:
                descriptor.append(a)
              count += 1
            results[tuple(descriptor)].append(word1)
            results[tuple(descriptor)].append(word2)


for val in patterns.values():
  # Partition again based on which letter(s) have to
  # change to get from one word to another.
  compare(val)

for s in results.values():
  if len(s) > 1:
    print(set(s))
