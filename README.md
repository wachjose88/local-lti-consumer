# Local LTI Consumer
This is a LTI consumer which can run on your local machine. It can be used to test LTI providers locally by writing testcases. It is based on python3 and django 1.11.

## Requirements
* certifi==2018.1.18
* chardet==3.0.4
* Django==1.11.9
* idna==2.6
* lti==0.9.2
* lxml==4.1.1
* oauthlib==2.0.6
* pytz==2017.3
* requests==2.18.4
* requests-oauthlib==0.8.0
* urllib3==1.22

## Install and Run
At first download or clone this repository and install the requirements.

```
pip3 install -r requirements.txt
```

Now create a database:

```
python3 manage.py migrate
```

Finally run the server. It is important to specify a local port by replacing PORT. This port must be differ from the port used for the LTI provider you want to test.

```
python3 manage.py runserver PORT
```

## Usage
Open http://127.0.0.1:PORT with your web browser and start by creating a testcase. After that you have to add some launch parameters and finally you can run the testcase.
