import pandas as pd

# Sample Data
data = {
    'Employee ID': [101, 102, 103, 104, 105],
    'Full Name': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis'],
    'Department': ['Sales', 'Marketing', 'IT', None, 'HR'],
    'Salary': ['50000', '60000', '70000', '80000', '90000']
}
employee_data = pd.DataFrame(data)

# Convert 'Salary' column to numeric
employee_data['Salary'] = pd.to_numeric(employee_data['Salary'], errors='coerce')

# Remove rows with missing values in 'Department'
employee_data = employee_data.dropna(subset=['Department'])

# Extract first name from 'Full Name'
employee_data['First Name'] = employee_data['Full Name'].apply(lambda x: x.split()[0])

print("Cleaned Employee Data:\n", employee_data)
