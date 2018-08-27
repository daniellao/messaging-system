import xmlrpc.client
import redis
import pybloom_live
import schedule
import time
import json


url = "http://172.20.0.1:8069"
db = "test"
username = "username@example.com"
password = "test"

common = xmlrpc.client.ServerProxy("%s/xmlrpc/2/common" % url)
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy("%s/xmlrpc/2/object" % url)

r = redis.Redis(
host = 'redis0',
port = 6379,
password = '')

with open('data.json', 'r') as f:
    data = json.load(f)

records = []
f = pybloom_live.BloomFilter(capacity=1000, error_rate=0.001)

def receive_order(records, f):
    records = models.execute_kw(db,
                                uid,
                                password,
                                'sale.order',
                                'search_read',
                                [[('invoice_status','=', 'to invoice')]])
    if records not in f:
        f.add(records)
        produce_message(records, data)

def produce_message(records, data):
    for record in records:
        data['order_id'] = record['id']
        send_message(r, data)


def send_message(r, data):
    r.sadd('in_queue', data)
    return publish_message(r)

def publish_message(r):
    r.publish('my-channel', 'some data')

schedule.every(1).second.do(receive_order, records, f)

while True:
    schedule.run_pending()
    time.sleep(1)
