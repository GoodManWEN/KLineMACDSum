from .baostockwrap import wrapmain
from aiohttp import web
#from aiohttp_debugmode import Debugmode as debug
from concurrent.futures import ThreadPoolExecutor
from aiohttp_basicauth import BasicAuthMiddleware
import aiohttp_jinja2
import jinja2
import asyncio
import os

########################################
auth_username = 'admin'
auth_password = 'password'
########################################
thread_pool = ThreadPoolExecutor()
routes = web.RouteTableDef()
workingpath = os.path.dirname(os.path.abspath(__file__))
auth = BasicAuthMiddleware(username=auth_username, password=auth_password)
app = web.Application(middlewares=[auth])
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(os.path.join(workingpath ,'templates')))

@aiohttp_jinja2.template('index.html')
def indexhandler(request):
    return {}

@routes.get('/')
async def hello(request):
    ret = await indexhandler(request)
    return ret

@routes.post('/macdapi')
async def macdapi(request):
    try:
        if request.body_exists:
            data = await request.json()
        else:
            raise Exception()
        paramset = ['stocknum',
                    'radio',
                    'sttime',
                    'edtime',
                    'stdate',
                    'eddate'
                    ]
        paramset = set(paramset)
        assert paramset == set(data.keys())
        stocknum , radio , sttime , edtime , stdate , eddate = data.values()
        for s in data.values():
            assert type(s) is str

        # logic
        loop = asyncio.get_running_loop()
        three = await wrapmain(loop , thread_pool ,stocknum , radio , sttime , edtime , stdate , eddate)
        assert three
        return web.json_response(
            {   'success': 1 , 
                'data' : {
                    "red":three[0],
                    "green":three[1],
                    "sum":three[2],
                }
            }
        )

    except Exception as e:
        return web.json_response({'success': 0 , 'msg':f"{type(e).__name__}:{str(e)}" })


app.add_routes(routes)
app.add_routes([web.static('/', os.path.join(workingpath ,'static'))])