# In this part, we will see a nice syntax to create Generator Expressions
# Also, we will see that if we do not need all the data, in an list, we can use ...
# ... a generaor expression instead.

import time

gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(10000000)]))
list_time = time.time() - gen_start_time

print(f'List Time -> {list_time}')
print(f'Gen Time -> {gen_time}')
