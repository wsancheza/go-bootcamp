# go-bootcamp
Repository for Go Bootcamp application at Wizeline Academy

API implemented using FastAPI (https://fastapi.tiangolo.com/) and tested using pytest

API has two endpoints:
1. /greeting : Only for healt check, it response with "Hello, World"
2. /wheather/{city} : Fetch from open weather API (https://openweathermap.org/) for City {city}

Tests
Due to responses are dinamic depending on hour run, check only static information for City, such as type, id, and country.

It just needs execute command pytest. 
