# Make a function that reverses a string

def reverse(rand_str: str) -> str:
    return rand_str[::-1]
        

def test_function():
    assert reverse("hello world") == "dlrow olleh"
