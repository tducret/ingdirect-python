FROM python:3

# L'image Docker peut être construite via :
# docker build -t ingdirect .

# Un container peut être instancié via :
# docker run -it --rm --name ing ingdirect

RUN pip3 install -U ingdirect

CMD [ "ing" ]