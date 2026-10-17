# Student Identity
LAST_NAME = 'Segundo'
STUDENT_ID = 'TUPM-26-1220'

# derive computational parameters
seed_digit = int(STUDENT_ID[-1])
id_checksum = sum(int(d) for d in STUDENT_ID if d.isdigit())
vector_dim = len(LAST_NAME)

# encapsulate state into a dictionary (Associative Map)
sys_config ={
    'operator': LAST_NAME,
    'auth_id': STUDENT_ID,
    'base_seed': seed_digit,
    'checksum': id_checksum,
    'vector_dim': vector_dim,
    'status': 'INITIALIZED'
}

# DISPLAY SYSTEM STATE
print('=== SYSTEM CONFIGURATION ===')
for key, value in sys_config.items():
    print(f'{key.upper()}: {value}')

# intialize a list using the system configuration
base_val = sys_config['base_seed']
number_sequence = [base_val, base_val + 15, sys_config['checksum']]

print(f'Initial Sequence: {number_sequence}')

#append a new value to the sequence
number_sequence.append(base_val + 20)
print(f'After Append: {number_sequence}')

new_numbers = [base_val + 5, sys_config['vector_dim'], base_val]
number_sequence.extend(new_numbers)
print(f'After Extend: {number_sequence}')

#count occurences of the base value
base_count = number_sequence.count(base_val)
print(f'Occurences of {base_val}: {base_count}')

#sort the sequence in ascending order
number_sequence.sort()
print(f'Sorted Sequence: {number_sequence}')

#define an immutable tuple using system parameters
fixed_coordinates = (sys_config['vector_dim'], sys_config['base_seed'], 0)
print(f'Fixed Coordinates: {fixed_coordinates}')

#unpacked the tuple into individual variables
x_val, y_val, z_val = fixed_coordinates 
print(f'Unpacked Values -> X: {x_val}, Y: {y_val}, Z: {z_val}')

# attempt to modify the tuple (expected to fail)
try:
    fixed_coordinates[0] = 99
except TypeError as error_msg:
    print(f'Modification Error: {error_msg}')

# create a dictionary representing astructured data payload
data_payload = {
    'Identifier': sys_config['auth_id'],
    'Dimension': sys_config['vector_dim'],
    'Status': 'active'
}

#iterate and display key-value pairs
print('--- Payload Data ---')
for key, value in data_payload.items():
    print(f'{key.capitalize()}: {value}')

# add a new key-value pair dynamically
data_payload['efficiency_rating'] = 98.5
print(f'Updated Payload: {data_payload}')

base_val = sys_config['base_seed']

#initialize a list with deliberate duplicate values
raw_data = [base_val, base_val + 5, base_val, sys_config['vector_dim'], base_val + 5]
print(f'Raw Data (with duplicates): {raw_data}')

#convert the  list to a set to remove duplicates
unique_data = set(raw_data)
print(f'Unique Set: {unique_data}')

# define a secondary refrence set for comparison
reference_set = {base_val, base_val + 10, base_val + 20}
print(f'Reference Set: {reference_set}')

#perform mathematical intersections and unions
common_elements = unique_data.intersection(reference_set)
combined_elements = unique_data.union(reference_set)

print(f'Intersection (Common): {common_elements}')
print(f'Union (Combined): {combined_elements}')

import array
# initialize an integer array using the type code 'i'
number_array = array.array('i', [sys_config['base_seed'],sys_config['vector_dim'], 100])
print(f'Integer Array: {number_array}')

# attempt to append a non-integer data type (expected to fail)
print('\nAttempting to append a string...')
try:
    number_array.append('invalid')
except TypeError as error_msg:
    print(f'Type Error: {error_msg}')

base_val = sys_config['base_seed']

# generate a sequence dynamically
generated_list = [(x * base_val) for x in range(1, 6)]
print(f'Generated Comprehension: {generated_list}')

# filter the generated sequence
filtered_list = [x for x in generated_list if x > 15]
print(f'Filtered Comprehension (Values > 15): {filtered_list}')

from collections import deque
# initialize a double-ended queue
data_queue = deque([sys_config['base_seed'], sys_config['vector_dim']])
print(f'Initial Queue: {data_queue}')

# append to both ends
data_queue.append(100)
data_queue.appendleft(200)
print(f'After Appends: {data_queue}')

# remove from left side
data_queue.popleft()
print(f'Final Deque(After Popleft): {data_queue}')

from collections import defaultdict

# initialize with a default factory (creates a 0 for missing keys)
default_data = defaultdict(int)

#assign a known key
default_data['active_key'] = sys_config['vector_dim']

print(f'Existing Key Value: {default_data["active_key"]}')
# accessing an  uninitialized key will not throw a keyerror
print(f'Missing Key Value (Auto Generated): {default_data["unknown_key"]}')
