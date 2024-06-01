from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_host: str
    database_port: str
    database_name: str
    database_password: str
    database_username: str
    secret_key: str
    api_key: str
    client_secret: str
    algorithm: str
    access_token_expiration_time: int
    
    class Config:
        env_file = ".env"
        
    


setting = Settings()





