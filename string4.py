# isidentifier()
# isalpha()
# isalnum()
# replace()
# join(iterable) loop list to string
# old formatting & control floating number
# slicing string

# isidentifier()
one = "aya_mohamed"
two = "AyaMohamed"
three = "aya--mohamed"

print(one.isidentifier())  # true
print(two.isidentifier())  # true
print(three.isidentifier())  # false

# isalpha()
x = "AaaaBaa"

# isalnum()
y = "Aaa123Bbbcc"

print(x.isalpha())
print(x.isalnum())

print("#" * 30)
# join()
names = ["aya", "ola", "alia"]
print("-".join(names))

# replace()
words = " Hello world one two three one "
print(words.replace("one", "1", 2))
print(words.replace("one", "yoyo", words.count("one")))

a = "hello world aya , welcome back aya "
print(a.count("aya"))

# old formatting
name = "aya"
age = 100
rank = 10

print("my name is :" + name)
# print("my name is : " + name , "my age is :" + age)
print("my name is :%s" % name)
print("my name is : %s and my age is: %d" % (name, age))
print("my name is : %s and my age is :%d and my rank is : %f" % (name, age, rank))

# control floating number
print("my name is : %s and my age is :%d and my rank is : %.2f" % (name, age, rank))

# slicing string
string = "Hello world i love pyhon"
print("Message is %.7s" % string)


