### Program to calculate the Electronic Configuration of an element using its atomic number
### Designed and programmed by Harivansh Mehta.
### Copyright © 2022
### All rights reserved.

## THE MAIN PYTHON CODE THAT WORKS UNDERNEATH THE HOOD

from elec_config_data import elements

def key(dict, elem): # A QoL function for accessing the key of a dictionary element from its value.
    return list(dict.keys())[list(dict.values()).index(elem)]

def superscript(x):  # Another QoL function to return superscripts.
    normal = "0123456789"
    super = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    res = x.maketrans(''.join(normal), ''.join(super)) 
    return x.translate(res)

orbitals = { # Key-value pairs of orbitals and their azimuthal (secondary) quantum number values
    0 : 's',
    1 : 'p',
    2 : 'd',
    3 : 'f'
}

iupacNames = { # Key-value pairs of numbers and their IUPAC nomenclature for elements with atomic number > 119
    0 : 'nil',
    1 : 'un',
    2 : 'bi',
    3 : 'tri',
    4 : 'quad',
    5 : 'pent',
    6 : 'hex',
    7 : 'sept',
    8 : 'oct',
    9 : 'enn'
}

subshells = []

for i in range(1,10):
    for j in ['s','p','d','f']:
        if key(orbitals, j) < i:
            subshells.append(str(i)+j) # Creates a list of all possible subshells for principal quantum numbers 1 to 9 (i.e, from 1s to 9f). This range can be modified as per need.

subshells_dict = {}

for i in subshells:
    subshells_dict[i] = int(i[0])+ key(orbitals, i[1])
subshells = [i[0] for i in sorted(subshells_dict.items(), key = lambda x : x[1])] # Sorts the list according to their ascending n+l value as per Aufbau principle.

electrons = { # Key-value pairs of orbitals and their maximum electron capacity
    's' : 2,
    'p' : 6,
    'd' : 10,
    'f' : 14
}

def electronicConfiguration(n): # MAIN FUNCTION
    if n == 24: # Exceptional electronic configuration of Chromium
        return "1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d⁵"
    elif n == 29: # Exceptional electronic configuration of Copper
        return "1s² 2s² 2p⁶ 3d² 3p⁶ 4s¹ 3d¹⁰"
    global subshells, electrons
    at = 0
    li = []
    for i in subshells:
        k = 0
        if at == n:
            break
        sub = electrons[i[1]]
        k = min(n-at, sub) # If subshell is fully filled, adds the max number of electrons, else, adds the number of electrons left
        li.append(i+superscript(str(k)))
        at+=k
    return ' '.join(li)

def iupacName(n): # Function to define the names of elements with atomic number more than 119 (not present in periodic table).
    global iupacNames
    li = list(str(n))
    st = ""
    sym = ""
    for i in li:
        st += iupacNames[int(i)]
        sym += iupacNames[int(i)][0]
    st += 'ium'
    return st.capitalize() + " (" + sym.capitalize() + ")"

def elemSearch(n): # Searches the elements by atomic number in the elements dictionary and returns the names of the element.
    global elements
    return elements[n][0] + " (" + elements[n][1] + ")"

def elemSymbol(n): # Returns the symbol of the element
    return elements[n][1]

if __name__ == "__main__":
    n = int(input("Enter the atomic number of the element: "))
    if n <= 118: # For elements present in periodic table, their proper name is used.
        elem = elemSearch(n)
    else:
        elem = iupacName(n) # For elements not present in periodic table, their IUPAC name is used.
    print(f"The electronic configuration of the element {elem} having atomic number {n} is:", electronicConfiguration(n), sep = "\n")