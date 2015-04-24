import datetime
from pymongo import MongoClient
from datetime import timedelta, datetime


class DBWrapper:

    client = MongoClient()
    db = client.TestTeams

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

    # Use build_job collection from db
    # Get all the distinct buildjobs from the DB and
    # get a count to show the number of servers per team
    def get_build_job_collection(self, region):
        c = self.db.buildjob
        list_of_teamName = self.get_distinct_list("teamName", None)
        region_name = region
        team_list = []
        for team in list_of_teamName:
            list_of_buildjobs = {}
            if(region == "null"):
                query = c.find({"teamName":str(team)}).distinct("name")
            else:
                query = c.find({"teamName":str(team), "computerName":str(region_name)}).distinct("name")
            length = len(query)
            list_of_buildjobs.update({"name": team, "buildjob":length})
            team_list.append(list_of_buildjobs)
        return team_list

    def get_build_job_collection_component_names(self, teamName):
        c = self.db.buildjob
        distinct_query = {"teamName": teamName}
        # region_name = self.get_regions()
        list_of_componentName = self.get_distinct_list("componentName", distinct_query)
        team_list = []
        for component in list_of_componentName:
            list_of_buildjobs = {}
            query = c.find({"componentName":str(component)}).distinct("name")
            length = len(query)
            list_of_buildjobs.update({"name": component, "buildjob":length})
            team_list.append(list_of_buildjobs)
        return team_list

    def get_distinct_list(self, collection_key, query):
        c = self.db.buildjob
        list_of_distinct_names = c.find(query).distinct(collection_key)
        return list_of_distinct_names

    def get_active_inactive_per_team(self, teamName):
        c = self.db.buildjob
        distinct_query = {"teamName": teamName}
        # region_name = self.get_regions()), "computerName":str(region_name)
        list_of_componentName = self.get_distinct_list("componentName", distinct_query)
        team_list = [] # TODO - Rename this bad name
        for component in list_of_componentName:
            list_of_data = {} # TODO - Rename this bad name
            list_of_distinct_buildjobs = c.find({"componentName":str(component)}).distinct("name")
            freq = { "InUse":0, "NotInUse":0 } # create obj

            # get the last date of a give buildjob
            for buildjob in list_of_distinct_buildjobs:
                buildjob_date = c.find({"name":str(buildjob)},{"endDate":1}).sort("endDate",-1).limit(1)

                # decide on active or inactive
                if self.is_inactive(buildjob_date[0]["endDate"]):
                    new_inuse = freq["InUse"] +1
                    freq["InUse"] = new_inuse
                else:
                    new_notinuse = freq["NotInUse"] +1
                    freq["NotInUse"] = new_notinuse

            list_of_data.update({"name": component, "freq":freq})
            team_list.append(list_of_data)
        return team_list

    def is_inactive(self, buildjob_date):
        last_seven_days = datetime.today() - timedelta(days=7)
        if buildjob_date >= last_seven_days:
            return True
        return False

    def get_build_job_usage(self, componentName, region):
        c = self.db.buildjob
        distinct_query = {"componentName": componentName}
        region_name = region
        sub_teams = []
        list_of_subTeam = self.get_distinct_list("subTeam", distinct_query)

        for sub_team in list_of_subTeam:
            list_of_buildjobs = {}
            query = c.find({"componentName": str(componentName),"subTeam":str(sub_team), "computerName":str(region)}).distinct("name")
            length = len(query)
            list_of_buildjobs.update({"count":length, "status": sub_team})
            sub_teams.append(list_of_buildjobs)
        return sub_teams

    # def get_regions(self, region_name):
    #     c = self.db.buildjob
    #     self.regionN = region_name
    #     list_domain_name = self.get_domain_name_from_db()
    #     region = ""
    #     for name in list_domain_name:
    #         if(name == region_name):
    #             region = region_name
    #     return region