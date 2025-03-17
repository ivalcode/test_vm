#import main
from casm_opcodes import BYTECODES, FLAGS

from types_data import Number
from casm_opcodes import BYTECODES, FLAGS


LABELS = {
  'for_run_start': 3,
  'new_cod_run_for': 10,
  'for_run_end': 15, # следующая команда после цикла
  'is_prime_start': 17,
  'is_le_or_nechet': 27,
  'pre_for_is_prime_start': 45,
  'for_is_prime_start': 48,
  'for_is_prime_end': 66,
  'end_is_prime': 71,
  'end_program': 76
}

DATA = [10000, None, None, None, None, None, None, None]
VARS = {
  'i': 1,
  'rez': 2,
  'is_chet': 3,
  'rez_stack': 4,
  'i_is_prime': 5,
  'num1': 6,
  'num2': 7
}
COMMANDS = [
  # Точка входа (начало первой функции)
  BYTECODES['mov'], VARS['i'], 0,
  # for_run_start:
  BYTECODES['cmp'], DATA[VARS['i']], DATA[0],
  BYTECODES['jmp_ge'], LABELS['for_run_end'],
  BYTECODES['jmp'], LABELS['is_prime_start'],
  # new_cod_run_for:
  BYTECODES['add'], DATA[VARS['i']], 1,
  BYTECODES['jmp'], LABELS['for_run_start'],
  # for_run_end:
  BYTECODES['jmp'], LABELS['end_program'],
  # конец первой функции

  # начало второй функции
  #is_prime_start:
  BYTECODES['cmp'], DATA[VARS['i']], 2,
  BYTECODES['jmp_ne'], LABELS['is_le_or_nechet'],
  BYTECODES['mov'], VARS['rez'], 1,
  BYTECODES['jmp'], LABELS['new_cod_run_for'],
  # is_le_or_nechet:
  BYTECODES['cmp'], DATA[VARS['i']], 1,
  BYTECODES['jmp_gt'], LABELS['pre_for_is_prime_start'],
  BYTECODES['mod'], DATA[VARS['i']], 2, # положит результат в rez_stack
  BYTECODES['cmp'], DATA[VARS['rez_stack']], 0,
  BYTECODES['jmp_ne'], LABELS['pre_for_is_prime_start'],
  BYTECODES['mov'], VARS['rez'], 0,
  BYTECODES['jmp'], LABELS['new_cod_run_for'],
  # pre_for_is_prime_start:
  BYTECODES['mov'], VARS['i_is_prime'], 3,
  # for_is_prime_start:
  BYTECODES['cmp'], DATA[VARS['i_is_prime']], 9,
  BYTECODES['jmp_ge'], LABELS['end_is_prime'],
  BYTECODES['mod'], DATA[VARS['i']], DATA[VARS['i_is_prime']],
  BYTECODES['cmp'], DATA[VARS['rez_stack']], 0,
  BYTECODES['jmp_ne'], LABELS['for_is_prime_end'],
  BYTECODES['mov'], VARS['rez'], 0,
  BYTECODES['jmp'], LABELS['new_cod_run_for'],
  # for_is_prime_end:
  BYTECODES['add'], DATA[VARS['i_is_prime']], 2,
  BYTECODES['jmp'], LABELS['for_is_prime_start'],
  # end_is_prime:
  BYTECODES['mov'], VARS['rez'], 1,
  BYTECODES['jmp'], LABELS['new_cod_run_for'],
  # конец второй функции
  # end_program:
  None
  # конец программы
]

print(len(COMMANDS))


pointer = 0

def add(num1, num2):
  DATA[VARS['rez_stack']] = num1 + num2

def sub(num1, num2):
  DATA[VARS['rez_stack']] = num1 - num2

def mul(num1, num2):
  DATA[VARS['rez_stack']] = num1 * num2

def div(num1, num2):
  DATA[VARS['rez_stack']] = num1 / num2

def idiv(num1, num2):
  DATA[VARS['rez_stack']] = num1 // num2

def mod(num1, num2):
  DATA[VARS['rez_stack']] = num1 % num2

def mov(name, val):
  print(name)
  DATA[name] = val
  print(DATA[VARS['i']])

def cmp(num1, num2):
  DATA[VARS['num1']] = num1
  DATA[VARS['num2']] = num2

# условия:
def eq():
  if DATA[VARS['num1']] == DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False

def ne():
  if DATA[VARS['num1']] != DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False

def lt():
  if DATA[VARS['num1']] < DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False

def gt():
  if DATA[VARS['num1']] > DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False

def le():
  if DATA[VARS['num1']] <= DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False

def ge():
  if DATA[VARS['num1']] >= DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False


is_running = True
while is_running:
  print(pointer, COMMANDS[pointer], COMMANDS[pointer + 1], COMMANDS[pointer + 2])
  print(DATA[VARS['i']])
  print(COMMANDS)
  if COMMANDS[pointer] == BYTECODES['add']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    add(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['sub']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    sub(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['mul']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    mul(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['div']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    div(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['idiv']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    idiv(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['mod']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    mod(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['mov']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    mov(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['cmp']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    cmp(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['jmp_eq']:
    eq()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp_ne']:
    ne()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp_lt']:
    lt()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp_gt']:
    gt()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp_le']:
    le()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp_ge']:
    ge()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp']:
    pointer = COMMANDS[pointer + 1]
    continue


  else:
    print("Ошибка байткода!")
    is_running = False
    break

  if pointer == len(COMMANDS) - 1:
    is_running = False

  pointer += 1

print(f"Программа завершена, результат: {DATA[VARS['rez']]}")
