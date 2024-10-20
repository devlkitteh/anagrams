# anagrams
A small project to find anagrams of entered words


## Prerequisites:
- Must have docker installed
- Must have access to python:3.7-alpine image (via dockerhub or locally)

## Notes:
To use a custom dictionary file, name the file "dictionary.txt" and place it in the main project directory. **Ensure that your custom dictionary follows the format of the included example file**

## To run the program:

Navigate to the program's main directory:

`cd ~/path-to-project`


Build the Docker image with:

`docker image build -t anagrams:1.0.0 .`


Run the Docker image with:

`docker run -ti anagrams:1.0.0`