# ChemDone

## Installation
ChemDone automatically installs dependencies upon the first run. How cool is that?

## Setup
After downloading ChemDone, all you have to do is have the file in the same directory as a terminal session to run it. If the file `chemdone.py` is alone on your desktop, the following script will run it as is:
``` bash
$ cd Desktop
$ python3 chemdone.py
```

If you want to get fancy, you can do this:
``` bash
$ cd Desktop
$ chmod u+x chemdone.py
$ ./ chemdone.py
```

If you want to be a show off: (be careful, you should only do this one if you know what you're doing)
``` bash
$ cd Desktop
$ chmod u+x chemdone.py
$ cp ./chemdone.py /usr/bin/chemdone
$ chemdone
```

If none of these work, either you're on Windows, or you're including the `$` in the command. Don't do either.

## Usage
ChemDone has several functions. It can give molar masses like so:
``` bash
$ python3 chemdone.py H2O
18.015287
```

It can balance equations as you see here:
``` bash
$ python3 chemdone.py 'CH4 + O2 -> H2O + CO2'
Balanced Equation:  CH4 + 2O2 -> 2H2O + CO2
Molar Masses:  16.042504 31.99881 18.015287 44.00955
```

And it can do some stoichiometry like this:
``` bash
$ chemdone.py 'Mg + AgNO3 -> Mg(NO3)2 + Ag' '{"AgNO3" : ".026l2.5m", "Mg" : 1.53}'
Balanced Equation:  Mg + 2AgNO3 -> Mg(NO3)2 + 2Ag
Molar Masses:  24.3051 169.873118 148.31493600000002 107.8682
Limiting Reactant:  AgNO3
Theoretical Moles:  0.0325 0.065 0.0325 0.065
Theoretical Masses:  0.7899158 11.0417527 4.8202354 7.011433
```
In this example, the thing in curly brackets off to the side is a set of givens. `"AgNO3" : ".026l2.5m"` says that we have .026 liters (`.026l`) of 2.5 M (`2.5m`) solution of Silver Nitrate (`"AgNO3"`). `"Mg" : 1.53` says that we have 1.53 grams (`1.53`) of Magnesium `Mg`. You can also specify mole amounts. If you, instead, wanted to say that there are 1.53 moles of magnesium, you would replace the `1.53` with `"1.53m"`.

## Disclaimer
We at ChemDone don't encourage academic dishonesty, so don't use this to do your homework or anything like that. That wouldn't be very nice. Just use it to check your practice work or something like that. We have used it in conjunction with a random chemical equation generator to create and check practice problems.
