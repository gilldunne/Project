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
        team_list = []
        for team in list_of_teamName:
            list_of_buildjobs = {}
            query = c.find({"teamName":str(team)}).distinct("name")
            length = len(query)
            list_of_buildjobs.update({"name": team, "buildjob":length})
            team_list.append(list_of_buildjobs)
        return team_list


    # Use build_job collection from TestEasyJLV
    def get_team_names(self):
        c = self.db.buildjob
        list_of_team_names = c.find().distinct("teamName")
        return list_of_team_names

    # Get the user and the servers they are connected to
    def get_user_data(self):
        pass

    def get_end_dates(self):
        pass


