from itertools import product

# Read K and M
k, m = map(int, input().split())

# Read each list, squaring the elements and taking modulo M immediately
# We ignore the first element of each line (Ni)
lists = []
for _ in range(k):
    row = list(map(int, input().split()))[1:]
    squared_row = [(x**2) % m for x in row]
    lists.append(squared_row)

# Generate all possible combinations (Cartesian product)
max_s = 0
for combination in product(*lists):
    # Calculate S = (f(X1) + f(X2) + ... + f(Xk)) % M
    current_s = sum(combination) % m
    if current_s > max_s:
        max_s = current_s

print(max_s)
