from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def algorithm(self):
        pass


class ConcreteStrategyA(Strategy):

    def algorithm(self):
        print('ConcreteStrategyA algorithm.')


class ConcreteStrategyB(Strategy):

    def algorithm(self):
        print('ConcreteStrategyB algorithm.')


class Context:

    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.algorithm()


if __name__ == '__main__':
    context = Context()
    context.set_strategy(ConcreteStrategyA())
    context.execute_strategy()
    context.set_strategy(ConcreteStrategyB())
    context.execute_strategy()