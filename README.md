
# RPN calculator

  
RPN is a simple calculator, I have used my own repository as a boilerplate https://github.com/workflows-guru/hexagonal-architecture

Notes: No AI generated content or Code has been used in this repository

Time elapsed: 2h-3h 

The app allow user to:

- Get a stack by ID
- Delete a stack by ID
- Add a value to the stack
- Apply an operator (+,-,*,/)
  

## Run the application

To run the application, create a virtual env and install the required dependencies as follow:

```
python -m venv venv
pip install fastapi[standard]
```
and run the application using

```
fastapi dev
```

This will expose the openapi doc in http://127.0.0.1:8000/docs

You will see the following swagger: Notes that I have changed the "apply operand" endpoint

![Alt text](/screenshots/rpn.png?raw=true "RPN swagger")


## Tests

You can test manually using the following calls (The local storage already contains a stack with id "test")

```
POST /rpn/stack/test
{
  "value": 1
}

POST /rpn/stack/test
{
  "value": 4
}

POST /rpn/stack/test
{
  "value": 5
}


POST /rpn/stack/test/operator

{
  "value": "+"
}

this will return the following stack

{
	"stack_id": "test",
	"content": [1, 9]
}
```

to run automated tests 

```
pytest
```