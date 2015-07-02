import random
#d = {'color': 'tangerine', ('pick', 'three'): ['words', 'clocks'],
#key = ('pick', 'three')
#len(d[key])
# pick random integer between 0 and length of entry
#r = random.randint(0, len(d[key]) - 1)
#randomword = d[key][r]

try:
   #f = open('sherlock-small.txt', 'r')
    f= open('sherlock.txt','r')
    lines = f.readlines()
    len(lines)
    f.close()

    # Parse the file to record all words in a list
    words = []
    for l in lines:
        if l.startswith(u"End of the Project Gutenberg EBook"):
            break
        words = words + l.split()[:]


    # Build word dictionary
    d = {}
    n = []
    for (i, word) in enumerate(words):
        # print(i, word)

        if i + 3 > len(words):
            break
        elif (words[i], words[i + 1]) in d:
            #print(d[(words[i], words[i + 1])])
            n = d[(words[i], words[i + 1])]
            n.append(words[i + 2])
            d[(words[i], words[i + 1])] = n
        else:
            d[(words[i], words[i + 1])] = [words[i + 2]]
except IOError as e:
    print(e)

# Generate random text
c = 0
newstory = []
startnum = random.randint(0, len(d) - 1)
startstring = list(d)[startnum]
endstring = d[(list(d)[startnum])]
while c < 30:
    endnum = random.randint(0, len(endstring) - 1)

    # Build a three-word chunk
    teststring = list(startstring) + endstring

    # Check if the last two words of the chunk appear as a key in d

    if (teststring[1], teststring[2]) in d and len(endstring) > 0:

        if c == 0:
            newstory.extend(teststring)
        else:
            newstory.extend(endstring)
        startstring = (teststring[1], teststring[2])
        endstring = d[(startstring)]
       #print(d[startstring])

       #print(startstring)
       #print(endstring)
        c = c + 1
        continue
    else:
        # if you hit a dead end, close the sentence and restart?
        newstory.extend('.')
        startnum = random.randint(0, len(d) - 1)
        startstring = list(d)[startnum]
        endstring = d[(list(d)[startnum])]
        c = c +1
        continue

print(' '.join(newstory))

