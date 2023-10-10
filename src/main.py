# This is a sample Python script.
from dataclasses import dataclass
from typing import Optional, Any

from aiohttp import web

import exc_handler
import route
import serializer
from handlers import *

if __name__ == '__main__':
    app = web.Application(middlewares=[])

    api_app = web.Application(middlewares=[serializer.serializer, exc_handler.exc_handler])
    api_app.router.add_routes(routes)
    app.add_subapp('/api/v1/', api_app)
    web.run_app(app, port=8081)
