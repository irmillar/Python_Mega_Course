temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        return f

# Create a new file to write to
with open("temp.txt", "w") as temp:
    temp.write("")

for t in temperatures:
    with open("temp.txt", "a") as temp:
        temp.write(f"{c_to_f(t)}\n")

with open("temp.txt", "r") as temp:
    print(temp.read())
