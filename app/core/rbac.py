from enum import Enum
class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
PERMISSIONS = {
    Role.ADMIN: {"read", "create", "update", "delete"},
    Role.USER: {"read"}
}    
   