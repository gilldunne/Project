from django.test import TestCase
from datetime import timedelta, datetime
import pymongo
from DashBoardIBM.db_wrapper import DBWrapper

class TestEndDate(TestCase):

    def test_end_date_is_active_in_use(self):
        # arrange - set the date to be passed to the function
        db = DBWrapper()
        date = datetime.today()
        # act - pass the date to the function
        result = db.is_inactive(date)
        # assert - response should be true as date is > 7 days ago
        self.assertTrue(result)

    def test_end_date_is_active_not_in_use(self):
        # arrange - set the date to be passed to the function
        db = DBWrapper()
        date = datetime.today() - timedelta(days=8)
        # act - pass the date to the function
        result = db.is_inactive(date)
        # assert - response should be false as date is < 7 days ago
        self.assertFalse(result)


class TestAllServers(TestCase):

    def test_get_build_job_collection(self):
        # arrange
        url = ('/api/get_build_job_collection?computerName=test1.ie.ibm.com')
        expected = [
            {"buildjob": 5, "name": "Unyte Team"},
            {"buildjob": 11, "name": "Connections Team"},
            {"buildjob": 5,  "name": "Cloud Platform Team"},
            {"buildjob": 2, "name": "IBM Docs Team"},
            {"buildjob": 15, "name": "SameTime Team"},
            {"buildjob": 0, "name": "Foundations Team"}
        ]
        # act
        response = self.client.get(url, format='json')
        # assert
        return self.assertEqual(response.data, expected)

    def test_get_build_job_collection_component_names(self):
        # arrange
        url = ('/api/get_build_job_collection_component_names?teamName=Connections%20Team&computerName=test1.ie.ibm.com')
        expected = [
            {"buildjob": 7, "name": "Connections"},
            {"buildjob": 4, "name": "Social Contacts"}
        ]
        # act
        response = self.client.get(url, format='json')
        # assert
        return self.assertEqual(response.data, expected)


