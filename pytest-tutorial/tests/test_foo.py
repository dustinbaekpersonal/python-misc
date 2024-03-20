from unittest import mock

from src.foo import Smt, another_func, foo_func, foo_func_with_class_instance


def test_another_func():
    """Using context manager ensures there is no leakage of our mocked object."""
    with mock.patch("src.foo.some_func", return_value=5) as mock_ctx, \
        mock.patch("src.foo.CONSTANT_A", 0):
        assert another_func() == 0
        mock_ctx.assert_called_once_with()
    with mock.patch("src.foo.some_func", return_value=1) as mock_ctx_2, \
        mock.patch("src.foo.asdf_func", return_value=1):
        assert another_func(flag=False) == 3
        mock_ctx_2.assert_called_once_with()


def test_another_func_monkeypatch(monkeypatch):
    """With monkeypatch, it does similar job as mock.patch. We can also use context manager."""
    with monkeypatch.context() as m:
        m.setattr("src.foo.CONSTANT_A", 0)
        m.setattr("src.foo.some_func", lambda: 100)
        assert another_func() == 0
        

def test_another_func_mocker(mocker):
    mocker.patch("src.foo.some_func", return_value=5)
    assert another_func() == 15


def test_foo_func_mock_method():
    # Assuming smt is an object with some_method() as an instance method
    with mock.patch('src.foo.Smt.some_method', return_value=100) as mocked_method:
        test_smt = Smt()
        assert foo_func(test_smt) == 100


def test_foo_func_mock_class(mocker):
    # if a class is too expensive to instantiate in test, you can mock the class itself.
    test_smt = mocker.MagicMock()
    test_smt.some_method.return_value = 1000
    assert foo_func(test_smt) == 1000


def test_foo_func_mock_class_with_context_manager(mocker):
    # even better is to use context manager.
    
    # TODO: Figure out why mocker.patch does not work using context manager!
    # mocker.patch gives AttributeError: 'NoneType' object has no attribute 'some_method'
    with mock.patch("src.foo.Smt", return_value=mocker.MagicMock()) as mocked_class:
        mocked_class.some_method.return_value = 1000
        assert foo_func(mocked_class) == 1000
    

def test_foo_func_mock_class_without_context_manager(mocker):
    # even better is to use context manager.
    
    # TODO: Figure out why mocker.patch does not work!
    # mocker.patch gives AttributeError: 'NoneType' object has no attribute 'some_method'
    mocked_class = mocker.patch("src.foo.Smt", return_value=mocker.MagicMock())
    mocked_class.some_method.return_value = 1000
    assert foo_func(mocked_class) == 1000


"""If you get AttributeError for a module, check attributes using dir().

Example:
    from src import foo
    dir(foo)
"""

def test_foo_func_with_class_instance():
    # when we have class instance within the source code.
    with mock.patch("src.foo.Smt", return_value=mock.MagicMock()) as mocked_class:
        # IMPT: you have to instantiate a mocked class, to mock smt instance.
        instance = mocked_class.return_value
        instance.some_method.return_value = 2000
        assert foo_func_with_class_instance() == 2000
