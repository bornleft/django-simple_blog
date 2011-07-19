from django.core.management import setup_environ
import project.settings
setup_environ(project.settings)
from django.db import connection

cursor = connection.cursor()
while 1:
    sql = raw_input(">")
    cursor.execute(sql)

    print cursor.fetchall()
