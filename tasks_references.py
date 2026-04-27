def make_multiplier(n):
    print("Я думаю что это 1 вывод")
    print("n = ",n)

    def multiply(x):
        print("Я думаю что это 3 вывод ")
        print("x = ", x)
        return x * n

    print("Я думаю что это 2 вывод (среди строк, передо мной должна n выводится)")
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
sto = make_multiplier(100)
print(double(4))  # 10
print(triple(6))  # 15
print(sto(5))

print("========================================================================")

print(id(double))
print(id(triple))
print(id(sto))
print(double is triple)

'''
раз
два
три
'''