# GitHub API Challenge

Dockerized web service that listens for organization events to know when a repository has been created, for which the following actions are automated:
 - The protection of the master branch. 
 - Personal notification with an @mention in an issue within the repository outlining the protections that were added.

## Getting Started 🚀

First, some things you will need:

* A GitHub account
* An organization (you can create one for free)
* A repository

### Prerequisites 📋

Since the webservice will be launched as a microservice, it will be platform-independent as long as the following requirements are satisfied and installed onto the OS:
```
> * OS:
>   * Mac OS (the webservice was developed into MacOS Mojave 10.14.5)
>   * GNU/Linux or any Unix-based supporting docker
Docker-Compose
Docker
Github client
```

### Installing 🔧

First, ater cloning the repository, it is first required to get some useful data for using the webservice, including the following within your github account:
- A Bear token (**BEAR_TOKEN**) as well as a normal one (**ACCESS_TOKEN**) for authentication.
- Specifying a github secret (**GITHUB_SECRET**) you can create from your own.
- Choosing an application port (**APP_PORT**), which the containers are going to utilize and be attached to.
Moreover, after obtaining the tokens, the .env properties' file ought to be modified, wherein the variables are to be added. 

```
- ACCESS_TOKEN="Personal Access Token"
- BEAR_TOKEN="Oauth bear token"
- GITHUB_SECRET="Secret to authenticate with Github Webhook"
- APP_PORT=8080 
```

After editting the file, you can source it, to store the variables for docker-compose to use them. Make sure you are located in the repository root location.

```
source .env
```

Next, the docker compose file already specifies the out-of-the box instructions to generate two containers:
```
docker-compose up -d --build --force-recreate
```
- One with Ngrok to generate a publicly available link, which the github webhook will send events to. This will be attached to the **APP_PORT** var specified in the .env file.
- Another one with the python webhook receiving github webhook events and acting accordingly.

![alt text](https://github.com/adopt-it/Github_webhook/blob/api_challenge/screen_docker.png)

After, access ngrok container via your browser by going to localhost:**APP_PORT**, with the port you have indicated into the properties .env file to obtain the webservice url to be the webhook listener for your github account:
![alt text](https://github.com/adopt-it/Github_webhook/blob/api_challenge/Ngrok_img.png)

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
* https://gist.githubusercontent.com/Villanuevand/6386899f70346d4580c723232524d35a/raw/8028158f59ba1995b0ca1afd3173bac3df539ca0/README-espa%25C3%25B1ol.md
