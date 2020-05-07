import uuid
from time import mktime
from datetime import datetime

from django.db import models

class Application(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    api = models.CharField(max_length=20)
    dateofcreation = models.BigIntegerField(default=0)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def create(self, name, **kwargs):
        api = str(uuid.uuid4().hex)
        dateofcreation = int(mktime((datetime.now()).timetuple()))
        app = self(name=name, dateofcreation=dateofcreation, api=api, **kwargs)
        app.save()
        return app

    @classmethod
    def get(self, **kwargs):
        apps = self.objects.filter(**kwargs)
        if len(apps)>0:
            return apps[0]
        else:
            return None

    def update(self, **kwargs):
        update_fields = []
        for key, value in kwargs.items():
            if key != "api": 
                setattr(self, key, value)
                update_fields.append(key)

        if len(update_fields) > 0:
            self.save(update_fields=update_fields)

        return self

    def api_update(self):
        self.api = str(uuid.uuid4().hex)
        self.save(update_fields = ['api'])
        return self
