import pytest
from decimal import Decimal
from datetime import date
from furniture_sale import calculate_discount


_test_data_during_advent = [
    pytest.param(Decimal('0.01'), date(2022, 1, 1), Decimal('0.00'), id="1"),
    pytest.param(Decimal('0.01'), date(2022, 11, 25), Decimal('0.00'), id="2"),
    pytest.param(Decimal('0.01'), date(2022, 12, 27), Decimal('0.00'), id="3"),
    pytest.param(Decimal('0.01'), date(2022, 12, 31), Decimal('0.00'), id="4"),
    pytest.param(Decimal('0.01'), date(2022, 11, 30), Decimal('0.05'), id="5"),
    pytest.param(Decimal('0.01'), date(2022, 12, 22), Decimal('0.05'), id="6"),
    pytest.param(Decimal('0.01'), date(2022, 11, 26), Decimal('0.15'), id="7"),
    pytest.param(Decimal('0.01'), date(2022, 12, 24), Decimal('0.15'), id="8"),

    pytest.param(Decimal('99.99'), date(2022, 1, 1), Decimal('0.00'), id="9"),
    pytest.param(Decimal('99.99'), date(2022, 11, 25), Decimal('0.00'), id="10"),
    pytest.param(Decimal('99.99'), date(2022, 12, 27), Decimal('0.00'), id="11"),
    pytest.param(Decimal('99.99'), date(2022, 12, 31), Decimal('0.00'), id="12"),
    pytest.param(Decimal('99.99'), date(2022, 11, 30), Decimal('0.05'), id="13"),
    pytest.param(Decimal('99.99'), date(2022, 12, 22), Decimal('0.05'), id="14"),
    pytest.param(Decimal('99.99'), date(2022, 11, 26), Decimal('0.15'), id="15"),
    pytest.param(Decimal('99.99'), date(2022, 12, 24), Decimal('0.15'), id="16"),

    pytest.param(Decimal('100.00'), date(2022, 1, 1), Decimal('0.00'), id="17"),
    pytest.param(Decimal('100.00'), date(2022, 11, 25), Decimal('0.00'), id="18"),
    pytest.param(Decimal('100.00'), date(2022, 12, 27), Decimal('0.00'), id="19"),
    pytest.param(Decimal('100.00'), date(2022, 12, 31), Decimal('0.00'), id="20"),
    pytest.param(Decimal('100.00'), date(2022, 11, 30), Decimal('0.1'), id="21"),
    pytest.param(Decimal('100.00'), date(2022, 12, 22), Decimal('0.1'), id="22"),
    pytest.param(Decimal('100.00'), date(2022, 11, 26), Decimal('0.19'), id="23"),
    pytest.param(Decimal('100.00'), date(2022, 12, 24), Decimal('0.19'), id="24"),

    pytest.param(Decimal('100.01'), date(2022, 1, 1), Decimal('0.00'), id="25"),
    pytest.param(Decimal('100.01'), date(2022, 11, 25), Decimal('0.00'), id="26"),
    pytest.param(Decimal('100.01'), date(2022, 12, 27), Decimal('0.00'), id="27"),
    pytest.param(Decimal('100.01'), date(2022, 12, 31), Decimal('0.00'), id="28"),
    pytest.param(Decimal('100.01'), date(2022, 11, 30), Decimal('0.1'), id="29"),
    pytest.param(Decimal('100.01'), date(2022, 12, 22), Decimal('0.1'), id="30"),
    pytest.param(Decimal('100.01'), date(2022, 11, 26), Decimal('0.19'), id="31"),
    pytest.param(Decimal('100.01'), date(2022, 12, 24), Decimal('0.19'), id="32"),

    pytest.param(Decimal('499.99'), date(2022, 1, 1), Decimal('0.00'), id="33"),
    pytest.param(Decimal('499.99'), date(2022, 11, 25), Decimal('0.00'), id="34"),
    pytest.param(Decimal('499.99'), date(2022, 12, 27), Decimal('0.00'), id="35"),
    pytest.param(Decimal('499.99'), date(2022, 12, 31), Decimal('0.00'), id="36"),
    pytest.param(Decimal('499.99'), date(2022, 11, 30), Decimal('0.1'), id="37"),
    pytest.param(Decimal('499.99'), date(2022, 12, 22), Decimal('0.1'), id="38"),
    pytest.param(Decimal('499.99'), date(2022, 11, 26), Decimal('0.19'), id="39"),
    pytest.param(Decimal('499.99'), date(2022, 12, 24), Decimal('0.19'), id="40"),

    pytest.param(Decimal('500.00'), date(2022, 1, 1), Decimal('0.00'), id="41"),
    pytest.param(Decimal('500.00'), date(2022, 11, 25), Decimal('0.00'), id="42"),
    pytest.param(Decimal('500.00'), date(2022, 12, 27), Decimal('0.00'), id="43"),
    pytest.param(Decimal('500.00'), date(2022, 12, 31), Decimal('0.00'), id="44"),
    pytest.param(Decimal('500.00'), date(2022, 11, 30), Decimal('0.2'), id="45"),
    pytest.param(Decimal('500.00'), date(2022, 12, 22), Decimal('0.2'), id="46"),
    pytest.param(Decimal('500.00'), date(2022, 11, 26), Decimal('0.28'), id="47"),
    pytest.param(Decimal('500.00'), date(2022, 12, 24), Decimal('0.28'), id="48"),

    pytest.param(Decimal('500.01'), date(2022, 1, 1), Decimal('0.00'), id="49"),
    pytest.param(Decimal('500.01'), date(2022, 11, 25), Decimal('0.00'), id="50"),
    pytest.param(Decimal('500.01'), date(2022, 12, 27), Decimal('0.00'), id="51"),
    pytest.param(Decimal('500.01'), date(2022, 12, 31), Decimal('0.00'), id="52"),
    pytest.param(Decimal('500.01'), date(2022, 11, 30), Decimal('0.2'), id="53"),
    pytest.param(Decimal('500.01'), date(2022, 12, 22), Decimal('0.2'), id="54"),
    pytest.param(Decimal('500.01'), date(2022, 11, 26), Decimal('0.28'), id="55"),
    pytest.param(Decimal('500.01'), date(2022, 12, 24), Decimal('0.28'), id="56"),
]


@pytest.mark.parametrize("total,day,expected", _test_data_during_advent)
def test_prices_during_advent(total: Decimal, day: date, expected: Decimal):
    # Act
    actual = calculate_discount(day, total)
    # Assert
    assert actual == expected


_invalid_test_data = [
    pytest.param("leet", date(2022, 12, 24), id="1"),
    pytest.param(Decimal('0.00'), date(2022, 12, 24), id="2"),
    pytest.param(Decimal('-0.01'), date(2022, 12, 24), id="3"),
    pytest.param(Decimal('100.00'), "leet", id="4"),
    pytest.param(Decimal('100.00'), date(2022, 11, 27), id="5"),
    pytest.param(Decimal('100.00'), date(2022, 12, 26), id="6"),
]


@pytest.mark.parametrize("total,day", _invalid_test_data)
def test_invalid_arguments(total: Decimal, day: date):
    with pytest.raises(ValueError):
        calculate_discount(day, total)