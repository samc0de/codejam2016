"""Generate jamcoins.

This solves problem A of the Google codejam 2016. Please see the problem online
for complete description.
"""

import math
import sys

# Caching primes (may need to traverse in reverse order)
# Using offset instead of calculating value each time.
# Divisibility checks. [DONE]
# No point in caching the value: divisor, 0 cache hits in 1 16 50.

_CACHE = {'found': 0, 'not found': 0}
PRIMES = [2, 3, 5, 7, 11]


def cache_primes(length):
  upper_bound = int('1' * length)
  for num in xrange(11, int(math.ceil(math.sqrt(upper_bound))), 2):
    for prime in PRIMES:
      if num % prime:
        break
      if prime <= math.sqrt(num):  # Remove if it's an overhead.
        break
    else:
      PRIMES.append(num)


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
  num_str = str(value)
  sum_of_digits = sum(map(int, num_str))
  # Fastest first.
  if sum_of_digits % 3 == 0:
    return 3
  if num_str[-1] in (0, 5):
    return 5
  if value % 2 == 0:
    return 2
  # for divisor in xrange(7, int(math.ceil(math.sqrt(value))), 2):
  for divisor in PRIMES:
    if value % divisor == 0:
      return divisor
  # return None


def find_jamcoins(length, count):
  """Generates jamcoins with given inputs in the output format needed."""

  # strs = stream_generator(2 ** length + 1, 2 ** (length - 1) + 1, -2)
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
  cache_primes(length)
  for case in range(cases):
    print "Case #{0}:".format(case + 1)
    jamcoins = find_jamcoins(length, count)


if __name__ == '__main__':
  main()
