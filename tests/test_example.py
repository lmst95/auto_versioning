from auto_versioning.example import add_one


def test_add_one():
    assert add_one(3) == 4

def test_add_one2():
    assert add_one(4) == 6
