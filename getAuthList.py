from utils import run_subprocess_cmd, load_json_input

def list_google_auth():
    cmd = ['gcloud', 'auth', 'list ' '--format json']
    error, result = run_subprocess_cmd(cmd)
    if (error):
        print("Error:: Not able to list the Auth List -google")
    return load_json_input(result)

def  main():
    accounts = list_google_auth()
    for account in accounts:
        print(account['account'])
        print(account['status'])
    
if __name__ == "__main__":
    main()