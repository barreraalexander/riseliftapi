# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from server.settings import settings

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = f'mysql+pymysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
