"""Generate jamcoins.

This solves problem A of the Google codejam 2016. Please see the problem online
for complete description.
"""

import math
import sys

_CACHE = {}
_PRIME_DIVISORS = [2, 3, 5]


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


def generate_prime_divisors(end):
  for prime in _PRIME_DIVISORS:
    if prime > end:
      return
    yield prime

  if prime <= end:
    for num in xrange(prime, end + 1, 2):
      for smaller_prime in _PRIME_DIVISORS:
        if num % smaller_prime == 0:
          break
      else:
        _PRIME_DIVISORS.append(num)
        yield num



def get_a_divisor(value):
  """Gets a non-trivial divisor of value, None if no divisors are found."""
  if value not in _CACHE:
    for divisor in xrange(2, int(math.ceil(math.sqrt(value)))):
    # for divisor in generate_prime_divisors(int(math.ceil(math.sqrt(value)))):
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
