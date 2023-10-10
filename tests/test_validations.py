from src.validator import *


def test_validate_name():
    assert len(validate_name(None)) > 0
    assert len(validate_name('')) > 0
    assert len(validate_name('test name')) == 0


def test_validate_age():
    assert len(validate_age(None)) == 0
    assert len(validate_age('42')) > 0
    assert len(validate_age('hehe')) > 0
    assert len(validate_age(-2)) > 0
    assert len(validate_age(42)) == 0


def test_validate():
    assert len(validate_person_request({
        'name': 'test name'
    })) == 0
    assert len(validate_person_request({
        'name': 'test name',
        'age': 42
    })) == 0
    assert len(validate_person_request({
        'name': 'test name',
        'age': 42,
        'work': 'testing',
        'address': None
    })) == 0
    assert len(validate_person_request({
        'name': 'test name',
        'age': -1,
        'work': 'testing',
        'address': None
    })) > 0
    assert len(validate_person_request({
        'age': 42,
        'work': 'testing',
        'address': None
    })) > 0
