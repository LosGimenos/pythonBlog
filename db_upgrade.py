from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))
