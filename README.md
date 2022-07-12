# Machine-Learning-Projects

### INEURON MACHINE LEARNING PROJECTS

### SOFTWARE REQUIREMENTS

1. [GITHUB]
2. [HEROKU ACCOUNT]
3. [VS CODE IDE]
4. [GIT CLI]

CREATING CONDA ENVIRONMENT

conda create -p venv python==3.7 -y

conda activate venv/

pip install -r requirements.txt

git add .

git status

git commit -m "message"

git push origin main

TO SETUP CI/CD PIPELINE IN HEROKU :-


BUILD DOCKER IMAGE

docker build -t <image name>:<tagname> .

docker images

docker run -p 5000:5000 -e PORT=5000 ab259eb9134c

TO CHECK RUNNING CONTAINER I DOCKER

docker ps

docker stop container id

python setup.py install

pip install ipykernel
