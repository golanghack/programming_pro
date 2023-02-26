#! /usr/bin/env python3 

class Authentication:
    
    USERS = [
        {
            'username': 'user1', 
            'password': 'pwd1'
        }
    ]
    
    def login(self, username: str, password: str) -> str:
        user = self.fetch_user(username)
        if not user or user['password'] != password:
            return None
        return user
    
    def fetch_user(self, username: str) -> str:
        for user in self.USERS:
            if user['username'] == username:
                return user 
            else:
                return None
            
class Authorization:
    
    PERMISSIONS = [
        {
            'user': 'user1', 
            'permissions': {
                'create', 'edit', 'delete',
            },
        }
    ]
    
    def can(self, user: str, action: str) -> bool:
        for user in self.PERMISSIONS:
            if user['user'] == user['username']:
                return action in user['permissions']
            else:
                return False