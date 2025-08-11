# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm.session import sessionmaker


# SQLALCHAMY_DATABASE_URL = 'sqlite:///.blog.db'
# engine = create_engine(SQLALCHAMY_DATABASE_URL , connect_args={"check_same_thread":False})

# SessionLocal = sessionmaker(bind=engine,autocommit = False,autoflush=False )

# Base = declarative_base()



from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ Fix 1: Typo in variable name
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db' 

# ✅ Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required only for SQLite
)

# ✅ Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ✅ Base class for models
Base = declarative_base()
