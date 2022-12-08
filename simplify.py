def simplify(txt):
    numer = int(txt.split("/")[0])
    deno = int(txt.split("/")[1])
    if numer // deno == numer / deno:
        return numer // deno
    else:
        return str(numer // common_factor(numer, deno)) + "/" + str(deno // common_factor(numer, deno))

def common_factor(a, b):
    while(b != 0):
        temp = b
        b = a%b
        a = temp
    return a

print(simplify("100/400"))
print(simplify("8/4"))
print(simplify("10/11"))
print(simplify("4/6"))
print(simplify("114/514"))



