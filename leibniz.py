
# User input for amount of terms
print("Input number of terms:")
r = input()

# Create list for all terms
s = []

# Calculate the terms and place them in the list
for n in range(r):
    a = float(-1) ** n
    b = float(2) * n + float(1)
    c = a / b
    s.append(c)

# Sum all terms and multiply by 4
pd = sum(s)
pi = pd * 4

# Convert the result into a string
pistr = str(pi)
rstr = str(r)

# Display the result
print "Estimation: " + pistr + " (" + rstr + " terms)"
