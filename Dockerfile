FROM python:3

# L'image Docker peut être construite via :
# docker build -t ingdirect .

RUN pip3 install -U ingdirect

CMD [ "ing" ]