from rest_framework.decorators import api_view
from rest_framework.response import Response

# Get all the domain names of the servers
from DashBoardIBM.db_wrapper import DBWrapper
from django.shortcuts import render_to_response

# OK the views I think should be on per graph/table in the project

@api_view(['GET', ])
# def get_domain_names(request):
#     # OK so we have the names, what are you going to do with them
#     db = DBWrapper()
#     db.db_open()
#
#     data = db.get_domain_name_from_db()
#     db.db_close()
#
#     return Response(data)

# Get all the regions
@api_view(['GET', ])
# def get_regions(request):
#     # not sure if getting the region from the url is a good idea
#     # what if it changes in the future? If it where me add a column in the db with this info
#
#     # So the region on it's own is not that useful, teams within a given region could be useful
#     # So what graphs would do good here?. I'm thinking a two tables one with the list of regions and when you click one
#     # it will list the the teams in the other
#     return Response("get_regions")

# Get all the build jobs per domain name
@api_view(['GET', ])
def get_build_job_collection(request):
    # List of build jobs for a given Team
    db = DBWrapper()
    db.db_open()
    data = db.get_build_job_collection()
    db.db_close()
    return Response(data)


# Get all the users per domain name
# @api_view(['GET', ])
# def get_user_data(request):
#     # get a list users for a given domain, so them in a table?
#     return Response("get_user_data")

# @api_view(['GET', ])
# def get_end_dates(request):
#     # this one is for the active and inactive domains.
#     # I would re name it to something with more meaning
#     return Response("get_end_dates")

# @api_view(['GET', ])
# def prepare_graph_data(request):
#     # is this one for the graph above?
#     return Response("prepare_graph_data")
