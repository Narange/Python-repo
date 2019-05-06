global1 = "global 1"
global2 = "global 2"

def do_it():
    global global1, global2
    global1 += "plus local"

    print(global1)


    global2 += "plus local"

    print(global2)

do_it()