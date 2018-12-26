# Hurriyet Developers API with Python

## EN
 Unoffical Hurriyet API to give you access to ALL [Hurriyet API](https://developers.hurriyet.com.tr) features (list articles, list writers, single writers, search writer with name ex...) with [Your API KEY](https://developers.hurriyet.com.tr) Written in Python
 NOTE: If you want to usage to this API [sign up](https://developers.hurriyet.com.tr) before.

## TR
  Resmi olmayan Hurriyet API si size [Hurriyet API](https://developers.hurriyet.com.tr)' nin sunduğu herşeye Hurriyet API den aldığınız API KEY ile erişim sağlar. Python ile yazılmıştır
  NOT: Eğer API' yi kullanmak isterseniz önce [üye olun](https://developers.hurriyet.com.tr)

Example Usage:
  ```
  from hurriyetApi import HurriyetApi

  apikey = "APIKEY"
  api = HurriyetApi(apikey)
  writer = api.searchWriter("Adil")
  articles = api.listArticles(42, 3)

  print(writer)
  ```
