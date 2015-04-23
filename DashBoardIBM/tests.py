from django.test import TestCase


class TestGetAllBuildJobs(TestCase):

    def test_get_build_job_collection_component_names(self):
        url = ('/api/get_build_job_collection?computerName=test1.ie.ibm.com')
        response = self.client.get(url, format='json')
        expected = [
            {
                "buildjob": 5,
                "name": "Unyte Team"
            },
            {
                "buildjob": 11,
                "name": "Connections Team"
            },
            {
                "buildjob": 5,
                "name": "Cloud Platform Team"
            },
            {
                "buildjob": 2,
                "name": "IBM Docs Team"
            },
            {
                "buildjob": 15,
                "name": "SameTime Team"
            },
            {
                "buildjob": 0,
                "name": "Foundations Team"
            }
        ]
        self.assertEqual(response.data, expected)



