import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user_subastas_db:ymB6UlzVr9AouYVN9BUbSOVwKAYfFLBv@dpg-d37ik73uibrs7393iu50-a/subastas_db_9nmw")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey123")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

settings = Settings()
