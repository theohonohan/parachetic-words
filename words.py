from collections import defaultdict

#words_file = open("linuxwords.txt")
words_file = open("collins_scrabble.txt")

words = words_file.read().split()

results = defaultdict(list)

# Tag each word with the the pattern of repeated letters:
# HAMMERS -> HA__ERS
# Words with multiple repeated letters get multiple tags:
# LITTORAL -> _ITTORA_ *and* LI__ORAL
for word in words:
  # First find the repeated letters.
  seen = set()
  dups = set()
  for character in word.lower():
    if character in seen:
      dups.add(character)
    else:
      seen.add(character)

  # Add this to the set of words with each tag that applies.
  for dup in dups:
    tag = word.lower().replace(dup, '_')
    results[tag].append(word)

for s in results.values():
  if len(s) > 1:
    print(set(s))
