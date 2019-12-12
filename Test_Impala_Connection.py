import os
import ssl
from impala.dbapi import connect
from impala.util import as_pandas
import pandas as pd

os.system("kinit -kt /etc/krb5.keytab user@DOMAIN")
IMPALA_HOST = os.getenv('IMPALA_HOST', '<data_lake_server')
conn = connect(host=IMPALA_HOST, port=21050, auth_mechanism='GSSAPI', use_ssl=True)
cursor = conn.cursor()
cursor.execute('SHOW TABLES')
tables = as_pandas(cursor)
cursor.execute('select namestr, destinationhostname from proxy_table limit 10')  //test connection

df = as_pandas(cursor)
print (df)
