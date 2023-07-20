FROM python
ENV BOT_NAME=$BOT_NAME

WORKDIR /home/fugguri/Документы/

COPY requirements.txt /home/fugguri/Документы/
RUN pip install -r /home/fugguri/Документы/requirements.txt && python mayn.py

