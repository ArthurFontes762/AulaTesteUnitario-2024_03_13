class UsersCRUD:
    def __init__(self):
        self.users = []

    def create_user(self, name, age): 
        user = {"name": name, "age": age}
        self.users.append(user)
        return user

    def read_users(self):  
        return self.users

    def update_user(self, index, name, age): 
        if 0 <= index < len(self.users):
            self.users[index]["name"] = name
            self.users[index]["age"] = age
            return self.users[index]
        else:
            raise IndexError("Index out of range")

    def delete_user(self, index):
        if 0 <= index < len(self.users):
            deleted_user = self.users.pop(index)
            return deleted_user
        else:
            raise IndexError("Index out of range")
