import sys

def solve():
    # Read n and m
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        n, m = map(int, line1)
        
        # Read the array elements
        arr = list(map(int, sys.stdin.readline().split()))
        
        # Read set A and set B
        set_a = set(map(int, sys.stdin.readline().split()))
        set_b = set(map(int, sys.stdin.readline().split()))
        
        happiness = 0
        
        # Iterate through the array to calculate happiness
        for i in arr:
            if i in set_a:
                happiness += 1
            elif i in set_b:
                happiness -= 1
                
        print(happiness)
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
