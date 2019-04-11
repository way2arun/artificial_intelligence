from utils import run_subprocess_cmd, load_json_input

def update_google_project(project_id:str, project_name:str):
    cmd = ['gcloud', 'projects', 'update', project_id, '--name ',project_name, ' --format json' ]
    error, result = run_subprocess_cmd(cmd)
    if (error) and "Updated" not in error:
        print("Error:: Not able to update the Project %s"%error)
    return result


project = update_google_project("arun-acton-1234", "arunactontest")
print(project)