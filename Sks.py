a = 5
b = 10

# Loop runs 8 times (i = 0 to 7)
for i in range(8):
    c = a + b
    d = 2 * c
    e = d - b
    a = e / c
    b = d + a
    print(f"Iteration {i+1}: e = {e}")

# First comparison
if e == a:
    print("Yes (e == a after loop)")
else:
    print("No (e != a after loop)")

# Second comparison
if a != e:
    x = a - e
    print(f"x = {x}")
else:
    x = 0  # define x to avoid error later if a == e
    print("No difference, so x = 0")

# Update 'a' again
a = x + e

# Third comparison
if e == a:
    print("Yes (after a = x + e)")
else:
    print("No (after a = x + e)")

# Fourth comparison
if a != e:
    y = a * e
    print(f"y = {y}")
else:
    y = 0  # avoid undefined variable
    print("No difference, so y = 0")

# Change 'a' again
if e != 0:   # avoid division by zero
    a = x / e
else:
    a = 0

# Final comparison
if e == a:
    print("Yes (after a = x / e)")
else:
    print("No (after a = x / e)")
def adjust_values(a, e):
    """
    This function adjusts 'a' so that it becomes equal to 'e'
    """
    print("\nAdjusting values so that e == a...")
    a = e
    return a


# --- Main Program ---
a = 5
b = 10

# Loop runs 8 times (i = 0 to 7)
for i in range(8):
    c = a + b
    d = 2 * c
    e = d - b
    a = e / c
    b = d + a
    print(f"Iteration {i+1}: e = {e}")

# First comparison
if e == a:
    print("Yes (e == a after loop)")
else:
    print("No (e != a after loop)")

# If not equal, perform some operations
if a != e:
    x = a - e
    print(f"x = {x}")
else:
    x = 0
    print("No difference, so x = 0")

# Update a
a = x + e

# Check again
if e == a:
    print("Yes (after a = x + e)")
else:
    print("No (after a = x + e)")

# Another operation
if a != e:
    y = a * e
    print(f"y = {y}")
else:
    y = 0
    print("No difference, so y = 0")

# Final adjustment using the function
a = adjust_values(a, e)

# Final comparison (guaranteed Yes)
if e == a:
    print("✅ Final Output: Yes (e and a are now equal)")
else:
    print("❌ Final Output: No")
