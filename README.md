# Sinel Hospital
This repository is where we (Analytica) develop the Sinel Hospital web application.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install - the software and how to install them.

```
Python 3.8+
Pip
```

### Installing

A step by step series on how to get a development env running.

#### Clone this repository and open it your prefered editor. e.g. VS Code.
```bash
git clone https://github.com/DCIT-208-ANALYTICA/sinel_web.git
cd sinel_web
pip install -r requirements.txt
```

#### Setting up the database.
```bash
python manage.py makemigrations dashboard website
python manage.py migrate
```

#### Running in the development mode.
```bash
python manage.py runserver
```