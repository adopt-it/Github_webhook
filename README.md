# GitHub API Challenge

Dockerized web service that listens for organization events to know when a repository has been created, for which the following actions are automated:
 - The protection of the master branch. 
 - Personal notification with an @mention in an issue within the repository outlining the protections that were added.

## Getting Started 🚀

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites 📋

```
Docker-Compose:
Docker
Github client
```

### Installing 🔧

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
For using the webservice, it is required to first generate a Bear token as well as a normal one for interacting with git API and git operations. Moreover, after obtaining the tokens, the .env file ought to be modified to add the required information:
> - ACCESS_TOKEN="Personal Access Token"
> - BEAR_TOKEN="Oauth bear token"
> - GITHUB_SECRET="Secret to authenticate with Github Webhook"
> - APP_PORT=8080

```

And repeat

```
until finished
```

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
