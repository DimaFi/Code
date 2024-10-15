
END_MARKER = -2 * 10**9


prev = int(input())

ascending = True
descending = True
constant = True

while True:
    current = int(input())
    
    if current == END_MARKER:
        break
    
    if current > prev:
        descending = False
        constant = False  
    elif current < prev:
        ascending = False 
        constant = False  
    else:
        ascending = False 
        descending = False

    
    prev = current



if constant:
    print("CONSTANT")
elif ascending and not descending:
    print("ASCENDING")
elif descending and not ascending:
    print("DESCENDING")
elif not ascending and not descending:
    print("RANDOM")
elif ascending:
    print("WEAKLY ASCENDING")
elif descending:
    print("WEAKLY DESCENDING")