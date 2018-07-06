#!/usr/bin/python3
#
# Title: Database
# Description: This script connect with database
# Author: @k1k9
#
import pymysql

class Database:



	# Connect to database
	def __init__(self, host, dbUser, dbName):


		print("""====================
 Connect to databse
====================
Host: {0}
User: {1}\n""".format(host,dbUser))


		# Try initialize connection with database
		try:
			# Apply parameters
			self.host = host
			self.dbUser = dbUser
			self.dbName = dbName
			

			# Get password from user for security ¯\_(ツ)_/¯
			dbPassword = input('Password: ')


			# Connect to database
			try:
				self.db = pymysql.connect(host, dbUser, dbPassword, dbName)
				print("\nSuccessful connect to " + dbName + " database on " + host + "\n")
			except:
				print("\n\nOPS! Can't connect to database\n\n")
		except:
			print("\n\nOPS! Please check your input data\n\n")



	# Send query to database
	def query(self, query):
		try:
			self.db.cursor().execute(query)
			self.db.commit()
		except:
			self.query = query
			print("\nError with query: " + query)
			print("\nRollbacking!\n")
			self.db.rollback();




	# Close connect with database
	def close(self):
		self.db.close()
		print("\nConnection between you and " + self.dbName + " database was closed")