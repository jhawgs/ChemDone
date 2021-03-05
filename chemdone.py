#!/usr/bin/python3

from os import system
system("python3 -m pip install --upgrade chempy molmass --user")

from sys import argv
from chempy import balance_stoichiometry
from molmass import Formula

try:
    argv[1]
except:
    print("""


    usage:

        python3 chemdone.py 'reac1 + reac2 + ... -> prod1 + prod2 + ...'\\
            '{"molecule" : known_mass, "molecule" : "<known_moles>m"}'
        
        or

        python3 chemdone.py substance


    """)
    exit()

molecules = False
try:
    argv[3]
    molecules = True if str(argv[3]) == "molecules" else False
except:
    pass

def merge(dict1, dict2):
    ret = {}
    for i in list(dict1.keys()):
        ret[i] = dict1[i]
    for i in list(dict2.keys()):
        ret[i] = dict2[i]
    return ret

reaction = str(argv[1])

if not "->" in reaction and not "+" in reaction:
    print(Formula(reaction).mass)
    exit()

calc_gram = True
try:
    grams_in = eval(str(argv[2]))
except IndexError:
    calc_gram = False
if calc_gram:
    for i in list(grams_in.keys()):
        if type(grams_in[i]) == type(""):
            if "m" in grams_in[i] and "l" in grams_in[i]:
                grams_in[i] = grams_in[i].replace(" ", "")
                if grams_in[i][-1] == "m":
                    split = grams_in[i].split("l")
                elif grams_in[i][-1] == "l":
                    split = grams_in[i].split("m")
                grams_in[i] = float(split[0]) * float(split[1][:-1]) * Formula(i).mass
            elif grams_in[i][-1] == "m":
                grams_in[i] = Formula(i).mass * float(grams_in[i][:-1])
            else:
                grams_in[i] = float(grams_in[i])

reaction = reaction.replace(" ", "")
reaction = reaction.replace("\t", "")
reaction = reaction.replace("\n", "")
reaction = reaction.replace("\r", "")

[_reactants, _products] = reaction.split("->")

reactants = []
for i in _reactants.split("+"):
    reactants.append(i)

products = []
for i in _products.split("+"):
    products.append(i)

for (i, n) in enumerate(products):
    j = n
    while j[0] in [str(i) for i in range(10)]:
        j = j[1:]
    products[i] = j

for (i, n) in enumerate(reactants):
    j = n
    while j[0] in [str(i) for i in range(10)]:
        j = j[1:]
    reactants[i] = j

reac, prod = balance_stoichiometry(reactants, products)

reac_string = ""
for i, n in reac.items():
    if not reac_string == "":
        reac_string += " + "
    reac_string += str(n if not n == 1 else "") + i

prod_string = ""
for i, n in prod.items():
    if not prod_string == "":
        prod_string += " + "
    prod_string += str(n if not n == 1 else "") + i

print("Balanced Equation: ", reac_string + " -> " + prod_string)

molar_masses = merge({i : Formula(i).mass for i, _ in reac.items()}, {i : Formula(i).mass for i, _ in prod.items()})

print("Molar Masses: ", *[molar_masses[i] for i in list(molar_masses.keys())])

if calc_gram:
    if len(list(grams_in.keys())) > 1:
        allposs = []
        mol = []
        for i in list(grams_in.keys()):
            if i in [n for n, _ in reac.items()]:
                mole = (grams_in[i]/molar_masses[i])/reac[i]
            else:
                mole = (grams_in[i]/molar_masses[i])/prod[i]
            moles = merge({i: mole * n for i, n in reac.items()}, {i: mole * n for i, n in prod.items()})
            allposs.append(i)
            mol.append(mole)
        limiting = allposs[mol.index(min(mol))]
        print("Limiting Reactant: ", limiting)
        grams_in = {limiting : grams_in[limiting]}
    if list(grams_in.keys())[0] in [i for i, _ in reac.items()]:
        mole = (grams_in[list(grams_in.keys())[0]]/molar_masses[list(grams_in.keys())[0]])/reac[list(grams_in.keys())[0]]
    else:
        mole = (grams_in[list(grams_in.keys())[0]]/molar_masses[list(grams_in.keys())[0]])/prod[list(grams_in.keys())[0]]
    moles = merge({i: mole * n for i, n in reac.items()}, {i: mole * n for i, n in prod.items()})
    print("Theoretical Moles: ", *[str(round(float(moles[i]), 7)) for i in list(moles.keys())])
    print("Theoretical Masses: ", *[str(round(float(molar_masses[i] * moles[i]), 7)) for i in list(molar_masses.keys())])
    if molecules:
        print("Theoretical Molecules: ", *[str(round(float(float(moles[i]) * 6.022e+23), 7)) for i in list(moles.keys())])
