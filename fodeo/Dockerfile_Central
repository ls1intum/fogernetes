FROM ba-woebker-bruegge.in.tum.de:30500/victorhcm/opencv

RUN apt-get update
RUN apt-get install software-properties-common -y

RUN add-apt-repository ppa:mc3man/trusty-media -y
RUN apt-get update
RUN apt-get install ffmpeg -y

RUN pip install --upgrade pip

EXPOSE 8080

COPY . .

RUN pip install -r requirements.txt

CMD python fog_run.py central