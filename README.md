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

Since the webservice will be launched as a microservice, it can be platform-independent as long as the following requirements are satisfied and installed onto the OS:
```
Docker-Compose
Docker
Github client
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

![alt text](https://github.com/adopt-it/Github_webhook/blob/api_challenge/screen_docker.png)

After, access ngrok container via your browser by going to localhost:**APP_PORT**, with the port you have indicated into the property file url to be used as the webhook listener for your github account:
![](https://github.com/adopt-it/Github_webhook/blob/api_challenge/Ngrok_WebPanel.png | width=100)

this url will have to be registered into your github account webhook section:
https://github.com/organizations/[:organizationname:]/settings/[:hooks:]


End with an example of getting some data out of the system or using it for a little demo

## Running the tests ⚙️

Explain how to run the automated tests for this system

### Break down into end to end tests ⌨️

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment 📦

Add additional notes about how to deploy this on a live system

## Built With 🛠️

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing 🖇️

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning 📌

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors ✒️

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments 🎁

* Hat tip to anyone whose code was used
* Inspiration
* etc
*https://gist.githubusercontent.com/Villanuevand/6386899f70346d4580c723232524d35a/raw/8028158f59ba1995b0ca1afd3173bac3df539ca0/README-espa%25C3%25B1ol.md
