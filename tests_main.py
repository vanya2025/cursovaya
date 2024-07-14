import json
import pytest
from main import get_last_five_operations

@pytest.fixture
def sample_operations(tmp_path):
    data = [
        {"id": 1, "date": "2023-07-14T10:00:00.000", "state": "EXECUTED", "operationAmount": {"amount": "1000", "currency": {"name": "RUB"}}, "description": "Перевод", "from": "1234567890123456", "to": "87654321"},
        {"id": 2, "date": "2023-07-13T10:00:00.000", "state": "EXECUTED", "operationAmount": {"amount": "2000", "currency": {"name": "RUB"}}, "description": "Перевод", "from": "6543210987654321", "to": "12345678"},
        {"id": 3, "date": "2023-07-12T10:00:00.000", "state": "CANCELED", "operationAmount": {"amount": "3000", "currency": {"name": "RUB"}}, "description": "Перевод", "from": "1111222233334444", "to": "99998888"},
        {"id": 4, "date": "2023-07-11T10:00:00.000", "state": "EXECUTED", "operationAmount": {"amount": "4000", "currency": {"name": "RUB"}}, "description": "Перевод", "from": "4444333322221111", "to": "88887777"},
        {"id": 5, "date": "2023-07-10T10:00:00.000", "state": "EXECUTED", "operationAmount": {"amount": "5000", "currency": {"name": "RUB"}}, "description": "Перевод", "from": "5555666677778888", "to": "77776666"},
        {"id": 6, "date": "2023-07-09T10:00:00.000", "state": "EXECUTED", "operationAmount": {"amount": "6000", "currency": {"name": "RUB"}}, "description": "Перевод", "from": "6666777788889999", "to": "66665555"}
    ]
    file_path = tmp_path / "operations.json"
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return file_path

def test_get_last_five_operations(sample_operations):
    result = get_last_five_operations(sample_operations)
    assert len(result) == 5
    assert "14.07.2023 Перевод" in result[0]
    assert "09.07.2023 Перевод" in result[-1]
