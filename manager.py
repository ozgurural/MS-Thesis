from multiprocessing import Process

from twitterStreamToDb import twitterStreamToDb
from hurriyetApiToDb import hurriyetApiToDb
import securityEventsWebPortal


if __name__ == '__main__':
    p1 = Process(target=twitterStreamToDb)

    p2 = Process(target=hurriyetApiToDb)    

    p3 = Process(target=securityEventsWebPortal.test)    

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
