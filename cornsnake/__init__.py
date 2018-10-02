from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


def init_app():
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])
    return app


def create_app():
    import aiohttp_debugtoolbar

    app = init_app()
    aiohttp_debugtoolbar.setup(app)

    return app


def main():
    app = init_app()
    web.run_app(app)

if __name__ == '__main__':
    main()
