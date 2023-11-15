import re

contador = 0

with open('tema0.gift', 'r') as f:
  lines = f.readlines()

for i, line in enumerate(lines):
  if re.search(r':: ASGBD00001 ::', line):
    contador += 1
    new_line = re.sub(r':: ASGBD00001 ::', f':: ASGBD{contador:05} ::', line)
    lines[i] = new_line

with open('tema0new.gift', 'w') as f:
  f.writelines(lines)
  