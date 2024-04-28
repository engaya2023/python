# method
# len()
# strip()
# title()
# capitalize ()
# zfill()
# upper()
# split()
# center()
# count()
# swaps()


# len()
msg = "i love python"
print(len(msg))
print(msg.strip())

# title()
b = " i love python and 3g "
print(b.title())

# capitalize()
c = " i love python and 3g "
print(c.capitalize())

#  zfill()
x, y, z = "1", "2", "111"
print(x.zfill(4))
print(y.zfill(4))
print(z.zfill(4))

# upper()
g = "aya"
print(g.upper())

# lower()
h = "AYA"
print(h.lower())

# split()
v = "i love python and php "
print(v.split())
star = "i love python and php "
print(star.split("-", 2))

# center() centralize word in text and move it num of spaces
e = "osama"
print(e.center(10))

# count("text",start,end) iteration of word
word= "i start with python and i love python "
print(word.count("python"))
print(word.count("python",0,10))


# swap case() turn capital to small and reverse
zz = "i love python"
print(zz.swapcase())

xx= "I LOVE PYTHON"
print(xx.swapcase())

