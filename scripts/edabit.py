def amplify(num):
    return [i * 10 if i % 4 == 0 else i for i in range(1, num + 1)]


print(amplify(1))
print(amplify(10))
