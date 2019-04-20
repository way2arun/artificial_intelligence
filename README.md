## Google Automation Deployment Framework
Google automation framework defines the process of spinning up environments on Google cloud for different business units. The goal is to give a solid foundational platform and eco-system to accelerate adoption of Cloud by different business units/teams in an agile, secure, and cost effective way.

&NewLine;
&NewLine;
## Table of Contents

 1. [Prerequisite](#prerequisite)
 2. [Development Environment Prerequisite](#Development-Environment-Prerequisite)
 3. [Software Installation on Developer Workstations](#Installation)
 4. [Google Automation Framework](#googleframework)
 5. [Google AI Project](#google-ai-project)
&NewLine;
&NewLine;
### 1. Prerequisite 
* Ensure following access are in place before you start:
	- Google Cloud Console
	- Source Code Repository / Git-Hub / BitBucket
	- Google Documents
	- Development VM (Linux/Windows)
&NewLine;	
&NewLine;
### 2. Development Environment Prerequisite 
Once the Prerequisites(#prerequisite) are in place, below softwares needs to be installed on development VM assigned to developer. Google Automation framework will be executed and deployed through a different Server, (to seggregate the duties). Ensure any codes are tested on Windows and on Linux Servers.
&NewLine;
- Developer Studio
- RHEL and Windows VM
- Google gcloud SDK 242.0.0 (https://cloud.google.com/sdk/docs/)
- Python 3.5+ 
- Vaults for securing Credentials (This is a question to Google Subject Matter Experts, as of now its not enabled)
- SourceTree or git bash for source control management.
&NewLine;
&NewLine;
### 3. Software Prerequisite installation 
&NewLine;
#### RHEL 7.4
&NewLine;
- gcloud sdk:
```
    1. https://cloud.google.com/appengine/docs/standard/go/download
```
&NewLine;
- Python3.5+: 
&NewLine;	
```
	1. Install python on linux machines
```
&NewLine;
- Git Client:		
&NewLine;
``` 
	1. Install git client
	2. Important steps to clone repo, since there had been issues with linux VM.
		a) git config --global http.sslverify false
		b) git config --global user.email "abc@arun.com"
		c) git clone "repo url"
	3. Do not modify or directly use master branch on bitbucket. Create branches from master and follow instruction while merging to master.
	4. Important note to avoid conflict when merging the code and before sending Pull Request
		a) Push the code from your current branch to remote
		b) Switch to the master
		c) git pull
		d) Switch back to your branch
		e) Git merge master
		f) Resolve conflicts
		g) Push the code
		h) Send a PR
```
&NewLine;	

&NewLine;
### 4. Google Automation Framewor
&NewLine;
#### 1. GSuiteFrame     
Framework consist of environments, parameters and logs as described below:
This is one kind of sample to show the power and richness of the google cloud automation, the intention behind this code is to demonstrate provisioning of the resources on cloud through gcloud.

&NewLine;
- Environments
  Environments folder consist of environment build templates and scripts used for spinning up environments for projects residing on google cloud. Following environment structures defined and used based on the releases and requirements.
&NewLine; 
```
    compute
    management
    network
    policy
    policy-set
    roles
    scripts
    security
    spn
    storage
```
&NewLine; 
&NewLine; 
This approach will provide prescriptive guidance on automated provisioning of infrastructure and applications.
1. Allows each Business Unit/Products to create it's own Variable file
2. build_google_cloud.py - reads the input json variable file and calls the right resource provisioning modules.
3. This approach will help to handle different BUs or Products and able to keep the state file separate for maintaining.
4. More Development required to keep the credentials to keep it on the KeyVault etc. (have to check with Google Cloud Subject Matter Expert on the details)
&NewLine; 
&NewLine;
### 5. Google AI Project
&NewLine;
&NewLine;
Google Image Vision API can detect and extract text from images.TEXT_DETECTION detects and extracts text from any image. For example, a photograph might contain a Ingrediants/Nutrition details. The JSON includes the entire extracted string, as well as individual words, and their bounding boxes.
&NewLine;
### Projects
Google Cloud Platform resources must belong to a project. Project consists of the settings, permissions and other metadata that describes the applications.
&NewLine;
&NewLine;
Each Project has:
&NewLine;
```
    1. A project name, which we provide.
    2. A project ID, which we can provide or Google Cloud Platform can provide for us (have to check with Google Subject Matter Expert).
    3. A project number, which Google Cloud Platform provides.
```
&NewLine;
### About the Project
This project is about Nutrition Fact Checking Application, it detects an image, and read through the ingrediants or nutritions, identifies the Calories, fats, proteins, sugar, sodium carbs etc. Once we get the information we can send the data back to the user stating the nutrition facts, like if sugar is greater than 24grams, its not good for the health in the long run, like how much sodium should take, (data collection is not fully completed)
Currently am using the credentials in a json file, which is not the right way to go for it, (will  be checking with Google Subject Matter Experts to understand this.)
&NewLine;
&NewLine;
```
    Check the resources folder, where you can see a cocacola.jpg, the application reads throguh the image and identifies the nutrition facts, this shows the richness of the google AI apis and its usages.
    ![cocacoala](https://raw/githubusercontent.com/way2arun/googlecloud/blob/master/google-ai/resources/cocacola.jpg)
    
```
&NewLine;
&NewLine;
```
    Note:: I cannot able to commit the authorization json, as it contains most protected confidential informations.
    Happy Coding
```

