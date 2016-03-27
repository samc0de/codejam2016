"""Generate jamcoins.
TODO: More detailed description follows here.
"""

import math
import sys

_CACHE = {}


def strem_generator(start, stop, step=1):
  """Generates a stream of strs from start to stop in binary system."""
  for num in range(start, stop, step):
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
  # if value not in _CACHE['divisors']:  # Remove if not much effective, too much
    # memory maybe.
  if value not in _CACHE:
    for divisor in range (2, int(math.ceil(math.sqrt(value)))):
      if value % divisor == 0:
        _CACHE[value] = divisor
        # break  # Repeating returns to make it faster, remove if unneded.
        return divisor
    return
  return _CACHE[value]


def find_jamcoins(length, count):
  """Generates jamcoins with given inputs in the output format needed."""

  strs = strem_generator(2 ** (length - 1) + 1, 2 ** length + 1, 2)
  # Edit if needed. This serves better when we return the whole dict??
  # jamcoins = collections.defaultdict(list)
  jamcoins, generated = {}, 0

  for num_str in strs:
    # Get value of num_str decoding using bases [2, 10]. If any of these values
    # is a prime number, break the loop. If the timing is still exceeding
    # limits, make a dict for interpreting values from string (above fn) and
    # keep a copy of value being looped for each base in a dict & increment the
    # previous value by an offset which keeps track of by what value the new
    # value differs from prev. eg cur_loop_values {2: 17, 3: 17, 4: 16, 5: 15,
    # # base: cur_val}; offset = 2. This saves efforts for looping and
    # calculating vals from string repr, it just changes slightly from the prev
    # value, we can just do tha math for that small value.
    if generated == count:
      print "Done {0} jamcoins.".format(generated)
      break

    divisors = []
    for base in range(2, 11):  # [2, 11)
      # set_trace()
      value = interpret_from_base(num_str, base)
      divisor = get_a_divisor(value)  # Memoization is imp, edit if needed.
      if not divisor:  # It's a prime number, we're no more interested in it.
        # if num_str in jamcoins:
        #   jamcoins.pop(num_str)
        break
      divisors.append(divisor)
      # jamcoins[num_str].append(divisor)  # Avoid dd if it's slow.
    else:
      # The string is a jamcoin as it didn't break non-primality check for any
      # base.
      jamcoins[num_str] = str(divisors)
      # print num_str + ' ' + ' '.join(divisors)
      print num_str + ' ' + ''.join(jamcoins[num_str])
      generated += 1
      # For performance (repeating an iteration of X/count.) printing here
      # itself. Probably (if time permits) just return the dict and print in
      # the caller.
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
