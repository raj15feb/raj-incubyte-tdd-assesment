from main import add

def test_add_blank_string():
    input_str = ""
    expected = 0
    total = add(input_str)
    assert expected == total
    