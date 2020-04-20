# 1
# n = int(input())
# k = int(input())
# print(n // 10 ** k)

# 2
a = int(input())
b = int(input())
print((a + (b - a % b) % b) // b)  # округление вверх
