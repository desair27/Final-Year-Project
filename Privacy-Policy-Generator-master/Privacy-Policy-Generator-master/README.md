# Privacy Policy Generator


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Python 3.8 or greater
2. pip

A full list of dependencies are in the [requirements.txt](requirements.txt) file.

### Installing

Install pipenv with:
```
pip install --user pipenv
```

Create a new pipenv virtual environment:
```
pipenv shell
```

When you are in the shell, install dependencies using:
```
pipenv install
```
If the dependencies have succesfully installed, run the server with:
```
python app/app.py
```
Visit the homepage at localhost:5000.

Once you are done using the input JSON generator, there will be json objects created from the generator that will look like this 
("dpv:hasPurpose": "x", "y", "z") when they should look like this ("dpv:hasPurpose": ["x, y, z"]). To see which of these objects 
Need square brackets around them make sure to download the input JSON skeleton and take a look at which JSON objects require
square brackets. This should be the last step taken in order to generate a usable JSON file for the privacy policy
generator.

If you want a general idea as to what the generated privacy policy is supposed to look like then download the sample JSON file
and upload it to the generator to render a sample privacy policy.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Acknowledgments

* W3Schools for the accordion.
* Harshvardhan Pandit and Dave Lewis for supervising this project.
