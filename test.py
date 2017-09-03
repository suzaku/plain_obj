import pytest

import plain_obj


class TestCreateNewType:

    def test_can_create_with_a_list_of_fields(self):
        Point = plain_obj.new_type('Point', ['x', 'y', 'z'])
        assert isinstance(Point, type)
        assert len(Point.__slots__) == 3

    def test_can_create_with_comma_separated_string(self):
        Point = plain_obj.new_type('Point', 'x,y,z')
        assert isinstance(Point, type)
        assert len(Point.__slots__) == 3

    def test_can_create_with_space_separated_string(self):
        Point = plain_obj.new_type('Point', 'x y  z')
        assert isinstance(Point, type)
        assert len(Point.__slots__) == 3


class TestValidation:

    def test_should_report_when_name_is_invalid(self):
        invalid_names = ['123', 'f(&*']
        for n in invalid_names:
            with pytest.raises(ValueError):
                plain_obj.new_type('Point', ['123'])

    def test_should_report_when_name_is_keyword(self):
        with pytest.raises(ValueError):
            plain_obj.new_type('Point', ['is'])


def test_create_new_objects():
    Config = plain_obj.new_type('Config', 'skips_dist,run_tests')
    config = Config(True, False)
    assert config.skips_dist
    assert not config.run_tests


def test_repr():
    Point = plain_obj.new_type('Point', 'x y z')
    point = Point(3, 1, 4)
    assert repr(point) == 'Point(3, 1, 4)'


def test_to_dict():
    Config = plain_obj.new_type('Config', 'skips_dist,run_tests')
    config = Config(True, False)
    assert config.to_dict() == {
        'skips_dist': True,
        'run_tests': False,
    }


def test_unpacking():
    Config = plain_obj.new_type('Config', 'skips_dist,run_tests')
    skips_dist, run_tests = Config(True, False)
    assert skips_dist
    assert not run_tests
