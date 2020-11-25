import random

# Setting up blockchain
class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

class Node:
    def __init__(self):
        if random.randint(0,50) < 45:
            self.data = random.randint(0,3)
        else:
            self.data = -1
        self.next = None

def addBlock(bc):
    newNode = Node()
    if bc.head == None:
        bc.head = newNode
        bc.tail = newNode
    else:
        bc.tail.next = newNode
        bc.tail = newNode

def countVotes(bc, candidates):
    ptr = bc.head

    while ptr != None:
        if ptr.data == 0:
            candidates["trump"] += 1
        elif ptr.data == 1:
            candidates["biden"] += 1
        elif ptr.data == 2:
            candidates["yang"] += 1
        ptr = ptr.next

    return candidates

def countFromTail(bc, candidates):
    vote = bc.tail.data
    if vote == 0:
        candidates["trump"] += 1
    elif vote == 1:
        candidates["biden"] += 1
    elif vote == 2:
        candidates["yang"] += 1
    return candidates

### METHOD 1
def tallyAtEnd(candidates, bc, numBlocks):
    print("Method 1")
    # Insert all votes first
    for i in range(numBlocks):
        addBlock(bc)

    # Count all votes at the end
    countVotes(bc, candidates)
    return candidates

### METHOD 2
def retallyDuring(candidates, bc, numBlocks):
    print("Method 2")
    for i in range(numBlocks):
        addBlock(bc) # Add block
        countVotes(bc, candidates) # Recount votes each time

        # Reset vote count
        if i < numBlocks-2:
            candidates = resetCands(candidates)
    return candidates

### METHOD 3
def tallyContinous(candidates, bc, numBlocks):
    print("Method 3")
    for i in range(numBlocks):
        addBlock(bc) # Add vote
        candidates = countFromTail(bc, candidates) # Update counts
    return candidates

def resetCands(candidates):
    candidates["trump"] = 0
    candidates["biden"] = 0
    candidates["yang"] = 0
    candidates["aoc"] = 0
    return candidates

def makeCands():
    candidates = {}
    candidates["trump"] = 0
    candidates["biden"] = 0
    candidates["yang"] = 0
    candidates["aoc"] = 0
    return candidates

def printResults(candidates):
    for name in candidates:
        print(str(name) + ": "+ str(candidates[name]))

# Run blockchain
if __name__ == "__main__":

    bc1 = Blockchain()
    bc2 = Blockchain()
    bc3 = Blockchain()
    candidates1 = makeCands()
    candidates2 = makeCands()
    candidates3 = makeCands()
    numBlocks = 9000000

    candidates1 = tallyAtEnd(candidates1, bc1, numBlocks)
    #candidates2 = retallyDuring(candidates2, bc2, numBlocks)
    #candidates3 = tallyContinous(candidates3, bc3, numBlocks)

    printResults(candidates1)
