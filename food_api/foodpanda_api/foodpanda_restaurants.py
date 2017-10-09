from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insertOneRestaurant(restaurant_id, name, address, rating_aggregate, delivery_fee, delivery_time, takeaway_time, minimum_order, payment_methods, voucher, data_resource):
	query = "INSERT INTO restaurants(restaurant_id, name, address, rating_aggregate, delivery_fee, delivery_time, takeaway_time, minimum_order, payment_methods, voucher, data_resource) " \
			"VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

	args = (restaurant_id, name, address, rating_aggregate, delivery_fee, delivery_time, takeaway_time, minimum_order, payment_methods, voucher, data_resource)

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
		print "RESTAURANT DATA INSERTED!!!"

def insertManyRestaurants(restaurants_info):
	query = "INSERT INTO restaurants(restaurant_id, name, address, rating_aggregate, delivery_fee, delivery_time, takeaway_time, minimum_order, payment_methods, voucher, data_resource) " \
			"VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.executemany(query, restaurants_info)

		conn.commit()

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()
		print "RESTAURANT DATA INSERTED!!!"

def findRestaurantById(id):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute("SELECT * FROM restaurants where restaurant_id = " + id)

		row = cursor.fetchone()
		print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()

def findRestaurantByName(query):
	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		if query: 
			query = "%" + query + "%"
		cursor.execute("SELECT * FROM restaurants WHERE name LIKE '%s'" % query)

		rows = cursor.fetchall()
		for row in rows:
			print row

	except Error as error:
		print error

	finally:
		cursor.close()
		conn.close()