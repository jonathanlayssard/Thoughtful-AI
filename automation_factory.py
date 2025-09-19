"""

### Rules

Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³
or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.


"""

def is_bulky(width, height, length):
    volume = width * height * length
    return (volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150)

def is_heavy(mass):
    return mass >= 20

def sort(width, height, length, mass):
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"

    return "STANDARD"

if __name__ == "__main__":
    print(sort(100, 100, 100, 10))   # SPECIAL
    print(sort(200, 50, 50, 10))     # SPECIAL
    print(sort(50, 50, 50, 25))      # SPECIAL
    print(sort(200, 200, 200, 25))   # REJECTED
    print(sort(100, 100, 100, 20))   # REJECTED
    print(sort(150, 10, 10, 10))     # SPECIAL
    print(sort(100, 100, 100, 0))    # SPECIAL
    print(sort(0, 0, 0, 0))          # STANDARD