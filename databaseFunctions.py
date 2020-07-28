import sqlite3

#Jermaine Foskey
#Create customer database table
def createCustomersTable():
	#creating and connection to database
	conn = sqlite3.connect('customer.db')

	# create a cursor
	c= conn.cursor()
	
	#Create Table
	c.execute("""CREATE TABLE customers(
	first_name text,
	last_name text,
	email text
	)""")

	#Insert one row at a time Rows into the customer database
	c.execute("INSERT INTO customers VALUES ('Steve', 'Rogers', 'Steve@Roger.com')")
	c.execute("INSERT INTO customers VALUES ('Kal', 'El', 'Kal@El.com')")
	c.execute("INSERT INTO customers VALUES ('Peter', 'Parker', 'Peter@Parker.com')")

	#Insert many rows into the database
	many_customers= [('Barry','Allen','Barry@Allen.com'), ('Charles','Xavier','Charles@Xavier.com'),('Remy','LeBeau','Remy@LeBeau.com')]
	c.executemany("INSERT INTO customers VALUES (?, ?, ?)",many_customers)
	#Commit our command
	conn.commit()

	#close our connection
	conn.close()





#Drop data from tabe
def dropDataFromCustomersTable():
	#creating and connection to database
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c= conn.cursor()

	#DROP Table(delete an entire table)
	c.execute("DROP TABLE customers")
	#Commit our command
	conn.commit()

	#close our connection
	conn.close()


#Query The DB and Return All Records
def show_all():
	#creating and connection to database
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c= conn.cursor()

	# Query The Database get Row ID
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()

	#print(items)
	for item in items:
		print(item)


	#Commit our command
	conn.commit()

	#close our connection
	conn.close()

	print("Command executed Successfully!!")




#Add a New Record To The Table
def add_one(first,last,email):
	#creating and connection to database
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c= conn.cursor()

	# Insert record into the database
	c.execute("INSERT INTO customers VALUES (?,?,?)",(first,last,email))
	#Commit our command
	conn.commit()

	#close our connection
	conn.close()

#Add Many Records to Table
def add_many(list):
	#creating and connection to database
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c= conn.cursor()
	# Insert record into the database
	c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
	#Commit our command
	conn.commit()

	#close our connection
	conn.close()

#Delete Record from table
def delete_one(id):
	#creating and connection to database
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c= conn.cursor()

	# Insert record into the database
	c.execute("DELETE from customers WHERE rowid = (?)", id)
	#Commit our command
	conn.commit()

	#close our connection
	conn.close()

# Lookup with Where
def email_lookup(email):
	#creating and connection to database
	conn = sqlite3.connect('customer.db')
	# create a cursor
	c= conn.cursor()
	# Insert record into the database
	c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
	items = c.fetchall()

	#print(items)
	for item in items:
		print(item)


	#close our connection
	conn.close()

