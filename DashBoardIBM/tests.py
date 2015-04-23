from django.test import TestCase


class TestGetAllBuildJobs(TestCase):

    def test_get_build_job_collection_component_names(self):
        url = ('/api/get_build_job_collection')
        response = self.client.get(url, format='json')
        expected = [
            {'buildjob': 6, 'name': u'Unyte Team'},
            {'buildjob': 11, 'name': u'Connections Team'},
            {'buildjob': 9, 'name': u'Cloud Platform Team'},
            {'buildjob': 7, 'name': u'IBM Docs Team'},
            {'buildjob': 19, 'name': u'SameTime Team'},
            {'buildjob': 6, 'name': u'Foundations Team'}
        ]
        self.assertEqual(response.data, expected)



