import unittest
from unittest.mock import patch, MagicMock
from app.service.drinkrecordservice import (
    add_drink_record,
    get_drink_record,
    get_drink_record_by_id,
    update_drink_record,
    daily_goal_check
)
from app.model.drinkrecord import DrinkRecord
from azure.cosmos import exceptions

class TestDrinkService(unittest.TestCase):

    @patch('app.db.cosmosconfig.cosmos_db.drink_records_container.create_item')
    def test_add_drink_record(self, mock_create_item):
        # Arrange
        mock_create_item.return_value = None
        record = DrinkRecord(Id="test123", patient_id="patient1", amount_ml=500)

        # Act
        result = add_drink_record(record)

        # Assert
        mock_create_item.assert_called_once_with(body=record.dict(by_alias=True))
        self.assertEqual(result, record)

    @patch('app.db.cosmosconfig.cosmos_db.drink_records_container.query_items')
    def test_get_drink_record(self, mock_query_items):
        # Arrange
        mock_query_items.return_value = [
            {"id": "record1", "patient_id": "patient1", "amount_ml": 300}
        ]

        # Act
        result = get_drink_record("patient1")

        # Assert
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].patient_id, "patient1")
    #
    @patch('app.db.cosmosconfig.cosmos_db.drink_records_container.query_items')
    def test_get_drink_record_by_id(self, mock_query_items):
        # Arrange
        mock_query_items.return_value = [
            {"id": "record1", "patient_id": "patient1", "amount_ml": 300}
        ]

        # Act
        result = get_drink_record_by_id("record1")

        # Assert
        self.assertEqual(result.Id, "record1")
    #
    #Above 3 tests are working
    # @patch('app.db.cosmosconfig.cosmos_db.drink_records_container.query_items')
    # @patch('app.db.cosmosconfig.cosmos_db.container.replace_item')
    # def test_update_drink_record(self, mock_replace_item, mock_query_items):
    #     # Arrange
    #     mock_query_items.return_value = [
    #         {"Id": "record1", "patient_id": "patient1", "amount_ml": 300}
    #     ]
    #     mock_replace_item.return_value = None
    #
    #     # Act
    #     result = update_drink_record("record1", 500)
    #
    #     # Assert
    #     mock_replace_item.assert_called_once()
    #     self.assertEqual(result.amount_ml, 500)

    # @patch('app.service.patientservice.get_daily_goal_by_id')
    # @patch('app.service.drinkservice.get_drink_record')
    # def test_daily_goal_check_goal_reached(self, mock_get_drink_record, mock_get_daily_goal):
    #     # Arrange
    #     mock_get_drink_record.return_value = [
    #         DrinkRecord(id="record1", patient_id="patient1", amount_ml=600)
    #     ]
    #     mock_get_daily_goal.return_value = 600
    #
    #     # Act
    #     result = daily_goal_check("patient1")
    #
    #     # Assert
    #     self.assertEqual(result, "Goal has been reached. No need to drink more.")
    #
    # @patch('app.service.patientservice.get_daily_goal_by_id')
    # @patch('app.service.drinkservice.get_drink_record')
    # def test_daily_goal_check_goal_not_reached(self, mock_get_drink_record, mock_get_daily_goal):
    #     # Arrange
    #     mock_get_drink_record.return_value = [
    #         DrinkRecord(id="record1", patient_id="patient1", amount_ml=200)
    #     ]
    #     mock_get_daily_goal.return_value = 500
    #
    #     # Act
    #     result = daily_goal_check("patient1")
    #
    #     # Assert
    #     self.assertEqual(result, "300 ml left to reach the daily goal.")

if __name__ == '__main__':
    unittest.main()
