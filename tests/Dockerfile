FROM python:3.9

WORKDIR /src
COPY ./src/ /src

RUN pip install -U requests pytest 
    
COPY wait-for-it.sh /
RUN chmod +x /wait-for-it.sh

# TODO: Update API Path to be an ENV/ARG in the Dockerfile
CMD ["/wait-for-it.sh" , "api:5000" , "--strict" , "--timeout=300" , "--" ,"pytest", "/src/"]