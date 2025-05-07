from get_value import get_value

def test_get_value():
    print("Running test: valid nested dictionary paths")

    assert get_value({"a": {"b": {"c": "d"}}}, "a/b/c") == "d"
    print("Test 1 passed: 'a/b/c' == 'd'")

    assert get_value({"num": {"value": 123}}, "num/value") == 123
    print("Test 2 passed: 'num/value' == 123")

    assert get_value({"flag": {"enabled": True}}, "flag/enabled") is True
    print("Test 3 passed: 'flag/enabled' == True")

    print("\nRunning test: error handling")

    try:
        get_value({"a": {"b": {}}}, "a/b/c")
        print("Test 4 failed: Missing key did not raise KeyError")
    except KeyError:
        print("Test 4 passed: Caught missing key as KeyError")

    try:
        get_value({"a": 1}, "a/b")
        print("Test 5 failed: Wrong type did not raise TypeError")
    except TypeError:
        print("Test 5 passed: Caught wrong type as TypeError")

    print("\nAll tests ran.")

if __name__ == "__main__":
    test_get_value()

