#Description
I wonder what this really is... [enc](https://mercury.picoctf.net/static/e47483f88b12f2ab0c46315afc12f64d/enc) ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])


The python code shown shows appending the values of two ASCII characters by bitshifting the first one, then converting the resulting value to a character. This was easily reversed, with the code used in solution.py


