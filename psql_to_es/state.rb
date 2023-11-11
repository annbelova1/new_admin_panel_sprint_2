import abc
import json
import logging
from json import JSONDecodeError
from typing import Any, Optional

logger = logging.getLogger(__name__)

FILE_NOT_FOUND = 'File {name} is not found. Error occurs: {error}.'
READ_ERROR = 'File {name} can not be read. Error occurs: {error}.'


class BaseStorage:
    @abc.abstractmethod
    def save_state(self, state: dict) -> None:
        """Save state in storage"""
        pass

    @abc.abstractmethod
    def retrieve_state(self) -> dict:
        """Retrieve state from storage"""
        pass


class JsonFileStorage(BaseStorage):
    def __init__(self, file_path: Optional[str] = None):
        self.file_path = file_path

    def save_state(self, state: dict) -> None:
        try:
            with open(self.file_path, "w") as write_file:
                json.dump(state, write_file)
        except FileNotFoundError as error:
            logger.debug(
                FILE_NOT_FOUND.format(name=self.file_path, error=error)
            )

    def retrieve_state(self) -> dict:
        state = {}
        try:
            with open(self.file_path, "r") as read_file:
                state = json.load(read_file)
        except (JSONDecodeError, FileNotFoundError) as error:
            logger.debug(READ_ERROR.format(name=self.file_path, error=error))
        return state


class State:
    """Keep states working with data"""

    def __init__(self, storage: BaseStorage):
        self.storage = storage
        self.state = {}

    def set_state(self, key: str, value: Any) -> None:
        """Set state for definite key"""
        if self.state is not None:
            self.state[key] = value
            self.storage.save_state(self.state)

    def get_state(self, key: str) -> Any:
        """Get state of definite key"""
        self.state = self.storage.retrieve_state()
        return self.state.get(key)