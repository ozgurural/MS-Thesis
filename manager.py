from multiprocessing import Process

from twitterStreamToDb import startTwitterStreamToDb
from hurriyetApiToDb import startHurriyetApiToDb
from ituNlpPipeline import startItuNlpApi
from securityEventsWebPortal import securityEventsWebPortalStart

if __name__ == '__main__':
    p1 = Process(target=startTwitterStreamToDb)

    p2 = Process(target=startHurriyetApiToDb)    

    p3 = Process(target=startItuNlpApi)  

    p4 = Process(target=securityEventsWebPortalStart)    


    p1.start()
    p2.start()
    p3.start()
    p4.start()


    p1.join()
    p2.join()
    p3.join()
    p4.join()
