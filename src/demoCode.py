#!/usr/bin/env python3
# date: 18 April 2022
# demo code for a menu system for the database management tool


# The below code is a demonstration of a basic menu system that you might want to use in your own database management system. This example code uses a hard-coded table (see tables_dict dictionary) from our campus database from class, however your system will need to use different tables according to user inputs. The user is able to specify at least three table attributes, and signal menu options to interact with these attributes such as populating, querying and modifying. Remember, the user will never need to interact directly with SQL programming -- your Python code is to handle all operations with the database.

# -----------------------------------------

# A sample and hard coded dictionary for the example code that contains the table names (keys) and the number of their attributes (values). Your code will not have hardcoded table names such as these.

tables_dict = {"instructor": 5,
"teaches":5,
"student": 4,
"course": 4,
"department": 3
}

# Define a function to get user input for the name of the table
def getTableName():
	"""Function to get the table name from the user"""
	print("\n\t [+] Welcome to getTableName()")

	# show the tables
	prmpt_str = ""
	for i in tables_dict:
		prmpt_str = prmpt_str + f"\n\t * {i}"
	prmpt_str = prmpt_str + "\n\t Choose a table name :"

	# get user table selection
	tableToEdit = input(prmpt_str) # enter input
	tableToEdit = tableToEdit.lower() # put text in to lower case

	# check to see that the selected table is contained in tables_dict
	while(tableToEdit not in tables_dict):
		print(f"\t [-] No such table, <{tableToEdit}> in dictionary. Please re-enter the name.")
		tableToEdit = input(prmpt_str) # enter input
		tableToEdit = tableToEdit.lower() # put text in to lower case

	return tableToEdit
# end of getTableName()


def databaseFunction():
	""" menu function to ask user what function is to be performed on a selected table"""
	print("\n\t [+] Welcome to databaseFunction()")

	options_list = [0, 1, 2, 3] # 0 = create, 1 = populate, 2 = query, 3 = modify
	prmpt_str = f"\n\t 0 = create, 1 = populate, 2 = query, 3 = modify\n\t Enter integer :"
	# Each attribute is assigned a number. Show the attributes and allow user to choose a number.

	result_int = "" # declare value before the below code block to keep the value in memory after the block has been execute

	# get an input from user; use exceptions
	try:
		result_int = int(input(prmpt_str))
		print(f"\t [+] Option {result_int} chosen.") # create? populate? query or modify a table?
	except ValueError:
		print("\t [-] First Exception Handled: Could not convert data to an integer.")

	# make sure that the user input actually works with the code. use exceptions.
	while result_int not in options_list: # check that the user entered a valid number
		print(f"\t [-] Option <{result_int}> not found. Please try again.")

		try:
			result_int = int(input(prmpt_str))
			print(f"\t [+] Option {result_int} chosen.") # create? populate? query or modify a table?
		except ValueError:
			print("\t [-] Second Exception Handled: Could not convert data to an integer.")

	if result_int == 0:
		create() # call this function if result_int is 0
	if result_int == 1:
		insert() # call this function if result_int is 1
	if result_int == 2:
		query() # call this function if result_int is 2
	if result_int == 3 :
		modify() # call this function if result_int is 3
	return result_int
# end of databaseFunction()


def create():
	""" print a welcome message for option 0, CREATE"""
	print("\n\t [+] Welcome to CREATE()")
	print("\t -- TODO: ask user what to do with DB and make it happen...")
# end of create()


def insert():
	""" print a welcome message for option 1, POPULATE"""
	print("\n\t [+] Welcome to POPULATE()")
	print("\t -- TODO: ask user what to do with DB and make it happen...")
# end of insert()


def query():
	""" print a welcome message for option 2, QUERY"""
	print("\n\t [+] Welcome to QUERY()")
	print("\t -- TODO: ask user what to do with DB and make it happen...")
# end of query()


def modify():
	""" print a welcome message for option 3, MODIFY """
	print("\n\t [+] Welcome to MODIFY")
	print("\t -- TODO: ask user what to do with DB and make it happen...")
# end of modify()


def main():
	# the program actually starts here. The dictionary of table names tables_dict is a global variable and is accessible by all functions, as necessary.
	print("\t Welcome to my database automation demo program!")
	result_int = databaseFunction()
	# print(f"\t [+] The returned value: {result_int}")

	print("\n\t [+] Enter function for selected table: ")
	myTable_str = getTableName()
	print(f"\t [+] There are <{tables_dict[myTable_str]}> attributes associated with table <{myTable_str}>.")

	print("  -- End of program --")
# end of main()


# -----------------------------------------


main() # call and run the driver function main().
