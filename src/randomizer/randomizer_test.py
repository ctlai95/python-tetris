from src.randomizer import randomizer


def test_new_list():
    r = randomizer.Randomizer()
    assert len(r.list) == 7
    expected = ["O", "I", "J", "L", "S", "Z", "T"]
    for e in expected:
        assert e in r.list


def test_next():
    r = randomizer.Randomizer()
    for i in range(7, 0, -1):
        n = r.next()
        assert n not in r.list
        assert len(r.list) == i - 1
    n = r.next()
    assert len(r.list) == 6
