# A unit fraction contains 1 in the numerator. The decimal representation of the unit
# fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen
# that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
# its decimal fraction part.


def recurring_cycle_digits(n):
    digits = []
    remainder = 1
    # Zero is the number impossoble to become quotient
    quotient = 0
    recurring = False
    cycle_len = 0

    while quotient not in digits or remainder != 0:
        digits.append(quotient)
        quotient, remainder = divmod(10 * remainder, n)

    if quotient in digits:
        recurring = True
        digits.pop(0)
        cycle_len = len(digits)
    return cycle_len

results = []
for i in range(2, 10):
    results.append(recurring_cycle_digits(i))
print(results)
