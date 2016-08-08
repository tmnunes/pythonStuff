#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET
import mysql.connector

# connect
db = mysql.connector.connect(host="localhost", user="admin", passwd="mysqladmin",
db="SA")

cursor = db.cursor()

# execute SQL select statement
cursor.execute("SELECT * FROM Businesses")

# commit your changes
# db.commit()

# get the number of rows in the resultset
numrows = int(cursor.rowcount)
#print db.host
print (numrows)

# get and display one row at a time.
#for x in range(0,numrows):
#    row = cursor.fetchone()
#    print row[0], "-->", row[1]


tree = ET.parse('user_data.xml')
root = tree.getroot()

urls = (
    '/users', 'list_users',
    '/business', 'business',
    '/users/(.*)', 'get_user'
)

app = web.application(urls, globals())

class list_users:
    def GET(self):
        output = 'users:[';
        for child in root:
                print ('child', child.tag, child.attrib)
                output += str(child.attrib) + ','
        output += ']';
        return output

class business:
    def GET(self):
        output = 'users:[';
        for x in range(0,numrows):
            row = cursor.fetchone()
            print (row[0], "-->", row[1])
            output += str(row[1]) + ','
        output += ']';
        return output

class get_user:
    def GET(self, user):
        for child in root:
            if child.attrib['id'] == user:
               return str(child.attrib)


if __name__ == "__main__":
    app.run()
