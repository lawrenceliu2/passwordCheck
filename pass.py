def check(password):
    if len([x for x in password if x.isupper()])>0 and len([x for x in password if x.isdigit()])>0 and len([x for x in password if x.islower()])>0:
        return True
    else:
        return False

print check("potato")
print check("Potato")
print check("123")
print check("potato1")
print check("Potato123")

def strengthCheck(password):
    strength = 0
    specials = ['.', '?', '!', '&', '#', ',', ';', ':', '-', '_', '*']
    if len([x for x in password if x.islower()])>0:
        strength+=1
        if len([x for x in password if x.isupper()])>0:
            strength+=1
        if len([x for x in password if x.isdigit()])>0:
            strength+=1
    if len([x for x in password if x.isupper()])>0:
        strength+=1
        if len([x for x in password if x.isdigit()])>0:
            strength+=1
    if len([x for x in password if x.isdigit()])>0:
        strength+=1
    if len([x for x in password if x in specials])>0:
        if len([x for x in password if x in specials])>5:
            strength+=6
        else:
            strength+=len([x for x in password if x in specials])
    return strength

print strengthCheck("potato")
print strengthCheck("Potato")
print strengthCheck("123")
print strengthCheck("Potato123")
print strengthCheck("Potato123!")
print strengthCheck("Potato123!,?")
print strengthCheck("Potato123!,?!!#@$@#$#$")
