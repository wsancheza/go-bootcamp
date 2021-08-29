from fastapi import APIRouter
import requests
from conf.conf import OPENWEATHERMAP_API_KEY, url


greeting = APIRouter()
wheather = APIRouter()

@greeting.get('/greeting')
def helloWorld():
    return "Hello, World"


@wheather.get('/wheather/{city}')
def getWheatherCity(city: str):
    req = url.format(city, OPENWEATHERMAP_API_KEY)
    res = requests.get(req)
    return res.json()