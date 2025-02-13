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

def test_add_with_single_separator():
    input_str = "1,2"
    expected = 3
    total = add(input_str)
    assert expected == total

def test_add_with_multi_delimeter():
    input_str = "//[***]\n1***2***3"
    expected = 6
    total = add(input_str)
    assert expected == total

def test_add_with_negative_value():
    input_str = "1,-3"
    expected = "Negative Numbers are not allowed"
    total = add(input_str)

    assert expected == total
    