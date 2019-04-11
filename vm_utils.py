
from utils import run_subprocess_cmd

def create_vm(vm_name, region):
    cmd = ['gcloud', 'compute', 'instances', 'create', vm_name, '--zone', region]
    error, response = run_subprocess_cmd(cmd)
    if (error):
        print("Error:: Not able to create the instance %s"%error)
        exit
    print(response)
    return response 

def update_vm(vm_name, region):
    cmd = ['gcloud', 'compute', 'instances', 'update', vm_name, '--zone', region, '--format json']
    error, response = run_subprocess_cmd(cmd)
    if (error):
        print("Error:: Not able to update the instance")
        exit
    print(response)
    return response 