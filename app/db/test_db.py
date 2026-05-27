from app.db.session import engine

from app.db.session import SessionLocal
from app.schemas.user import UserSchema
from app.db.db_user import create_user

from app.db.hash import Hash

# ==== TEST CONNECTION DATABASE ===

# Test connection database
try :
    engine.connect()
    print("Database connection successful")
except Exception as e:
    print("Database connection failed")

# ==== TEST CREATE USER ====

# create ORM session
db = SessionLocal()

# Create a new user schema for the request
request = UserSchema(
    name="Angel",
    email="angel@gmail.com",
    hashed_password="123"
)

""" 
# Hash the password
hashed_password = Hash.get_password_hash(request.hashed_password)
print("Hashed password:", hashed_password)

# verify the password
is_valid = Hash.verify_password("123", hashed_password)
print("Password verification result:", is_valid) 

request.hashed_password = hashed_password
"""

new_user = create_user(db, request)

print(new_user)


