print('--------1--------')
text = input()
def f(text):
    return len(text.split())

print(f(text))


print('------2--------')
text = input()
def f(text):
    ct = 0
    for i in text:
        if i == "(" or i == "[" or i == "{":
            ct += 1
        elif i == ")" or i == "}" or i == "}":
            ct -= 1
            if ct < 0:
                print("не сбалансировано")
                return False
    return print("сбалансировано")
print(f(text))



print('-----3-----')
# не знаю!!!!

def f(a):
    n = [i for i,x in enumerate(a) if x <0]
    s = sum(a[n[0] + 1: a[-1]]) if len(n) > 1 else 0
    res = [x for x in a if abs(x)>4]
    res += [0]*(len(a) - len(res))
    return s, res
print()








