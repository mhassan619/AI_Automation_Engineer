## lets discuss about Generators
# A function that gives only one value at one time
# Normal Function - returns whole list
def get_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(i * 2)
    return numbers # sab eik saath memory mein

# Generator - ek ek karke deta hai
def get_numbers_gen(n):
    for i in range(n):
        yield i * 2         # yield = eik value do aur ruk jao
# use karo:
for num in get_numbers_gen(5):
    print(num)
print(get_numbers(5))

# Generator expression - like list compression
gen = (x * 2 for x in range(5))
print(next(gen)) # 0
print(next(gen)) # 2
print(next(gen)) # 4