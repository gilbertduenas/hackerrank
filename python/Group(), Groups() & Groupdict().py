# https://www.hackerrank.com/challenges/re-group-groups/problem

# regex still \me.

import re

alpha = '[qwrtypsdfghjklzxcvbnm]'

a = re.findall('(?<=' + alpha +')([aeiou]{2,})' + alpha, input(), re.I)

print('\n'.join(a or ['-1']))
