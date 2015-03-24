import datetime
from pymongo import MongoClient
from datetime import timedelta, datetime


# remove this
import sys

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
        list_of_teamName = self.get_distinct_list("teamName", None)
        team_list = []
        for team in list_of_teamName:
            list_of_buildjobs = {}
            query = c.find({"teamName":str(team)}).distinct("name")
            length = len(query)
            list_of_buildjobs.update({"name": team, "buildjob":length})
            team_list.append(list_of_buildjobs)
        return team_list

    def get_build_job_collection_component_names(self, teamName):
        c = self.db.buildjob
        distinct_query = {"teamName": teamName}
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
        # TODO - Test query where query equals none
        list_of_distinct_names = c.find(query).distinct(collection_key)
        return list_of_distinct_names

    # Get the user and the servers they are connected to
    def get_user_data(self):
        pass

    def get_end_dates(self):
        pass

    def get_active_inactive_per_team(self, teamName):
        c = self.db.buildjob
        distinct_query = {"teamName": teamName}
        list_of_componentName = self.get_distinct_list("componentName", distinct_query)
        team_list = [] # TODO - Rename this bad name
        for component in list_of_componentName:
            list_of_data = {} # TODO - Rename this bad name
            list_of_distinct_buildjobs = c.find({"componentName":str(component)}).distinct("name")
            freq = { "InUse":0, "NotInUse":0 } # create obj

            # get the last date of a give buildjob
            for buildjob in list_of_distinct_buildjobs:
                buildjob_date = c.find({"name":str(buildjob)},{"endDate":1}).sort("endDate",-1).limit(1)
                print >> sys.stderr, buildjob_date[0]["endDate"]

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
        print >> sys.stderr, buildjob_date
        if buildjob_date >= last_seven_days:
            return True
        return False

    #TODO - Add in the number of servers

    def get_build_job_usage(self, componentName):
        c = self.db.buildjob
        distinct_query = {"componentName": componentName}
        sub_teams = []
        list_of_subTeam = self.get_distinct_list("subTeam", distinct_query)
        for sub_team in list_of_subTeam:
            list_of_buildjobs = {}
            query = c.find({"subTeam":str(sub_team)}).distinct("name")
            length = len(query)
            list_of_buildjobs.update({"count":length, "status": sub_team})
            sub_teams.append(list_of_buildjobs)
        return sub_teams
