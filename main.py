from logging import debug
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

from pydantic.types import Json
import requests
import json
import re

description = """
# This is MAJHCC's  (Mohammed Aljahawri)   API helps you to do some cool stuffs.
<br>
[-] This API is still under development.<br>
[+] This API is working perfectly.<br>
[+] This API is Fast and Simple.<br>
[+] This API is Secure.<br>
[+] This API is Free.<br>
"""

app = FastAPI(title="MAJHCC's API", description=description, version="0.2.3")
from src.random_str import get_random_str

@app.get("/")
def read_root():
    return {"dev": "@majhcc", 
            "profiles": {
                "twitter": "https://twitter.com/majhcc",
                "github": "https://github.com/majhcc",
                "instagram": "https://instagram.com/majhcc",
                "website": "https://majhcc.pw"
            },
            "version": "0.2.0"  
            }
@app.get("/api/yt")
async def YouTube(url: str):
    """
    This can download videos from YouTube.<br>
    and it can also download audio from YouTube.<br>
    and it can also give you title and thumbnail of video from YouTube.<br>
    <pre>
    :param url: YouTube URL<br>
    :return: JSON <br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/yt?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ
    </code>


    """
    from src.youtube import download_youtube_video
    return download_youtube_video(url)

@app.get("/api/tk")
async def TikTok(url: str):
    """
    This can download videos from TikTok.<br>
    and it can also download audio from TikTok.<br>
    <pre>
    :param url: TikTok URL either video or audio<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/tk?url=https://vm.tiktok.com/Zzv6xq/
    </code>
    
    """
    from src.tiktok import getVideo
    json = getVideo(url)
    json['dev'] = "@majhcc"
    return json

@app.get("/api/twitter")
async def twitter(url: str):
    """
    This can download videos from Twitter.<br>
    <pre>
    :param url: Twitter video URL<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/twitter?url=https://twitter.com/majhcc/status/1234
    </code>
    """
    from src.twitter import download_twitter_video
    return download_twitter_video(url)
@app.get("/api/tw")
async def Twitter_v2(url: str):
    """
    This also can download videos from Twitter but it's faster than Twitter v1.<br>
    <pre>
    :param url: Twitter video URL<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/tw?url=https://twitter.com/majhcc/status/1234
    </code>
    """
    from src.tweet import get_url_download
    return get_url_download(url)
@app.get("/api/BTC")
async def btc():
    """
    This give you the current price of Bitcoin.<br>
    <pre>
    :return: RAW<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/BTC
    </code>
    """
    from API.BTC import get_btc_price
    return get_btc_price()

@app.get("/api/ETH")
async def eth():
    """
    This give you the current price of Ethereum.<br>
    <pre>
    :return: RAW<br>
    </pre>
    example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/ETH
    </code>
    """
    from API.ETH import get_eth_price
    return get_eth_price()
class postvht(BaseModel):
    url : str
    s : Optional[str] = get_random_str(5)
@app.post("/api/vht")
async def vht(data : postvht):
    """
    This can shorten your URL using v.ht servise.<br>
    <pre>
    :return: JSON<br>
    </pre>
    example:<br>
    <br>
    <code>
    import requests</br>
    data = '{"url": "http://127.0.0.1:8000/docs#/default/vht_api_vht_post", "s": "DOdqQ"}'</br>
    response = requests.post('https://server1.majhcc.xyz/api/vht', data=data)
    <code/>
    """
    if data.url == None:
        return {"error": "Please enter a URL"}
    from src.v_ht import short_url
    return short_url(data.url , data.s)

@app.get("/api/ip")
def ip(request: Request):
    """
    This returns your IP address.<br>
    <pre>
    :return: RAW<br>
    </pre>
    """
    client_host = request.client.host
    return {"ip": client_host}
@app.get("/api/fake-address")
def fake_address(request: Request):
    """
    This returns fake address.<br>
    <pre>
    :return: json<br>
    </pre>
    """
    from src.fake_add import fake_add
    return fake_add()

@app.get('/api/downloader/auto')
def downloader_auto(url: str):
    """
    This can download videos from YouTube, TikTok, Twitter, and other websites.<br>
    <pre>
    :param url: URL<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/downloader/auto?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ
    </code>
    """
    # regex youtube url
    if re.match(r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+', url):
        from src.youtube import download_youtube_video
        return download_youtube_video(url)
    # regex tiktok url
    elif re.match(r'(https?://)?(www\.)?(tiktok\.com|tiktok\.net)/.+', url):
        from src.tiktok import getVideo
        json = getVideo(url)
        json['dev'] = "@majhcc"
        return json
    # regex twitter url
    elif re.match(r'(https?://)?(www\.)?(twitter\.com|twitter\.net)/.+', url):
        from src.twitter import download_twitter_video
        return download_twitter_video(url)

@app.get('/api/caller-id')
def caller_id(request: Request, number: str, country_code: str):
    """
    This can get caller id from any country.<br>
    <pre>
    :param number: Number<br>
    :param country_code: Country Code<br>
    :return: JSON<br>
    </pre>
    Example:<br>
    <br>
    <code>
    https://server1.majhcc.xyz/api/caller-id?country_code=US&number=123456789
    </code>
    """
    from API.caller_id import get_names
    return get_names(number, country_code)

@app.get('/favicon.ico', include_in_schema=False)
def favicon():
    return FileResponse('static/favicon.ico')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8011)