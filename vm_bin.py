import struct

prog_file = 'calc_io.vmbin'

with open(prog_file, 'rb') as f:
  code = f.read()

pointer = 0
count_vars = struct.unpack('<I', code[-size_arg:])[0] + 1
DATA = [None] * count_vars
stack_tmp = {}
size_arg = 4


def get_opcode():
  global pointer
  opcode = code[pointer]
  pointer += 1
  return opcode

def get_arg():
  global pointer
  arg = struct.unpack('<I', code[pointer:pointer+size_arg])[0]
  pointer += size_arg
  return arg


def add():
  num1 = get_arg()
  num2 = get_arg()
  DATA[num1] += DATA[num2]

def sub():
  num1 = get_arg()
  num2 = get_arg()
  DATA[num1] -= DATA[num2]

def mul():
  num1 = get_arg()
  num2 = get_arg()
  DATA[num1] *= DATA[num2]

def div():
  num1 = get_arg()
  num2 = get_arg()
  DATA[num1] /= DATA[num2]

def idiv():
  num1 = get_arg()
  num2 = get_arg()
  DATA[num1] //= DATA[num2]

def mod():
  num1 = get_arg()
  num2 = get_arg()
  DATA[num1] %= DATA[num2]

def mov():
  name = get_arg()
  val = get_arg()
  DATA[name] = val

def movm():
  name = get_arg()
  val = get_arg()
  DATA[name] = DATA[val]

def cmp():
  num1 = get_arg()
  num2 = get_arg()
  stack_tmp['num1'] = num1
  stack_tmp['num2'] = num2

# условия:
def eq():
  global pointer
  if stack_tmp['num1'] == stack_tmp['num2']:
    pointer = get_arg()
  else:
    pointer += size_arg

def ne():
  global pointer
  if stack_tmp['num1'] != stack_tmp['num2']:
    pointer = get_arg()
  else:
    pointer += size_arg

def lt():
  global pointer
  if stack_tmp['num1'] < stack_tmp['num2']:
    pointer = get_arg()
  else:
    pointer += size_arg

def gt():
  global pointer
  if stack_tmp['num1'] > stack_tmp['num2']:
    pointer = get_arg()
  else:
    pointer += size_arg

def le():
  global pointer
  if stack_tmp['num1'] <= stack_tmp['num2']:
    pointer = get_arg()
  else:
    pointer += size_arg

def ge():
  global pointer
  if stack_tmp['num1'] >= stack_tmp['num2']:
    pointer = get_arg()
  else:
    pointer += size_arg

def vm_print():
  print(DATA[get_arg()])

def read():
  DATA[get_arg()] = int(input())

def jmp():
  global pointer
  pointer = get_arg()

def halt():
  raise StopIteration

OPCODES = {
  0: halt, # завершение программы. ВЫХОД!
  1: add, # +
  2: sub, # -
  3: mul, # *
  4: div, # /
  5: idiv, # //
  6: mod, # %
  7: mov, # = присвоение конкретного значения
  8: movm, # = присваивает одной переменной значение другой переменной
  9: cmp, # сравнение двух операндов
  10: eq, # перейти на метку, если ==
  11: ne, # перейти на метку, если !=
  12: lt, # перейти на метку, если <
  13: gt, # перейти на метку, если >
  14: le, # перейти на метку, если <=
  15: ge, # перейти на метку, если >=
  16: jmp, # безусловный переход на метку
  17: vm_print, # печать в консоль строки
  18: read, # читать данные из консоли
}

try:
  while pointer < len(code):
    opcode = get_opcode()

    OPCODES[opcode]()
except StopIteration:
  pass
