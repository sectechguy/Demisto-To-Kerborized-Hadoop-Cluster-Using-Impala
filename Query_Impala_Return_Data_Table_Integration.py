"""About: This integration is for querying data from hadoop using impala
   Author: sectechguy
   Creation Date: 11/5/2019
"""
 
import os
import ssl
from impala.dbapi import connect
 
os.system("kinit -kt /etc/krb5.keytab user@DOMAIN")
 
if demisto.command() =='as-get-impala-search':
    rows = []
    try:
        query = demisto.args().get('query')
        IMPALA_HOST = os.getenv('IMPALA_HOST', 'datalakeserver')
        conn = connect(host=IMPALA_HOST, port=21050, auth_mechanism='GSSAPI', use_ssl=True)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
    except Exception as e:
        return_error(str(e))
 
    contents = []
    table = [];
    table.append(colnames);
 
    for row in rows:
        obj = {}
        tableRow = [];
        for x in range(0,len(colnames)):
            obj[colnames[x]]=str(row[x])
            tableRow.append(str(row[x]))
        contents.append(obj)
        table.append(tableRow)
 
    demisto.results({
        'ContentsFormat': formats['json'],
        'Type': entryTypes['note'],
        'Contents': contents,
        "ReadableContentsFormat": formats['table'],
        "HumanReadable": table
    });
