from abc import ABC, abstractmethod


class UsAbstractSocket(ABC):
    @abstractmethod
    def us_way_plug_in(self) -> str:
        pass


class EuropeAbstractSocket(ABC):
    @abstractmethod
    def european_way_plug_in(self) -> str:
        pass


class UsSocket(UsAbstractSocket):
    def us_way_plug_in(self) -> str:
        return "Plugged a us socket"


class EuropeSocket(EuropeAbstractSocket):
    def european_way_plug_in(self) -> str:
        return "Plugged a european socket"


class EuropeanSocketAdapter(EuropeAbstractSocket):
    def __init__(self, us_socket: UsSocket) -> None:
        # composition with high coupling
        self.us_socket = us_socket

    def european_way_plug_in(self) -> str:
        return self.us_socket.us_way_plug_in() + " to an europen socket"


if __name__ == "__main__":
    us_sckt = UsSocket()
    european_socket_adapter = EuropeanSocketAdapter(us_socket=us_sckt)
    print(european_socket_adapter.european_way_plug_in())
