# GitHub API Challenge

Dockerized web service that listens for organization events to know when a repository has been created, for which the following actions are automated:
 - The protection of the master branch. 
 - Personal notification with an @mention in an issue within the repository outlining the protections that were added.

## Getting Started 🚀

First, some things you will need:

* A GitHub account
* An organization (you can create one for free)
* A github repository

Optional: 

* Since Ngrok creates a public url for your webservice (in this case the github webhook url), an optional Ngrok account (https://dashboard.ngrok.com/login) can be created in order that the public Ngrok url does not time out. 

### Prerequisites 📋

Because of the fact that the webservice will be launched as a microservice, it can be platform-independent as long as the following requirements are satisfied and installed onto the OS:
```
Docker-Compose (tested on version 3.7)
Docker (tested on version 18.09.0, build 4d60db4)
Github client (tested on version 2.18.0)
```
For reference, the webservice was tested under MacOS Mojave 10.14.5.

### Installing 🔧

First, ater cloning the repository, it is first required to get some useful data for using the webservice, including the following within your github account:
- A Bear token (**BEAR_TOKEN**) as well as a normal one (**ACCESS_TOKEN**) for authentication.
- Specifying a github secret (**GITHUB_SECRET**) you can create from your own.
- Choosing a ngrok port (**PANEL_PORT**), which the ngrok web panel will be accessible from.
- If you have created a Ngrok account, you can specify the (**NGROK_AUTH**) token, otherwise the public url will only last around 9 hours.

Moreover, after obtaining the tokens, one can indicate either a different property file or use the default one (.env_webservice), wherein the variables for the containarized webservice need to be added. 

```
$ cat .env_webservice
- ACCESS_TOKEN="Personal Access Token"
- BEAR_TOKEN="Oauth bear token"
- GITHUB_SECRET="Secret to authenticate with Github Webhook"
- APP_PORT=8080 (Webservice port, which the Ngrok will generate the public url for, no need to change)
- NGROK_AUTH="Optional Ngrok auth token"
- PANEL_PORT="Port under which Ngrok web panel will run"
```
or set your own one by exporting the variable FILE_NAME, whose format is "KEY=VALUE":

```
export FILE_NAME=".myPropertyFile"
```

Next, the docker compose file already specifies the out-of-the box instructions to generate two containers:
```
docker-compose up -d --build --force-recreate
```
- One with Ngrok to generate a publicly available link, which the github webhook will send events to. The url can be found on the Ngrok web panel, which has been launched into localhost:**PANEL_PORT** as per the property file.
- Another one with the python webhook receiving github webhook events and acting accordingly.

![alt text](https://github.com/adopt-it/Github_webhook/blob/api_challenge/media/screen_docker.png)

After accessing ngrok container via your browser by going to localhost:**APP_PORT** with the port you have indicated into the property file, the status tab will depict the webhook url to specify into your github account:
<img src="https://github.com/adopt-it/Github_webhook/blob/api_challenge/media/Ngrok_WebPanel.png" width="400" height="400">

Besides, I created the following:
* an organization called "**adopt-it**"
* and further on as part of the demo, a new repository called "**Git_test_repo**" is being added.

this url will have to be registered into your github account webhook section:
https://github.com/organizations/[:organizationname:]/settings/[:hooks:]

![Alt Text](https://github.com/adopt-it/Github_webhook/blob/api_challenge/media/Receiver_url_ngrok.gif)

Next, you can go ahead to create a new repository within your organization in order that the githook webservice starts listening to github events. 
Moreover, after creating a new github repository, the following actions are going to be carried out:
* Protection of the master branch belonging to the new repo
* A new issue will be opened stating which actions have been performed onto the repo and with a @mention to the user who launched it.
* E-mail will be sent from github to the user.

![Alt Text](https://github.com/adopt-it/Github_webhook/blob/api_challenge/media/Gif_master_protected.gif)

## Testing ⚙️
Testing master branch protection on the newly created git repository with one user within the organization adopt-it:
![Alt Text](https://github.com/adopt-it/Github_webhook/blob/api_challenge/media/Git_masterEnabledProtected.gif)

## Deployment 📦

These webservice can also be deployed for testing into multiple cloud platforms and/or OS, but not yet for production full usage. For instance:
* AWS (Amazon Web Services)
* Google Cloud Platform
* Digital Ocean
* Locally if needed
and the list goes on. 

Also, It is recommended to run it on a Unix-based OS.

## Built With 🛠️

* [Docker compose](http://www.dropwizard.io/1.0.2/docs/) - Tool for defining multi-container apps.
* [Python](https://www.python.org/) - Interpreted programming language.
* [Github API](https://developer.github.com/webhooks/#events) - GitHub API for the operations.
* [Flask web framework](https://flask.palletsprojects.com/en/1.0.x/) - Used to create the webservice in a more robust way.
* [Ngrok](https://ngrok.com/) - Used to generate public url's with embedded security for exposing web services, applications, etc.

## Authors ✒️

* **Carlos Klinsmann** - *First Version* 

## License 📄

This project is licensed under the GNU License 

## Acknowledgments 🎁

* Github API & valuable resources.
* Inspiration on the GithHub template: https://gist.githubusercontent.com/Villanuevand/6386899f70346d4580c723232524d35a/raw/8028158f59ba1995b0ca1afd3173bac3df539ca0/README-espa%25C3%25B1ol.md
* Flask documentation.
* References like https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3, https://github.com/PyGithub/PyGithub
