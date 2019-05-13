import requests
import json
import time
import sched

class HurriyetApi:

    _URI = "https://api.hurriyet.com.tr/v1"
    s = sched.scheduler(time.time, time.sleep)

    def __init__(self, apikey):
        self.apikey = apikey
        self.apikeys = { 'apikey': apikey }
        self.lastJson = None
        self.findList = []

            ########## Search Methods ##########
    def search(self, keyword, total=None, skip=None, old=None):
        # if old is 1 old to new, -1 new to old
        if keyword is not None:
            return self.sender('/search/{}'.format(keyword), total, skip)
        else:
            return "Keyword args is required!"

    def searchPath(self, name):
        if name:
            self.listPaths(select = 'Path,Id')
            self.searchEngine(name)

            if self.findList:
                return self.findList
            else:
                return "Your path name was not finded!"
        else:
            return "Name args is required!"

    def searchWriter(self, name):
        if name:
            self.s.enter(0,1, self.listWriters, kwargs={'select': 'Fullname, Id'})
            self.s.enter(0,2, self.searchEngine, argument=(name,))
            self.s.enter(0,3, self.listColumns, kwargs={'select': 'Fullname,WriterId'})
            self.s.enter(0,4, self.searchEngine, argument=(name,))
            self.s.run()
            """
            self.listWriters(select = 'Fullname,Id')
            self.searchEngine(name)
            self.listColumns(select = "Fullname, WriterId")
            self.searchEngine(name)
            """
            if self.findList:
                return self.findList
            else:
                return "Writer not found!"
        else:
            return "Name args is required!"

    def searchEngine(self, name):
        for item in self.lastJson:
            if name in str(item.values()):
                self.findList.append(item)

            ########## END Search Methods ##########

            ########## List Methods ##########
    def listArticles(self, total=None, skip=None):
        return self.sender('/articles/', total, skip)

    def listPhotos(self, total=None, skip=None):
        return self.sender('/newsphotogalleries/', total, skip)

    def listVideos(self, total=None, skip=None):
        return self.sender('/newsvideos/', total, skip)

    def listPages(self, total=None, skip=None):
        return self.sender('/pages/', total, skip)

    def listPaths(self, total=None, skip=None, select=None):
        return self.sender('/paths/', total, skip, select)

    def listColumns(self, total=None, skip=None, select=None):
        return self.sender('/columns/', total, skip)

    def listWriters(self, total=None, skip=None, select=None):
        return self.sender('/writers/', total, skip, select)
            ########## END List Methods ##########

            ########## Single Methods ##########
    def singlePhoto(self, id):
        return self.sender('/newsphotogalleries/{}'.format(id))

    def singleArticle(self, id):
        return self.sender('/articles/{}'.format(id))

    def singleVideo(self, id):
        return self.sender('/newsvideos/{}'.format(id))

    def singlePages(self, id):
        return self.sender('/pages/{}'.format(id))

    def singleColumn(self, id):
        return self.sender('/columns/{}'.format(id))

    def singleWriter(self, id):
        return self.sender('/writers/{}'.format(id))
            ########## END Single Methods ##########

    def sender(self, endpoint, total=10, skip=None, select=-1):
        params = {'apikey': self.apikey, '$select': select, '$top': total, '$skip': skip }
        return self.SendRequest(endpoint, params=params)

    def SendRequest(self, endpoint, params=None):
        while True:
            try:
                if params is not None:
                    r = requests.get(self._URI + endpoint, params)
                else:
                    return "Parameter not entered"
                break
            except Exception as e:
                print("Except on SendRequest (Wait 5 second and resend):", + str(e))
                time.sleep(5)

        if r.status_code == 200:
            self.lastJson = json.loads(r.text)
            return self.lastJson
        else:
            return "Request return " + str(r.status_code) + " error!"
