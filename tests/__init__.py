from __future__ import unicode_literals
from finix.resources import *

import uuid
import datetime

# DEFAULT_API_URL = os.environ.get('PROCESSING_URL')
SYNC_UNDERWRITING_LAST_NAME = "Sunkhronos"
DUMMY_PROCESSOR = "DUMMY_V1"
DISPUTED_AMOUNT = 888888


def sample_user():
    return User(enabled=True)


def sample_processor():
    return Processor(name=DUMMY_PROCESSOR, type=DUMMY_PROCESSOR, config={"key1": "value-1", "key2": "value-2"})


def sample_entity():
    now = datetime.datetime.now()
    return {
        "first_name": "xdwayne",
        "last_name": SYNC_UNDERWRITING_LAST_NAME,
        "email": "xuser@example.org",
        "business_name": "business inc 2",
        "business_type": "LIMITED_LIABILITY_COMPANY",
        "url": "http://sample.company.com",
        "doing_business_as": "xdoingBusinessAs",
        "phone": "x1234567890",
        "business_phone": "+1 (408) 756-4497",
        "tax_id": "x123456789",
        "business_tax_id": "x123456789",
        "default_statement_descriptor": "sample",
        "incorporation_date": {"day": now.day, "month": now.month, "year": now.year - 1},
        "principal_percentage_ownership": 10,
        "personal_address": {
            "line1": "741 Douglass St",
            "line2": "Apartment 7",
            "city": "San Mateo",
            "region": "CA",
            "postal_code": "94114",
            "country": "USA"
        },
        "business_address": {
            "line1": "741 Douglass St",
            "line2": "Apartment 7",
            "city": "San Mateo",
            "region": "CA",
            "postal_code": "94114",
            "country": "USA"
        },
        "mcc": 7399,
        "dob": {
            "day": 27,
            "month": 5,
            "year": 1978
        },
        "max_transaction_amount": 1,
        "settlement_currency": "USD",
        "settlement_bank_account": "CORPORATE",
        "annual_card_volume": 100
    }


def sample_application():
    return Application(entity=sample_entity())


def sample_invalid_application():
    return Application(entity=sample_entity())


def sample_identity():
    return Identity(entity=sample_entity())


def sample_underwriting():
    return Merchant(processor=DUMMY_PROCESSOR)


def sample_payment_card():
    return PaymentCard(
        name=sample_name(),
        expiration_month=12,
        expiration_year=2030,
        number="4111 1111 1111 1111",
        security_code=231
    )


def sample_name():
    return "Joe-{} Doe-{}".format(uuid.uuid4().hex, uuid.uuid4().hex)


def sample_bank_account():
    return BankAccount(
        name=sample_name(),
        account_number="84012312415",
        bank_code="840123124",
        account_type="SAVINGS",
        company_name="sample company",
        country="USA",
        currency="USD"
    )


def sample_transfer(merchant_identity, source):
    return Transfer(
        merchant_identity=merchant_identity,
        source=source,
        currency="USD",
        amount=DISPUTED_AMOUNT,
        tags={"name": "sample_tag"},
        processor=DUMMY_PROCESSOR
    )


def sample_authorization(merchant_identity, source):
    return Authorization(
        amount=100,
        processor=DUMMY_PROCESSOR,
        source=source,
        merchant_identity=merchant_identity
    )


def sample_settlement():
    return Settlement(
        processor=DUMMY_PROCESSOR,
        currency="USD"
    )


def sample_verification():
    return Verification(
        processor=DUMMY_PROCESSOR
    )
