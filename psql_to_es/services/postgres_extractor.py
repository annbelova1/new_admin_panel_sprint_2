import logging
from datetime import datetime
from typing import Iterator

import psycopg2
from config import etl_settings, pg_settings
from psycopg2 import DatabaseError, OperationalError, ProgrammingError
from psycopg2.extras import RealDictCursor
from queries import FILMWORKS_QUERY

logger = logging.getLogger(__name__)

CONNECT_TO_POSTGRES = "Connect to Postgres..."
POSTGRES_CONNECTION = "Connection to Postgres succeeded."


class PostgresExtractor:
    """A class to extract Postgres data and transform it to pydantic format."""

    def __init__(self) -> None:
        self.connection = None
        self.cursor = None

    def connect_to_postgres(self) -> None:
        logger.info(CONNECT_TO_POSTGRES)
        self.connection = psycopg2.connect(
            **pg_settings.dict(), cursor_factory=RealDictCursor
        )
        self.cursor = self.connection.cursor()
        logger.info(POSTGRES_CONNECTION)

    def extract_movies(self, date_last_modified: datetime) -> Iterator:
        """Extract data from Postgres"""
        self.cursor.execute(FILMWORKS_QUERY, (date_last_modified,) * 3)
        while rows := self.cursor.fetchmany(etl_settings.BATCH_SIZE):
            yield rows