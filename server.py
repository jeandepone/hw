from aiohttp import web
from aiohttp.web_response import json_response, Response
import asyncpg
import os
import json


async def get(request):
    async with request.app["pool"].acquire() as conn:
        values = list(await conn.fetch("SELECT data::json FROM table1"))
    return json_response({"values": [v for v, in values]})


async def post(request):
    data = json.loads(await request.read())
    async with request.app["pool"].acquire() as conn:
        await conn.execute("insert into table1(data) values ($1::json)", data)
    return Response()


async def delete(request):
    async with request.app["pool"].acquire() as conn:
        await conn.execute("delete from table1")
    return Response()


async def js(request):
    return web.FileResponse("./js/cpw.js")


async def app():
    app = web.Application()
    pool = await asyncpg.create_pool(
        os.environ.get("DATABASE_URL", "postgres://test:testpwd@localhost:5432/test")
    )
    async with pool.acquire() as conn:
        # await conn.execute("drop table if exists table1")
        await conn.execute("create table if not exists table1(id Serial, data jsonb)")
        await conn.set_type_codec(
            "json", encoder=json.dumps, decoder=json.loads, schema="pg_catalog"
        )
    app["pool"] = pool
    app.add_routes(
        [
            web.get("/coucou", get),
            web.get("/coucoudelete", delete),
            web.post("/", post),
            web.get("/", js),
        ]
    )
    return app


if __name__ == "__main__":
    web.run_app(app(), port=int(os.environ.get("PORT", 8888)))
