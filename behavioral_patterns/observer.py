import random
from abc import ABC, abstractmethod
from typing import List


class ISubscriber(ABC):
    @abstractmethod
    def subscribe_to_event(self, state: int) -> str:
        """"""


class SubscriberA(ISubscriber):
    name = "SubA"

    def subscribe_to_event(self, state: int) -> str:
        if 2 < state < 6:
            return f"A was notified from publisher!"


class SubscriberB(ISubscriber):
    name = "SubB"

    def subscribe_to_event(self, state: int) -> str:
        if 3 < state < 9:
            return f"B was notified from publisher!"


class Publisher:
    def __init__(self) -> None:
        self.subscribers: List[ISubscriber] = list()

    def add_subscriber(self, subscriber: ISubscriber) -> str:
        self.subscribers.append(subscriber)
        return f"{subscriber.name} was successfully registed!"

    def publish_event(self) -> str:
        state = random.randint(1, 11)
        publish_info = f"Source was published with state:{state}!\n"
        for sbscrbr in self.subscribers:
            publish_info += f"{sbscrbr.subscribe_to_event(state)}\n"
        return publish_info


if __name__ == "__main__":
    sub1, sub2 = SubscriberA(), SubscriberB()
    publisher = Publisher()
    print(publisher.add_subscriber(sub1))
    print(publisher.add_subscriber(sub2))

    print("\n\n\n")

    for _ in range(5):
        print(publisher.publish_event())
