import string_ops as s
import numpy as np
import pandas as pd

print(s.is_palindrome('abba'))
example = "This is an example. Return the nth occurrence of example in this example string."
print(s.find_nth_occurrence("example", example, 3))
print(s.find_nth_occurrence(example, 3))
print(s.repeated_substring("ababab"))
print(s.repeated_substring(1))
print(s.solve("code*s","codewars"))
