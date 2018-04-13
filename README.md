[![Build Status](https://travis-ci.org/rubensfig/PhastLoad.svg?branch=master)](https://travis-ci.org/rubensfig/PhastLoad)

testing 

```  
virtualenv .env -p python3
source .env/bin/activate
pip install -r requirements.txt
cd phastload
./manage.py runsslserver
```

And visit

``` https://localhost:8000/index ```

build the image

``` sudo docker build -t phast . ```

run the file

``` sudo docker-compose up -d ```

Access the Web page

``` localhost/index ```
