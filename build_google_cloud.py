import json
import os
from utils import load_json,get_json_field_value
from createProject import create_google_project
from getAuthList import list_google_auth
from vm_utils import create_vm, update_vm

def read_variable_file():
    
    auth_lists = list_google_auth()
    for auth_list in auth_lists:
        print("You are :- %s" %auth_list['account'])
    project_file_name = "C:\\Users\\aruna\\Desktop\\Azure\\myDatas\\src\\google\\myproject.json"
    project_json = load_json(project_file_name)
    
    project_details_parameter = 'googleCloud.projectDetails'
    project_details = get_json_field_value(project_json,project_details_parameter)

    for projects in project_details:
        project_id = projects['project_id']
        project_name = projects['project_name']
        response = create_google_project(project_id, project_name)
        print(response)
       
    instance_details_parameter = 'googleCloud.instances'
    instance_details = get_json_field_value(project_json,instance_details_parameter)
    for instances in instance_details:
        instance_name = instances['instance_name']
        cpu = instances['cpu']
        region = instances['region']
        response = create_vm(instance_name, region)
        print(response)




def main():
    """Build Google Cloud Pipeline file"""
    read_variable_file()

if __name__ == "__main__":
    main()


    