from flask import Flask, request,render_template, request, redirect, url_for, jsonify
from sys import argv
import hmac,requests
import hashlib
import subprocess
import os
import json,base64
from requests.exceptions import HTTPError
import configparser

app = Flask(__name__)
#run_with_ngrok(app)  # Start ngrok when app is run
access_token=os.environ['ACCESS_TOKEN']
bear_token=os.environ['BEAR_TOKEN']

@app.route('/',methods=['POST'])
def foo():
   data = json.loads(request.data)
   print(request.headers.get('X-GitHub-Event'))
   print(f"New Json response like: {data}")
   return "OK"

def verify_hmac_hash(data, signature):
    github_secret = bytes(os.environ['GITHUB_SECRET'], 'UTF-8')
    mac = hmac.new(github_secret, msg=data, digestmod=hashlib.sha1)
    return hmac.compare_digest('sha1=' + mac.hexdigest(), signature)

def get_url(*args):
    """
    Form a git api path
    """
    return '/'.join(('https://api.github.com', 'repos', *args))

def create_file(*args):
   repo=args[0]
   path=args[1]
   api_url=get_url(repo,'contents',path)

   #encoded_64=base64.b64encode(bytes('First File to Push', 'utf-8'))
   info_file={
      "message": "README.md",
      "committer": {
         "name": "Github",
         "email": "github@github.com"
         },
      "content": "bXkgbmV3IGZpbGUgY29udGVudHM=",
      "branch": "master"
      }   
   header_info={
      'Authorization': f'Token {access_token}'
      }
   print(api_url+" create_file")
   try:
      r=requests.put(api_url,headers=header_info,json = info_file)
      # If the response was successful, no Exception will be raised
      r.raise_for_status()
      return r.json()
   except HTTPError as http_err:
      print(f'HTTP error occurred: {http_err}')  # Python 3.6
   except Exception as err:
      print(f'Other error occurred: {err}')  # Python 3.6
   else:
        print('Success!')

def check_branch(*args):
   repo=args[0]
   branch=args[1]
   #api_url=get_url(repo,'git/refs/heads',branch)
   api_url=get_url(repo,'branches',branch)
   header_info={
      'Authorization': f'Token {access_token}'
      }
   try:
      r=requests.get(api_url,headers=header_info)
      # If the response was successful, no Exception will be raised                                                    
      r.raise_for_status()
      return r.status_code
   except HTTPError as http_err:
      print(f'HTTP error occurred: {http_err}')  # Python 3.6 
   except Exception as err:
      print(f'Other error occurred: {err}')  # Python 3.6                                                    
   else:
        print('Success!')

def get_restrictions(*args):
   repo=args[0]
   branch="master"
   header_info={
      'Authorization': f'Token {access_token}'
      }
   api_url=get_url(repo,"branches",branch,"protection")
   try:
      r=requests.get(api_url,headers=header_info)
      # If the response was successful, no Exception will be raised                                                                            
      r.raise_for_status()
      return r.json()
   except HTTPError as http_err:
      print(f'HTTP error occurred: {http_err}')  # Python 3.6                                                                                                                   
   except Exception as err:
      print(f'Other error occurred: {err}')  # Python 3.6                                                                                                                  
   else:
        print('Success!')
   
def create_issue(*args):
   repo=args[0]
   assign=args[1]
   restrictions=get_restrictions(repo)
   print(restrictions)
   header_info={
      'content-type': 'application/json',
      'Authorization': f'Bearer {bear_token}'
      }
   api_url=get_url(repo,"issues")
   info_des=f"""
@{assign}
- [master] branch protection added to repository: {repo} to all members of organization
- Approvers are now required
- ```json
    {restrictions}
  ```
"""
   issue_m={
      "title": "Found a protected repo "+repo,
      "body": info_des,
      "assignees": [assign],
      }
   print(issue_m)
   print(api_url)
   try:
      r=requests.post(api_url,json = issue_m,headers=header_info)
      # If the response was successful, no Exception will be raised
      r.raise_for_status()
      return r.json()
   except HTTPError as http_err:
      print(f'HTTP error occurred: {http_err}')  # Python 3.6 
   except Exception as err:
      print(f'Other error occurred: {err}')  # Python 3.6                                                                    
   else:
        print('Success!')

def restrict_permission(*args):
   repo = args[0]
   branch = args[1]
   #owner = args[2]
   api_url=get_url(repo,'branches',branch,'protection')
   info_restriction={
      "required_status_checks": {
         "strict": True,
         "contexts": []
         },
      "enforce_admins": True,
      "required_pull_request_reviews": {
         "dismissal_restrictions": {
            "users": [],
            "teams": []
            },
         "dismiss_stale_reviews": True,
         "require_code_owner_reviews": True,
         "required_approving_review_count": 1
         },
      "restrictions": {
         "users": [],
         "teams": []
         }
      }
   
   header_info={
      'Accept': 'application/vnd.github.luke-cage-preview+json',
      'Authorization': f'Token {access_token}'
      }
   print(api_url)
   try:
      r=requests.put(api_url,headers=header_info,json = info_restriction)
      # If the response was successful, no Exception will be raised
      r.raise_for_status()
      return r.json()
   except HTTPError as http_err:
      print(f'HTTP error occurred: {http_err}')  # Python 3.6                                             
   except Exception as err:
      print(f'Other error occurred: {err}')  # Python 3.6                                                                   
   else:
        print('Success!')

@app.route("/webhook", methods=['POST','GET'])
def github_payload():
   org_name="adopt-it"
   signature = request.headers.get('X-Hub-Signature')
   data = request.data
   if verify_hmac_hash(data, signature):
      request_type=request.headers.get('X-GitHub-Event')
      payload = request.get_json()
      if "ping" in request_type:
         return jsonify({'msg': 'Ok'})
      elif "repository" in request_type:
         if "created" in payload["action"]:
            repository_name = payload["repository"]["full_name"]
            repository_owner = payload["sender"]["login"]
            if check_branch(repository_name,"master") != 200:
               create_file(repository_name,"README.md")
               message=str(restrict_permission(repository_name,'master'))
               create_issue(repository_name,"carlos-username")
               return jsonify({'msg': str("new repository "+repository_name+" with protection on master added "+message)})
            else:
               message=str(restrict_permission(repository_name,'master'))
               create_issue(repository_name,"carlos-username")
               return jsonify({'msg': str("new repository "+repository_name+" with protection on master added "+message)})
      else:
         return payload
         
   else:
      return jsonify({'msg': 'invalid hash'})


if __name__ == '__main__':
   app.run("0.0.0.0",argv[1])
