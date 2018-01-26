from ..settings import CENTRAL_PORT

from app import app

from convert import schedule_main

from threading import Thread


def central_main():
    thread = Thread(target=schedule_main)
    thread.start()
    app.run(host='0.0.0.0', port=CENTRAL_PORT, debug=True)
    thread.join()
    print "Everything is finished."
