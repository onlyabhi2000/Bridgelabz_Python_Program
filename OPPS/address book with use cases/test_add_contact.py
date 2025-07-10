
import pytest
from address_book_main import AddressBook
from person import Person
from regex_validate import validate_person_data



@pytest.fixture
def addres_book():
    return AddressBook("TestBook")

@pytest.mark.parametrize(
    "first_name, last_name, address, city, state, zip_code, phone, email, should_be_valid",
    [
        ("Abhi", "Sharma", "LAPATA", "DHN", "BIHAR", "452001", "9988776655", "abhi@gmail.com", True),
        ("balaji", "sapkal", "kolhapur", "pune", "maharastra", "560001", "1234567890", "bala@gmail.com", True),
        ("Abhi123", "Sharma", "LAPATA", "DHN", "BIHAR", "452001", "9988776655", "abhi@@gmail.com", False)
    ]
)
def test_add_contact_with_data(
    addres_book,
    first_name, last_name, address, city, state, zip_code, phone, email, should_be_valid
):
    person = Person(
        first_name=first_name,
        last_name=last_name,
        address=address,
        city=city,
        state=state,
        zip_code=zip_code,
        phone=phone,
        email=email
    )

    is_valid = validate_person_data(person)
    assert is_valid == should_be_valid

    if should_be_valid:
        addres_book.add_contact(person)
        assert addres_book.contacts[0].first_name == first_name
    else:
        assert len(addres_book.contacts) == 0
