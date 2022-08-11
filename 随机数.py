import random,pprint
coll=set()
for i in range(25):
    year=random.randrange(1960,1990)
    month=random.randrange(1,12)
    day=random.randrange(1,28)
    coll.add(str(year)+'/'+str(month)+'/'+str(day))
pprint.pprint(coll)