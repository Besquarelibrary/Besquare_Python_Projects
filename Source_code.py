# Import the mysql.connector module for MySQL database connection
import mysql.connector

from SMTP import email_service

# Establishing a connection to the MySQL database(host, user, password, database)
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sangeetha@123",
    database="sangeetha"
)

# Create a cursor object to execute SQL queries
cursor = con.cursor()

# # Execute the SQL query to show tables in the database
# cursor.execute("CREATE Database sangeetha")
#
# # Execute the SQL query to create table
# cursor.execute("CREATE TABLE employees_table(Name varchar(30), ID int(10), Email varchar(20))")
cursor.execute("ALTER TABLE employees_table MODIFY Email VARCHAR(40) ;")
# Execute the SQL query to show tables in the database
cursor.execute("SHOW TABLES")

# Print a separator line
print("-------------------------------------------------------------------------------------------")

# Iterate through the result set and print each table name
for db in cursor:
    print(db)

# Print another separator line
print("-------------------------------------------------------------------------------------------")

Emails_List = []


# Function to check if an employee with the given ID already exists
def check_resource(resource_id):
    c = con.cursor()
    sql = "SELECT * FROM employees_table WHERE id = %s"
    c.execute(sql, (resource_id,))
    result = c.fetchone()
    return result is not None


# Function to add an resource
def add_resource():
    resource_id = input("Enter resource Id: ")

    # Checking if resource with given ID already exists
    if check_resource(resource_id):
        print("Resource already exists. Please try again.")
        menu()
    else:
        name = input("Enter Resource Name: ")
        email = input("Enter Resource Email: ")
        data = (resource_id, name, email)

        # Inserting Resource details into the Employee Table
        sql = 'INSERT INTO employees_table (id, name, email) VALUES (%s, %s, %s)'
        c = con.cursor()

        try:
            # Executing the SQL Query
            c.execute(sql, data)
            # Committing the changes in the table
            con.commit()
            print("Resource Added Successfully")
            menu()
        except mysql.connector.Error as e:
            print(f"An error occurred: {str(e)}")
            menu()


def display_table():
    # Executing the SQL query to fetch data from the table
    sql = "SELECT * FROM employees_table order by ID"
    cursor.execute(sql)

    # Fetching all rows from the result set
    rows = cursor.fetchall()

    # Printing the table data
    for row in rows:
        print("Resource name:", row[0])
        print("Resource ID:", row[1])
        Emails_List.append(str(row[2]))
        print("Email ID:", row[2])
        print("----------------------------------------------------------------------")

    menu()


def promote_resource(resource_id, new_email):
    # Updating the Resource's email
    sql = "UPDATE employees_table SET email = %s WHERE id = %s"
    data = (new_email, resource_id)

    try:
        # Executing the SQL query
        cursor.execute(sql, data)

        # Committing the changes in the database
        con.commit()

        print("Resource promoted successfully")
    except mysql.connector.Error as e:
        print(f"An error occurred while promoting the resource: {str(e)}")

    menu()


def remove_resource(resource_id):
    # Checking if the Resource exists
    if not check_resource(resource_id):
        print("Resource does not exist. Please try again.")
        menu()

    try:
        # Deleting the employee from the table
        sql = "DELETE FROM employees_table WHERE ID = %s"
        cursor.execute(sql, (employee_id,))

        # Committing the changes in the database
        con.commit()

        print("Resource removed successfully")
    except mysql.connector.Error as e:
        print(f"An error occurred while removing the resource: {str(e)}")

    # Return to the menu
    menu()


def menu():
    # Display the menu options
    print("1. Add resource")
    print("2. Display data table")
    print("3. Remove resource")
    print("4. Check resource")
    print("5. Email service")
    print("6. Exit")
    print("---------------------------------------------------------------------------")

    # Prompt for user's choice
    choice = input("Enter your choice: ")

    # Perform actions based on the user's choice
    if choice == "1":
        add_resource()


    elif choice == "2":
        display_table()


    elif choice == "3":
        resource_id = int(input("Enter ID number to remove: "))
        remove_resource(resource_id)


    elif choice == "4":
        resource_id = int(input("Enter the resource ID: "))
        if check_resource(employee_id):
            sql = "SELECT * FROM employees_table WHERE id = %s"
            cursor.execute(sql, (resource_id_id,))
            resource_data = cursor.fetchone()
            print("Resource name:", resource_data[0])
            print("Resource ID:", resource_data[1])
            print("Email ID:", resource_data[2])
            print("-------------------------------------------------------------------------------------------")
        else:
            print("ID does not exist")
            print("-------------------------------------------------------------------------------------------")
        menu()


    elif choice == "5":
        # Executing the SQL query to fetch data from the table
        sql = "SELECT * FROM employees_table order by ID"
        cursor.execute(sql)

        # Fetching all rows from the result set
        rows = cursor.fetchall()

        # Printing the table data
        for table_data in rows:
            email_service(table_data[2], table_data[0])
            print("Email Successfully sent to:", table_data[0])
            break
        exit()


    elif choice == "6":
        # Close the database connection and exit the program
        con.close()
        print("Goodbye!")
        exit()


    else:
        print("Invalid choice. Please try again.")
        menu()


# Starting point of the program
menu()

 














# Import the smtplib module for SMTP functionality
import smtplib
# Import the MIMEText class for creating email body
from email.mime.text import MIMEText
# Import the MIMEMultipart class for creating email message
from email.mime.multipart import MIMEMultipart
import datetime


def email_service(Receiver_Email, Person_name):
    # Sender's email details
    sender_email = 'sangeethareddy2129@gmail.com'
    sender_password = 'axivlivjfbqwczau'

    # Recipient's email details
    recipient_email = Receiver_Email

    # Email content
    subject = 'Builder Tracker Reminder'
    body_1 = f'Dear {Person_name},' \
             '\n' \
             '\n' \
             'Good Morning, This is reminder to start your  "Builder Tracker"  timer and run it for 8 hours without losing any work hours.' \
             '\n' \
             '\n' \
             'Please ignore this email if you have already started the tracker.' \
             '\n' \
             '\n' \
             'Thank you,\n' \
             'BeSquare Technologies' \
             '\n' \
             '\n' \
             'NOTE : This is a system generated email, Please do not reply to this message.'\

    body_2 = f'Dear {Person_name},' \
             '\n' \
             '\n' \
             'Good Evening, This is reminder to stop your  "Builder Tracker"  timer after completing 8 working hours.' \
             '\n' \
             '\n' \
             'Please ignore this email if you have already stopped the tracker.' \
             '\n' \
             '\n' \
             'Thank you,\n' \
             'BeSquare Technologies' \
             '\n' \
             '\n' \
             'NOTE : This is a system generated email, Please do not reply to this message.' \

    # Create the email message
    message = MIMEMultipart()
    # Set the 'From' header of the email message
    message['From'] = sender_email
    # Set the 'To' header of the email message
    message['To'] = recipient_email
    # Set the 'Subject' header of the email message
    message['Subject'] = subject
    # Flag to keep track if a message has been attached
    message_attached = False
    while not message_attached:
        time_now = datetime.datetime.now().strftime("%I:%M%p")

        if time_now == "09:55AM":
            # Create MIMEText attachment with body_1
            message.attach(MIMEText(body_1, 'plain'))
            # Set the flag to exit the loop
            message_attached = True
        elif time_now == "19:30":
            # Create MIMEText attachment with body_2
            message.attach(MIMEText(body_2, 'plain'))
            # Set the flag to exit the loop
            message_attached = True

    try:
        # Connect to Gmail's SMTP server using SSL
        with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
            # Login to the sender's Gmail account
            smtp.login(sender_email, sender_password)

            # Send the email
            smtp.send_message(message)

        # print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("Error: unable to send email.")
        print(str(e))

