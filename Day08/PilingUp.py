import sys
from collections import deque

def can_stack():
    # Read number of test cases
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        t = int(line1.strip())
    except EOFError:
        return

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        # Use a deque for efficient popping from both ends
        blocks = deque(map(int, sys.stdin.readline().split()))
        
        last_picked = float('inf')
        possible = True
        
        while blocks:
            # Choose the larger of the two ends
            if blocks[0] >= blocks[-1]:
                current = blocks.popleft()
            else:
                current = blocks.pop()
            
            # If current block is bigger than the previous one, it's impossible
            if current > last_picked:
                possible = False
                break
            
            last_picked = current
            
        print("Yes" if possible else "No")

if __name__ == "__main__":
    can_stack()
