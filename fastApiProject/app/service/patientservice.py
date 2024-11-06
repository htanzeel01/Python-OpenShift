from app.db.cosmosconfig import cosmos_db
from app.model.patient import Patient
from azure.cosmos import exceptions


def get_daily_goal_by_id(patient_id: str) -> float:
    try:
        query = "SELECT c.DailyGoal FROM c WHERE c.Id=@patient_id"
        parameters = [
            {"name": "@patient_id", "value": patient_id}
        ]

        items = list(cosmos_db.patients_container.query_items(
            query=query,
            parameters=parameters,
            enable_cross_partition_query=True
        ))
        if not items:
            raise ValueError("Patient not found")

        print(f"Patient's daily goal: {items[0]['DailyGoal']}")  # Debug statement
        return items[0]['DailyGoal']

    except exceptions.CosmosHttpResponseError as e:
        print(f"Failed to retrieve patient's daily goal: {e}")
        raise e

