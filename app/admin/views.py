from sqladmin import ModelView

from app.users.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.tg_id]