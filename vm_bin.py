pointer = 0
VARS = [None]
DATA = [None] * len(VARS)


def get_two_params():
  pointer += 1
  val1 = COMMANDS[pointer]
  pointer += 1
  val2 = COMMANDS[pointer]
  pointer += 1
  return val1, val2


def add():
  num1, num2 = get_two_params()
  DATA[num1] += DATA[num2]

def sub():
  num1, num2 = get_two_params()
  DATA[num1] -= DATA[num2]

def mul():
  num1, num2 = get_two_params()
  DATA[num1] *= DATA[num2]

def div():
  num1, num2 = get_two_params()
  DATA[num1] /= DATA[num2]

def idiv():
  num1, num2 = get_two_params()
  DATA[num1] //= DATA[num2]

def mod():
  num1, num2 = get_two_params()
  DATA[num1] %= DATA[num2]

def mov():
  name, val = get_two_params()
  DATA[name] = val

def movm():
  name, val = get_two_params()
  DATA[name] = DATA[val]

def cmp():
  num1, num2 = get_two_params()
  DATA[VARS['num1']] = DATA[num1]
  DATA[VARS['num2']] = DATA[num2]

# условия:
def eq():
  if DATA[VARS['num1']] == DATA[VARS['num2']]:
    pointer = COMMANDS[pointer + 1]
  else:
    pointer += 2

def ne():
  if DATA[VARS['num1']] != DATA[VARS['num2']]:
    pointer = COMMANDS[pointer + 1]
  else:
    pointer += 2

def lt():
  if DATA[VARS['num1']] < DATA[VARS['num2']]:
    pointer = COMMANDS[pointer + 1]
  else:
    pointer += 2

def gt():
  if DATA[VARS['num1']] > DATA[VARS['num2']]:
    pointer = COMMANDS[pointer + 1]
  else:
    pointer += 2

def le():
  if DATA[VARS['num1']] <= DATA[VARS['num2']]:
    pointer = COMMANDS[pointer + 1]
  else:
    pointer += 2

def ge():
  if DATA[VARS['num1']] >= DATA[VARS['num2']]:
    pointer = COMMANDS[pointer + 1]
  else:
    pointer += 2

def vm_print():
  pointer += 1
  print(DATA[COMMANDS[pointer]])
  pointer += 1

def read(var):
  pointer += 1
  DATA[COMMANDS[pointer]] = int(input())
  pointer += 1

def jmp():
  pointer = COMMANDS[pointer + 1]

COMMANDS = [
  add, sub, mul, div, idiv, mod, mov, movm, cmp, eq, ne, lt, gt,
  le, ge, vm_print, read, jmp
]

is_running = True
while is_running:
  #print(pointer, COMMANDS[pointer])
  if pointer == len(COMMANDS) - 1:
    is_running = False
    break

  COMMANDS[pointer]()
