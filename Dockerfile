FROM python:3.5.7-buster
 
ADD krb5.conf /etc/krb5.conf
ADD krb5.keytab /etc/krb5.keytab
 
COPY requirements.txt .
 
RUN apt-get update && apt-get install -y libsasl2-dev libsasl2-2 libsasl2-modules-gssapi-mit openssl libkrb5-dev \
    krb5-config kinit kinit-dev krb5-user libpam-krb5 krb5-multidev libcurl4-openssl-dev keyutils libkeyutils-dev \
    python-keyutils python3-keyutils
RUN pip install --no-cache-dir -r requirements.txt
