# Linear Feedback Shift Register
# statisticaly this will generate robust random bits
# it will take longer than the life of the universe before it repeats it self

state = (1 << 127) | 1

while True:
    print(state & 1, end = '')
    nbit = (state ^ (state >> 1) ^ (state >> 2) ^ (state >> 7)) & 1
    state = (state >> 1) | (nbit << 127)

