from pydantic import BaseSettings, Field


class PostgresSettings(BaseSettings):
    dbname: str = Field(env="POSTGRES_DB")
    user: str = Field(env="POSTGRES_USER")
    password: str = Field(env="POSTGRES_PASSWORD")
    host: str = Field(env="DB_HOST")
    port: int = Field(env="DB_PORT")
    options: str = Field(env="DB_OPTIONS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class ElasticsearchSettings(BaseSettings):
    hosts: str = Field("http://127.0.0.1:9200", env="ELASTIC_SERVER")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class ETLSettings(BaseSettings):
    BATCH_SIZE: int = Field(100, env="BATCH_SIZE")
    TIME_INTERVAL: int = Field(60, env="TIME_INTERVAL")
    STATE_FILE_NAME: str = Field("state.json", env="STATE_FILE_NAME")
    LOGGING_LEVEL: str = Field(env="LOGGING_LEVEL")
    FILEMODE: str = Field(env="FILEMODE")
    FILENAME: str = Field(env="FILENAME")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


etl_settings = ETLSettings()
pg_settings = PostgresSettings()
es_settings = ElasticsearchSettings()