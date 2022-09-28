from keys import messages as msg
from query import get_command


print(msg[0])
inp = ''
# while inp != '/exit':
inp = input(msg[1])
get_command(inp)
