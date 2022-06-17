FROM python

COPY ./producer/requirements.txt /producer/requirements.txt 

WORKDIR /producer

RUN pip install -r requirements.txt

COPY ./producer/ /producer

ENTRYPOINT [ "python" ]

CMD [ "producer.py" ]