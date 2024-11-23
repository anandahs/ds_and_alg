emp_list = [('Ankit', 10000), ('Rahul', 12000), ('Sumit', 14000), ('Dheeraj', 21000), ('Pavan', 11000),
            ('Mohit', 13000)]

emp_dict = dict(emp_list)

avg = sum(emp_dict.values()) / len(emp_dict)

print(f"average salary:{avg}")

employee_avg_list = [(key, value) for key, value in emp_dict.items() if value > avg]

print(employee_avg_list)

import numpy as np
avg_sal = np.mean([x[1] for x in emp_list])
print([x for x in emp_list if x[1] > avg_sal])
