from abc import ABC, abstractmethod


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: list):
        pass


class BubbleSort(SortingStrategy):
    def sort(self, data: list) -> list:
        n = len(data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class MergeSort(SortingStrategy):
    def merge(self, left: list, right: list) -> list:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self.merge(left, right)


class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort_data(self, data: list):
        return self._strategy.sort(data)


if __name__ == "__main__":
    sorter = Sorter(BubbleSort())
    data = [5, 3, 8, 4, 9, 1, 7, 2, 6]
    print("Bubble sort:", sorter.sort_data(data))

    sorter.set_strategy(MergeSort())
    print("Merge sort:", sorter.sort_data(data))