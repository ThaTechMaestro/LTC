class IntegerContainerImpl:
    def __init__(self):
        self.store = []

    def add(self, value: int) -> int:
        self.store.append(value)
        return len(self.store)

    def delete(self, value: int) -> bool:
        if value not in self.store:
            return False
        self.store = [x for x in self.store if x != value]
        return True

    def get_median(self):
        if not self.store:
            return None

        new_store = sorted(self.store)
        n = len(new_store)
        mid = n // 2

        if n % 2 == 1:     # odd length
            return new_store[mid]
        else:              # even length → left middle
            return new_store[mid - 1]


def test_level_2_case_08_median_of_container_with_negative_integers():
    container = IntegerContainerImpl()
    assert container.add(-20) == 1
    assert container.add(-10) == 2
    assert container.add(10) == 3
    assert container.add(20) == 4
    assert container.add(0) == 5
    assert container.get_median() == 0
    assert container.add(-30) == 6
    assert container.get_median() == -10
    assert container.add(30) == 7
    assert container.get_median() == 0
    assert container.add(40) == 8
    assert container.add(50) == 9
    assert container.get_median() == 10
    print("✅ test_level_2_case_08 passed!")


if __name__ == "__main__":
    test_level_2_case_08_median_of_container_with_negative_integers()
