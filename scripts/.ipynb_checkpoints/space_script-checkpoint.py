from xmlrpc import client

url = 'https://intralix-technical-course-v141-dev-luis-3278789.dev.odoo.com'
db = 'intralix-technical-course-v141-dev-luis-3278789'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print('versión')
print(common.version())

uid = common.authenticate(db, username, password, {})
print('uid')
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

ships = models.execute_kw(db,uid,password,'space.space','search_read',[[['active','=',True]]])
print('ships')
print(ships)


new_ship = models.execute(db, uid, password, 'space.space','create',[
            {
                'name':'Enterprice',
                'shiptype':'moenix',
                'fueltype':'gas',
                'width':180,
                'height':250,
                'fuel':1800,
                'active':True,
                'description':'No hay nada por aquí. Lee otra nave'
            }
        ]
    )

print('New ship')
print(new_ship)