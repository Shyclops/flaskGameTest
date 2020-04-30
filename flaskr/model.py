max_chain = 1
state = None

def create_state(r, c):
    try:
        global state 
        state = [[1] * c for i in range(r)]
        return True
    except:
        return False


def update_state(r, c, chain=0):
    global state
    try:
        if state[r][c] == 0:
            state[r][c] = 1
        else:
            state[r][c] = 0
        if chain != max_chain:
            if r != 0:
                update_state(r-1,c,1)
            if r != len(state):
                update_state(r+1,c,1)
            if c != 0:
                update_state(r,c-1,1)
            if c != len(state[0]):
                update_state(r,c+1,1)
        return True
    except:
        return False

def get_state():
    if state == None:
        return False
    else:
        return state



