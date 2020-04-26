max_chain = 1

def create_state(int r, int c):
    global state = [[0] * r for i in range(c)]


def update_state(int r, int c, int chain=0):
    if state[r][c] = 0:
        global state[r][c] = 1
    else:
        global state[r][c] = 0

    if chain != max_chain:
        update_state(r+1, c, 1)
        update_state(r-1, c, 1)
        update_state(r, c+1, 1)
        update_state(r, c-1, 1)

def get_state():
    return state



