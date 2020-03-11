import magic


def test_a():
    assert magic.LOADER.list_templates() == ['1.txt']
