# Code Samurai 2024 - Preliminary Round

## Team Information
Team Name: Team ParmunaLastTime \
University: Ahsanullah University of Science and Technology \
Team Members: \
    1. Muhammad Hossain (hussain0613@gmail.com) \
    2. Rakib Hasan Bappy (rakibhasan15144@gmail.com) \
    3. Fahmidur Rahman (fahmidurrahman07@gmail.com)

## Running the project

### Commands to run the project in a docker container:
```bash
# build the docker image
docker build --tag=sol:latest .

# run the docker container

# interactive mode
docker run -it --rm --name sol sol:latest
# or interactive mode with port forwarding
docker run -it -p 5000:5000 --rm --name=sol sol:latest
# or detached mode with port forwarding
docker run -d -p 5000:5000 --rm --name=sol sol:latest
# or detached mode with random port forwarding
docker run -d -P --rm --name=sol sol:latest
```

### Commands to run the project in a local environment:
```bash
# create a virtual environment
python -m venv .venv
# install the dependencies
pip install -r requirements.txt
# initialize the database
python init_db.py

# run the application
python main.py
```
Might need replace `python` with `python3` or `py` depending on the system.
