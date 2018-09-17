"""
Exercise problem:

Write a function that takes in 3 integers as arguments and returns a list of numbers from 1 to 100 (inclusive),
containing only integers that are evenly divisible by at least one of the integers.
For example, given 50, 30, and 29, return [29, 30, 50, 58, 60, 87, 90, 100].
"""

"""
This first one is the more 'show your work' version, which goes through the logic as I think a person normally would.
While the meat of the function can process more than 3 arguments, the ask was to write one that accepts 3. Both
methods skip duplicates, though they could be included by removing a line.
"""


def divisibility(a, b, c):
    inputs = locals().values()
    output = []
    for i in inputs:
        for r in range(i, 101):
            if (r % i) == 0:
                if (r in output) is False:
                    output.append(r)
    output.sort()
    return output


"""
This one is a little more slick - fewer lines and accepting unlimited inputs. 'Evenly divisible by' also means
'multiple of' so we can use range() in a funky way to accomplish the same thing a little more efficiently. If we wanted
to crunch it down to even fewer lines, I think you could use reduce(), but you start sacrificing readability. This
version is what I'd use on a project at work because it strikes a happy medium. 
"""


def divisibility2(*args):
    output = []
    for i in args:
        for r in range(0, 101, i)[1::]:
            if (r in output) is False:
                output.append(r)
    output.sort()
    return output
