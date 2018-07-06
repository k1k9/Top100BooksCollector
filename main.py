#!/usr/bin/python3
#
# Title: Collect
# Description: This script grab Top100 books and save it in database
# Author: @k1k9
#
from urllib.request import urlopen as uRequest			# collect.py
from bs4 import BeautifulSoup as bSoup 					# collect.py
import pymysql											# database.py

from collect import grab100 as grabTopPages
from database import Database


# Grab data
books = grabTopPages()


# Connect to database
db = Database('localhost','root','pyDB')


# Send data to database
try:
	for book in books:
		# Add this line when you see warning like this "Data truncated for column[..]"
		# db.query("ALTER TABLE `top100LC` CHANGE addDate addDate CHAR(34);")
		
		db.query("""INSERT INTO `top100LC` (Title, Author, Rank, Readers, Opinions, Rate, addDate)
									VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', NOW())""".format(
										book[0], book[1], book[2], book[3], book[4], book[5]))

	print("\nSuccessful send data to database")
except:
	print("\nCannont send data to database")


# Close database connect
db.close()