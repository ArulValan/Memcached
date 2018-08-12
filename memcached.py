# go tho the memcached.exe directory
# cd C:\path\to\memcache\containing\folder

# Start memcached with 1024MB of RAM with a UDP port "11211" with max connection limit of 2048 and 8Thread configuration
# memcached.exe -m 1024 -U 11211 -c 2048 -t 8
# for more information on memcached startup refer to https://docs.oracle.com/cd/E17952_01/mysql-5.6-en/ha-memcached-cmdline-options.html





--------------------------------------------------
# PYTHON #

# Install Pymemcache library on your environment using pip using below command
# pip install pymemcache

# In your Python file include the following lines to store the data in memcached server

from pymemcache.client.base import Client

client = Client(('localhost', 11211))
client2 = Client(('129.168.1.10', 11211))
client.set('key', 'value')
client2.set('key', 'value')

# To retrieve the parameters use the same key and the client object to that server should have receive the value

cache=client.get('key')
print(cache)

cache=client2.get('key')
print(cache)
--------------------------------------------------
