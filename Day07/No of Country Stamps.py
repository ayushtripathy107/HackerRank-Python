# Read the total number of stamps
n = int(input())

# Initialize an empty set to store unique country names
country_set = set()

# Loop N times to read each country name and add it to the set
for _ in range(n):
    country_name = input().strip()
    country_set.add(country_name)

# The size of the set represents the number of distinct stamps
print(len(country_set))



