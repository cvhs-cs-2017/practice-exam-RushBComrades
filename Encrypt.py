"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""
def void(o):
    v = "aeiouAEIOU"
    w = ""
    for x in o:
        if x in v:
            x = "#"
        w += x
    return w
print(void("AP"))
