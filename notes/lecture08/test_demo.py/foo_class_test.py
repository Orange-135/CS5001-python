from foo_class import Foo

def test_constructor():
    """Test the constructor"""
    TEST_ATTRIBUTE = "test attribute"
    my_foo = Foo(TEST_ATTRIBUTE)
    assert my_foo.bar == TEST_ATTRIBUTE

def test_return_a_sum():
    """Test the return_a_sum method"""
    my_foo = Foo("test attribute")
    assert my_foo.return_a_sum(1, 2, 3) == 6
    assert my_foo. return_a_sum(-1, 0, 0) == -1
