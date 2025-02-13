from main import add

def test_add_blank_string():
    input_str = ""
    expected = 0
    total = add(input_str)
    assert expected == total

def test_add_single_string():
    input_str = "1"
    expected = 1
    total = add(input_str)
    assert expected == total
    