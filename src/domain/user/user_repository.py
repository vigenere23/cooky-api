from abc import ABC, abstractmethod
from src.infra.db.models.user import AccountModel, UserModel, AddressModel

class UserRepository(ABC):

    # FUTURE change to domain entity
    @abstractmethod
    def find_by_username(self, username: str) -> UserModel:
        raise NotImplementedError()

    # FUTURE change to domain entity
    @abstractmethod
    def find_by_id(self, user_id: int) -> UserModel:
        raise NotImplementedError()

    # FUTURE change to domain entity
    # FUTURE make Account children of User (aggregate)
    @abstractmethod
    def find_account_of(self, user_id: int) -> AccountModel:
        raise NotImplementedError()

    # FUTURE change to domain entity
    # FUTURE make Address children of User (aggregate)
    @abstractmethod
    def find_account_address(self, account_id: int) -> AddressModel:
        raise NotImplementedError()

    # FUTURE change to domain entity
    @abstractmethod
    def save(self, account: AccountModel, user: UserModel, address: AddressModel) -> UserModel:
        raise NotImplementedError()

    # FUTURE change to domain entity
    @abstractmethod
    def replace_account(self, account: AccountModel) -> AccountModel:
        raise NotImplementedError()

    # FUTURE change to domain entity
    @abstractmethod
    def replace_address(self, account_id: int, address: AddressModel) -> AddressModel:
        raise NotImplementedError()
