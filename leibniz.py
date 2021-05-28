# User input for amount of terms
numTerms = int(input("Input number of terms: "))

# Create list for all terms
allTerms = []

# Calculate the terms and place them in the list
for n in range(numTerms):
    allTerms.append((float(-1) ** n) / (float(2) * n + float(1)))

# Sum all terms and multiply by 4
pi = sum(allTerms) * 4

# Display the result
print(f'Estimation: {pi} ({numTerms} terms)')
