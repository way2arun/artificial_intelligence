# googlecloud
Google Cloud Automation

This is one kind of sample to show the power and richness of the google cloud automation, the intention behind this code is to demonstrate
provisioning of the resources on cloud through gcloud.

Pre-Requisites 
Download the Google Cloud SDK installer.
    https://cloud.google.com/sdk/docs/quickstart-windows

1. Allows each Business Unit/Products to create it's own Variable file
2. build_google_cloud.py - reads the input json variable file and calls the right resource provisioning modules.
3. This approach will help to handle different BUs or Products and able to keep the state file separate for maintaining.
4. More Development required to keep the credentials to keep it on the KeyVault etc.
