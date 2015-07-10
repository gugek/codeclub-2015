import re
import random
def foo(s):
    """Takes something"""
    if random.random() <= .25:
        return "Goodbye cruel"
    elif random.random() <= .50:
        return "Go away"
    else:
        return "Bye"

bar_re = re.compile(r"\b(Hello)\b")

s = "Hello world, Hello world, Hello world,"

# magical behavior where the repl can be a function that acts on each
# individual match

s2 = bar_re.sub(foo, s)
print(s2)