from utils import run_subprocess_cmd, load_json_input
from updateProject import update_google_project

def create_google_project(project_id:str, project_name:str):
  cmd = ['gcloud', 'projects', 'create', project_id, '--name ',project_name, '--set-as-default', ' --format json' ]
  error, result = run_subprocess_cmd(cmd)
  if (error):
        if "project ID you specified is already in use by another project" in error:
          print("Error:: This project is already created, so updating it.")
          #Lets do update
          result = update_google_project(project_id, project_name)
        else:
          print("Error:: Not able to Create the Project %s"%error)
  return result


project = create_google_project("arun-acton-1234", "arunactontest")
print(project)