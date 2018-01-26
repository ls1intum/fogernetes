FROM ba-woebker-bruegge.in.tum.de:30500/victorhcm/opencv

RUN pip install --upgrade pip

EXPOSE 8089
EXPOSE 8090

COPY . .

RUN pip install -r requirements.txt

CMD python fog_run.py middleman