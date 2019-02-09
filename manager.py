from multiprocessing import Process

from twitterStreamToDb import twitterStreamToDb
from hurriyetApiToDb import hurriyetApiToDb
import securityEventsWebPortal


if __name__ == '__main__':
    p = Process(target=twitterStreamToDb)

    p2 = Process(target=hurriyetApiToDb)    
    p.start()
    p2.start()

    p.join()
    p2.join()
