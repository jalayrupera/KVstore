from dotenv import load_dotenv
from pydantic import BaseSettings
from os import environ as env

load_dotenv(".env")

class Settings(BaseSettings):
    ETCD_HOST = env.get("ETCD_HOST", "localhost")
    ETCD_PORT = env.get("ETCD_PORT", 2379)


settings = Settings()