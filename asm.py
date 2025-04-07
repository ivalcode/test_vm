from casm_opcodes import BYTECODES

asm_file = 'calc_io'

commands = []

with open(f'{asm_file}.vmasm', 'r', encoding='utf-8') as asm:
  for line in asm:
    commands.append(line.strip().split())

sum_vars = 0

with open(f'{asm_file}.py', 'w', encoding='utf-8') as programm:
  programm.write('from types_data import Number\n')
  programm.write('from casm_opcodes import BYTECODES\n')
  programm.write('\n')
  programm.write('COMMANDS = [\n')

  for cmd in commands:
    if not cmd:
      continue
    if int(cmd[1]) > sum_vars:
      sum_vars = int(cmd[1]) # получаем количество переменных в коде

    if len(cmd) == 2:
      programm.write(f'{BYTECODES[cmd[0]]}, {cmd[1]},\n')
    elif len(cmd) == 3:
        programm.write(f'{BYTECODES[cmd[0]]}, {cmd[1]}, {cmd[2]},\n')
    else:
      exit('Неверный формат ассемблернго кода')

  programm.write(f'{BYTECODES["halt"]}\n')
  programm.write(']\n')
  programm.write('VARS = {\n')

  for i in range(sum_vars + 1):
    programm.write(f'{i}: {i},\n')

  programm.write('}\n')
