import databaseFunctions

#Jermaine Foskey

#drop data from Customers table
databaseFunctions.dropDataFromCustomersTable()

#create database  Customers table
databaseFunctions.createCustomersTable()


#Add record to the database
databaseFunctions.add_one("Natasha","Romanoff","Natasha@Romanoff.com")
databaseFunctions.add_one("Bruce","Banner","Bruce@Banner.com")

# Delete Record use Row ID as string
databaseFunctions.delete_one('6')



#Add Many Records

stuff = [
	("Ororo'","Munroe","Ororo@Monroe.com"),
	("Selina","Kyle","Selina@Kyle.com"),
	("Barbra","Gordon","Barbra@Gordon.com"),
	('Clark','Kent','Clark@kent.com')
	]

databaseFunctions.add_many(stuff)

# Lookup Email Address Record
databaseFunctions.email_lookup("Natasha@Romanoff.com")

#show all the records
databaseFunctions.show_all()

