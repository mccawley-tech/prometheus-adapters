import requests
import time
import os
from prometheus_client import start_http_server, Summary, Counter, Gauge

github_api_token = os.environ['GITHUB_PAT']
organisation_name = os.environ['GITHUB_ORG']

default_headers ={
        "Accept":"application/vnd.github+json",
        "Authorization":f"Bearer {github_api_token}"}

action_minutes_remaining = Gauge('GitHub_actions_minutes_remaining', 'Total number of minutes remaining in GitHub actions')

def get_repositories():
    response = requests.get(url=f"https://api.github.com/orgs/{organisation_name}/repos", 
    headers=default_headers)
    return map(lambda x: x['name'], list(response.json()))

def get_deployments(org, repo):
    resp = requests.get(url=f"https://api.github.com/repos/{organisation_name}/{repo}/deployments", headers=default_headers)


def get_billing_minutes_remaining():
    response = requests.get(url=f"https://api.github.com/orgs/{organisation_name}/settings/billing/actions", headers=default_headers)
    data = response.json()
    return int(data['included_minutes']) - int(data['total_minutes_used'])

if __name__ == '__main__':
    start_http_server(3300)
    while True:
        action_minutes_remaining.set(get_billing_minutes_remaining())
        time.sleep(30)
