from abc import ABC,abstractclassmethod

class Receivers(ABC):
    @abstractclassmethod
    def create(self,data):
        pass
    @abstractclassmethod
    def get(self,data):
        pass
    @abstractclassmethod
    def update(self,data):
        pass
    @abstractclassmethod
    def all(self,data):
        pass
    @abstractclassmethod
    def update_account_bank(self,data):
        pass   
    @abstractclassmethod
    def get_balance(self,data):
        pass
    @abstractclassmethod
    def create_balance_withdrawal(self,data):
        pass
    @abstractclassmethod
    def get_balance_withdrawal(self,data):
        pass
    @abstractclassmethod
    def get_all_balance_withdrawal(self,data):
        pass
    @abstractclassmethod
    def update_config_transference(self,data):
        pass
    @abstractclassmethod
    def update_automatic_anticipation_settings(self,data):
        pass