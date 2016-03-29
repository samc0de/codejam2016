"""Sleeping sheep.

This solves problem B of the Google codejam 2016. Please see the problem online
for complete description.
"""

import math
import sys


def get_sleeping_num(num):
  if not num:
    return 'INSOMNIA'

  digits_seen = set(str(num))
  original_num = num
  while len(digits_seen) < 10:
    num += original_num
    digits_seen.update(str(num))

  return num


def main():
  input_file = sys.argv[1]
  output_file = sys.argv[2] if len(sys.argv) > 2 else 'output'
  inputs = {}
  with open(input_file, 'r') as ifile:
    cases = int(ifile.readline())
    for case in range(cases):
      inputs[case] = int(ifile.readline())

  outputs = {case: get_sleeping_num(num) for case, num in inputs.iteritems()}

  with open(output_file, 'w') as ofile:
    for case, num in outputs.iteritems():
      ofile.write('Case #{0}: {1}\n'.format(case + 1, num))


if __name__ == '__main__':
  main()
