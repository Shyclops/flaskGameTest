max_chain = 1

def create_state(r, c):
    try:
        global state 
        state = [[0] * r for i in range(c)]
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
            update_state(r+1, c, 1)
            update_state(r-1, c, 1)
            update_state(r, c+1, 1)
            update_state(r, c-1, 1)
        
        return True
    except:
        return False

def get_state():
    return state



