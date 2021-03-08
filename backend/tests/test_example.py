from pytest_postgresql import factories

postgresql_external = factories.postgresql("postgresql_nooproc")


def test_dummy():
    pass
