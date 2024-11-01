# reverse string

def reverse(string):
    return string[::-1]
# The [::-1] slice notation returns the string in reverse order.
print(reverse("hello my name is steve"))
print(reverse("python code "))



# palindrome function
def pali(word):
    return word== word[::-1]
print(pali("salas"))
print(pali("nope"))
print(pali("hello"))
print(pali("world"))
print(pali("kak"))



# fibonacci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

print(fibonacci(7))
print(fibonacci(11))
