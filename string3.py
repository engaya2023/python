# startswith('text',start,end)
# endswith('text',start,end)
# rjust()
# Ljust()
# splitlines()
# expandtabs()
# isspace()

a = "i love python"
print(a.startswith('i'))
print(a.endswith('m'))

# index(substring,start,end)
b = " i study english"
print(b.index("e"))
print(b.index('e', 0, 10))

# rjust()
c = "aya"
print(c.rjust(10, '@'))

d = '''first  
second
third'''

f = "first\nsecond\nthird"
# return output in list
print(d.splitlines())
print(f.splitlines())

g = "i\tlove\tphp"
print(g.expandtabs(3))

three = "  "
print(three.isspace())
