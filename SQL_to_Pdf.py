import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Replace these with your database credentials
host = 'localhost'
user = 'root'
password = ''
database = 'mps_connection_phase_i'

# SQL query
sql_query = """
    SELECT tn.Transaction_ID, tn.CreatedAt, tn.Status, tn.task_name, tn.TaskID, ln.Lead_ID, 
    e_assigned.emp_role AS AssignedToRole, e_assigned.name AS AssignedToName, 
    e_assigned_by.emp_role AS AssignedByRole, e_assigned_by.name AS AssignedByName, 
    e_status_updated.emp_role AS StatusUpdatedByRole, e_status_updated.name AS StatusUpdatedByName, 
    s.Service_Name, tn.update_description 
    FROM transaction_table tn 
    LEFT JOIN leadnew ln ON tn.LeadID = ln.Lead_ID 
    LEFT JOIN employee e_assigned ON tn.AssignedTo_Id = e_assigned.Emp_id 
    LEFT JOIN employee e_assigned_by ON tn.AssignedBy_Id = e_assigned_by.Emp_id 
    LEFT JOIN employee e_status_updated ON tn.Status_updated_by = e_status_updated.Emp_id 
    LEFT JOIN service s ON tn.service_id = s.Service_id;
"""

# Create a database connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Execute the query and fetch the result into a pandas DataFrame
df = pd.read_sql_query(sql_query, connection)

# Increase the page size (figure size)
fig, ax = plt.subplots(figsize=(15, 9))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', fontsize=14)

# Customize the table appearance
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(5, 5)  # Adjust the overall size of the table
for key, cell in table.get_celld().items():
    cell.set_linewidth(2)  # Set border width

# Save the plot as a PDF file
plt.savefig('output.pdf', format='pdf', bbox_inches='tight')

# Display the plot (optional)
plt.show()

# Close the database connection
connection.close()
