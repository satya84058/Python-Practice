# --- Function Definitions ---

def calculate_values(a, b):
    """Performs calculations and returns updated values."""
    c = a + b
    d = 2 * c
    e = d - b
    a = e / c
    b = d + a
    return a, b, c, d, e


def adjust_values(a, e):
    """Adjusts 'a' so that it becomes equal to 'e'."""
    print("\nAdjusting values to make e == a...")
    a = e
    return a


# --- Main Program Starts Here ---

# Initial values
a = 5
b = 10

print("----- Starting the Loop -----")
# Run loop 8 times
for i in range(8):
    a, b, c, d, e = calculate_values(a, b)
    print(f"Iteration {i+1}: e = {e:.2f}, a = {a:.2f}, b = {b:.2f}")

print("\n----- After Loop Ends -----")

# First comparison
if e == a:
    print("Yes (e == a after loop)")
else:
    print("No (e != a after loop)")

# If not equal, calculate x
if a != e:
    x = a - e
    print(f"x = {x:.2f}")
else:
    x = 0
    print("No difference, so x = 0")

# Update a using x
a = x + e
print(f"Updated a = {a:.2f}")

# Check again
if e == a:
    print("Yes (after a = x + e)")
else:
    print("No (after a = x + e)")

# Perform another operation
if a != e:
    y = a * e
    print(f"y = {y:.2f}")
else:
    y = 0
    print("No difference, so y = 0")

# --- Adjust values so final output becomes YES ---
a = adjust_values(a, e)

# Final comparison (guaranteed Yes)
if e == a:
    print("\n✅ Final Output: Yes (e and a are now equal!)")
else:
    print("\n❌ Final Output: No (something went wrong)")
