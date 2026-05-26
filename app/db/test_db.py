from session import engine


# Test connection database
try :
    engine.connect()
    print("Database connection successful")
except Exception as e:
    print("Database connection failed")