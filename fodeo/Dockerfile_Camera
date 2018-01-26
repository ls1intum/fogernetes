FROM ba-woebker-bruegge.in.tum.de:30500/victorhcm/opencv

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

CMD python fog_run.py camera -r --n 10