from pymongo import MongoClient


# remove this
client = MongoClient()
db = client.TestEasyJLV


class DBWrapper:

    client = MongoClient()
    db = client.TestEasyJLV

    # Open a connection to TestEasyJLV
    def db_open(self):
        return self.db

    # Close connection to TestEasyJLV
    def db_close(self):
        self.client.close()

    # Get all the domain names of the servers
    def get_domain_name_from_db(self):
        c = self.db.buildjob
        list_of_computer_names = c.find().distinct("computerName")
        return list_of_computer_names

    # Use build_job collection from TestEasyJLV
    def get_build_job_collection(self):
        c = self.db.buildjob
        list_of_teamName = self.get_team_names()
        list_of_buildjobs = []
        for team in list_of_teamName:
            query = c.find({"teamName":str(team)}).distinct("name")
            list_of_buildjobs.append(team)
            length = len(query)
            list_of_buildjobs.append(length)
        return list_of_buildjobs


    # Use build_job collection from TestEasyJLV
    def get_team_names(self):
        c = self.db.buildjob
        list_of_teamm_names = c.find().distinct("teamName")
        return list_of_teamm_names

    # Get the user and the servers they are connected to
    def get_user_data(self):
        pass

    def get_end_dates(self):
        pass


