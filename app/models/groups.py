from app.models import db
from app.models import ma

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    keterangan = db.Column(db.String(100))

    def __serialize__(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'keterangan' : self.keterangan
        }
        
db.create_all()

class GroupSchema(ma.Schema):
    class Meta:
        model = Group
        fields = ['id','name','keterangan']

group_schema = GroupSchema(many=True) 
