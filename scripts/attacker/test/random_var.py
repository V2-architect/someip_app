import numpy as np
import time

mean = 10
std_dev = 2

def generate_bounded_random_variable(mean, std_dev, min_val, max_val):
    while True:
        random_variable = np.random.normal(mean, std_dev)
        if min_val <= random_variable <= max_val:
            return int(random_variable)

min_val = 5
max_val = 15

random_variables = []


ss = time.time()
for _ in range(1000):
    random_variable = generate_bounded_random_variable(mean, std_dev, min_val, max_val)
    random_variables.append(random_variable)
ee = time.time()

print(f"Generated random variables: {random_variables}")
print(f"time elapsed: {ee-ss}")
