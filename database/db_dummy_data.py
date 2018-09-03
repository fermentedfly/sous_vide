from database.db_app import db, Ds18b20
import datetime

# cleanup
Ds18b20.query.delete()

time = datetime.datetime.now()
data = [Ds18b20(db_id=i, timestamp=time + datetime.timedelta(seconds=i) , temperature=float(i + 20)) for i in range(10)]

for x in data:
    db.session.add(x)

db.session.commit()
print(str(Ds18b20.query.all()).replace(',', '\n'))
