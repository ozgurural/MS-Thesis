from multiprocessing import Process

from twitterStreamToDb import twitterStreamToDb
from hurriyetApiToDb import hurriyetApiToDb
from securityEventsWebPortal import securityEventsWebPortal


if __name__ == '__main__':
    p = Process(target=twitterStreamToDb)

    p2 = Process(target=hurriyetApiToDb)    

    p3 = Process(target=securityEventsWebPortal)    

    p.start()
    p2.start()
    p3.start()

    p.join()
    p2.join()
    p3.join()
