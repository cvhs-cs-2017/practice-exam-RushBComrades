def void(o):
    v = "EeFfLlIiAa"
    w = ""
    for x in o:
        if x in v:
            if x == "e":
                x = "Windows 98"
            if x == "E":
                x = 'WIndows 98'
            if x == 'F':
                x = 'WINdows 98'
            if x == 'f':
                x = 'WINDows 98'
            if x == 'l':
                x = 'WINDOws 98'
            if x == "L":
                x = "WINDOWs 98"
            if x == "l":
                x = 'WINDOWS 98'
            if x == 'I':
                x = 'WiNDOWS 98'
            if x == 'i':
                x = 'WInDOWS 98'
            if x == 'A':
                x = 'WINdOWS 98'
            if x == 'a':
                x = 'WINDoWS 98'
        w += x
    return w
print(void("The lazy Student Never Gets Paid!"))
