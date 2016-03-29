"""Generate jamcoins.

This solves problem A of the Google codejam 2016. Please see the problem online
for complete description.
"""

import math
import sys

_CACHE = {}


def stream_generator(start, stop, step=1):
  """Generates a stream of strs from start to stop in binary system."""
  for num in xrange(start, stop, step):
    yield str(bin(num))[2:]


def interpret_from_base(string, base):
  """Return value of the string decoding from the base system."""
  # Not ensuring base values in [2, 10] for performance.
  num = 0
  for digit in string:
    num = num * base + int(digit)
  return num


def get_a_divisor(value):
  """Gets a non-trivial divisor of value, None if no divisors are found."""
  if value not in _CACHE:
    if value % 2 == 0:
      _CACHE[value] = 2
      # break  # Repeating returns to make it faster, remove if unneded.
      return 2
    for divisor in xrange(3, int(math.ceil(math.sqrt(value))), 2):
      if value % divisor == 0:
        _CACHE[value] = divisor
        # break  # Repeating returns to make it faster, remove if unneded.
        return divisor
    return
  return _CACHE[value]


def find_jamcoins(length, count):
  """Generates jamcoins with given inputs in the output format needed."""

  strs = stream_generator(2 ** (length - 1) + 1, 2 ** length + 1, 2)
  jamcoins, generated = {}, 0

  for num_str in strs:
    if generated == count:
      break

    divisors = []
    for base in range(2, 11):  # [2, 11)
      value = interpret_from_base(num_str, base)
      divisor = get_a_divisor(value)
      if not divisor:  # It's a prime number, we're no more interested in it.
        break
      divisors.append(str(divisor))
    else:
      jamcoins[num_str] = divisors
      print num_str + ' ' + ' '.join(jamcoins[num_str])
      generated += 1
  return jamcoins


def main():
  # Need to handle file inputs and also outputting in file. It's better to get
  # the dict here and the open file for writing.
  # Don't use argparse, as the boilerplate slows it down.
  cases, length, count = map(int, sys.argv[1:4])
  for case in range(cases):
    print "Case #{0}:".format(case + 1)
    jamcoins = find_jamcoins(length, count)


if __name__ == '__main__':
  main()
