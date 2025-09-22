# Local LTI Consumer
This is a [LTI](https://www.imsglobal.org/activity/learning-tools-interoperability) consumer which can run 
on your local machine. It can be used to test LTI providers locally by writing testcases. 
It is based on [python3](https://www.python.org/) and [Django LTS 5.2](https://www.djangoproject.com/).
For older Django versions checkout corresponding tags. 

## Requirements
Please see requirements.txt

## Install and Run
At first download or clone this repository and install the requirements.

```
pip3 install -r requirements.txt
```

Now create a database:

```
python3 manage.py migrate
```

Finally run the server. It is important to specify a local port by replacing PORT. This port 
must be different from the port used for the LTI provider you want to test.

```
python3 manage.py runserver PORT
```

## Usage
Open [http://127.0.0.1:PORT](http://127.0.0.1:PORT) with your web browser and start by creating a testcase. 
After that you have to add some launch parameters and finally you can run the testcase.
