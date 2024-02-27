from models.user import User as UserModel
from schemas.user import User

class UserService():
    def __init__(self, db) -> None:
        self.db = db
 
    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user(self, id:int):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result

    def create_user(self, user:User):
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()

    def update_user(self, id:int, data:User):
        user = self.get_user(id)
        user.user_name = data.user_name
        user.user_mail = data.user_mail
        user.password = data.password
        self.db.commit()

    def delete_user(self, id:int):
        user = self.get_user(id)
        self.db.delete(user)
        self.db.commit()