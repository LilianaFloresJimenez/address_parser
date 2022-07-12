# Address parser
This project deal only with some specific concatenated street names and numbers. 

## General
- Using regular expressions.
- Not scaling well. It could be a wrong choice later but for now it is working
- Not so easy to maintain.
- Code can be run only by test at the moment.

## Environment
- docker > 20.10.14(This version was tested)
- docker-compose > 1.25.0

## How to run the test
```shell
# In project directory
make test
```
