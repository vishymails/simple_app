import pytest

def test_generic() :
    a = 30
    b =30
    assert a == b


class NotInRange (Exception) :
    def __init__(self, message="value not in range") :
        self.message = message 
        super().__init__(self.message)

def test_generic1() :
    a = 5
    with pytest.raises(NotInRange) :
        if a not in range(10, 20) :
            raise NotInRange