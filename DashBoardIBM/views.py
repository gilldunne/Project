from rest_framework.decorators import api_view
from rest_framework.response import Response

# Get all the domain names of the servers
from DashBoardIBM.db_wrapper import DBWrapper
from django.shortcuts import render_to_response

# Get all the build jobs per domain name
@api_view(['GET', ])
def get_build_job_collection(request):
    """
    get_build_job_collection
    """
    # List of build jobs for a given Team
    region = request.GET.get("computerName")
    db = DBWrapper()
    db.db_open()
    data = db.get_build_job_collection(region)
    db.db_close()
    return Response(data)


@api_view(['GET', ])
def get_active_inactive_per_team(request):
    # List of build jobs for a given Team
    team_name = request.GET.get("teamName")
    region = request.GET.get("computerName")
    db = DBWrapper()
    db.db_open()
    data = db.get_active_inactive_per_team(team_name, region)
    db.db_close()
    return Response(data)


@api_view(['GET', ])
def get_build_job_collection_component_names(request):
    # List of build jobs for a given Team
    """
    get_build_job_collection_component_names
    """
    team_name = request.GET.get("teamName")
    region =  request.GET.get("computerName")
    db = DBWrapper()
    db.db_open()
    data = db.get_build_job_collection_component_names(team_name, region)
    db.db_close()
    return Response(data)


@api_view(['GET', ])
def get_build_job_usage_sub_teams(request):
    region =  request.GET.get("computerName")
    component_name = request.GET.get("componentName")
    db = DBWrapper()
    db.db_open()
    data = db.get_build_job_usage(component_name, region)
    db.db_close()
    return Response(data)
