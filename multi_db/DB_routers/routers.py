# class AuthRouters:
#     route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}
#
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'default_db'
#         return None
#
#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'default_db'
#         return None
#
#     def allow_relation(self, obj1, obj2, **hints):
#         if (
#                 obj1._meta.app_label in self.route_app_labels or
#                 obj2._meta.app_label in self.route_app_labels
#         ):
#             return True
#         return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'default_db'
#         return None


# # for mongodb database (administrator)
# class MongodbRouter:
#
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'accounts':
#             return 'administrator'
#         return None
#
#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'accounts':
#             return 'administrator'
#         return None
#
#     def allow_relation(self, obj1, obj2, **hints):
#
#         if obj1._meta.app_label == 'accounts' or \
#                 obj2._meta.app_label == 'accounts':
#             return True
#         return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'accounts':
#             return db == 'administrator'
#         return None


# for postgres database (store)
class PostgreSQLRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'store':
            return 'sales'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'store':
            return 'sales'
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label == 'store' or \
                obj2._meta.app_label == 'store':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'store':
            return db == 'sales'
        return None


