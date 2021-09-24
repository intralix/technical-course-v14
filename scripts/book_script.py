# -*- coding: utf-8 -*-
from xmlrpc import client
from datetime import datetime
from datetime import timedelta

url = 'https://intralix-technical-course-v141-deb-jonas-3279311.dev.odoo.com'
db = 'intralix-technical-course-v141-deb-jonas-3279311'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid= common.authenticate(db,username,password,{})

print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db,uid,password,
                                 'library.renting','check_access_rights',
                                 ['write'],{'raise_exception':False})

print(model_access)

oldiedatetime = datetime.today() - timedelta(days=60)

oldiesrentings = models.execute_kw(db,uid,password,
                            'library.renting','search',
                             [[['startdate' ,'<', oldiedatetime ]]])

print(oldiesrentings)

for renting in oldiesrentings :
    models.execute_kw(db, uid, password, 'library.renting', 'write', [[renting], {
    'phone': "8186574156"}])
    # get record name after having changed it
    res_renting = models.execute_kw(db, uid, password, 'library.renting', 'search_read', [[['id' ,'=', renting ]]])
    print(res_renting)
    