import subprocess
import json
import os

def check_directory(dirname):
    """Check if it is a directory, then further actions on the directory"""
    if not dirname or not os.path.exists(dirname) or not os.path.isdir(dirname):
        return False
    return True


def check_filename(filename):
    """Check the file if exists before any further operations on it"""
    if not filename or not os.path.exists(filename) or not os.path.isfile(filename):
        return False
    return True

def load_json_input(result):
    """Load json data from the file."""
    jsondata = None
    try:
        jsondata = json.loads(result)
    except:
        pass
    return jsondata
def load_json(filename):
    """Load json data from the file."""
    jsondata = None
    try:
        if check_filename(filename):
            with open(filename) as jsonfile:
                jsondata = json.load(jsonfile)
    except:
        print('Failed to load json from file: %s' %filename)

    return jsondata


def run_subprocess_cmd(cmd):
    """ Run a sub-process command"""
    result = '[]'
    errresult = None
    if cmd:
        if isinstance(cmd, list):
            cmd = ' '.join(cmd)
        myprocess = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     stdin=subprocess.PIPE)
        out, err = myprocess.communicate()
        result = out.rstrip()
        errresult = err.rstrip() if err else None
        if isinstance(result, bytes):
            result = result.decode()
        if errresult and isinstance(errresult, bytes):
            errresult = errresult.decode()
    return errresult, result

def get_json_field_value(data, parameter):
    """Utility to get json value from a nested structure."""
    retval = None
    if data and parameter:
        fields = parameter.split('.')
        retval = data
        for field in fields:
            if retval:
                if field in retval:
                    retval = retval[field]
                else:
                    retval = None
    return retval
