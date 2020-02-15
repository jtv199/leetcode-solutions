
# they are stacks
stack1 = [4,3,2,1]
stack2 = []
stack3 = []
moves = []
## how to debug better, actually look at the variables

def try3(count,f,s,t):
    if count ==0:
        move(f,t)
        return
    try3(count-1,f,t,s)
    move(f,t)
    try3(count-1,s,f,t)
    print(count,stack1,stack2,stack3)

    return

def move(f,t):
    if checkMove(f,t):
        moved = f.pop()
        t.append(moved)
        return True
    else:
        print(f"error cant move {f}->{t}")
        return False

def checkMove(f,t):
    if f == []:
        return False
    if t == []:
        print(f"{f}->{t}")
        return True
    if f[-1] < t[-1]:
        return True
    return False

if __name__ == '__main__':
    try3(4,stack1,stack2,stack3)
