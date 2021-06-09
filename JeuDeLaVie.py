import curses

def next_state (state):
    new_state = []
    
    for i in range(len(state)):
        line = ["."]*len(state[i])
        new_state.append(line)
    
    for y in range(len(state)):

        for x in range(len(state[y])):
            neighbours = 0
            for i in range(-1,2):
                for j in range(-1,2): 
                    if y + i >= 0 and y + i < len(state) \
                    and x + j >= 0 and x + j < len(state[y]) \
                    and state[y + i][x + j] == "O" \
                    and not (i == 0 and j == 0):
                        neighbours += 1 
            if state[y][x] == "." and neighbours == 3:
                new_state[y][x] = "O"
            elif state[y][x] == "O" and neighbours == 2 or neighbours == 3:
                new_state[y][x] = "O"
            else: 
                new_state[y][x] = "."

    return new_state

def main (stdscr):
        
    curses.curs_set(False) 
    
    text_file = open("cells.txt", "r")
    state = text_file.read().splitlines()
    
    key = " "
    while key != "q":
            
        stdscr.clear()
            
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == "O":
                    stdscr.addstr(i, j, "O")    
            
        stdscr.refresh()
        
        state = next_state(state)
        
        key = stdscr.getkey()


curses.wrapper(main)