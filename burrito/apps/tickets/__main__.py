import uvicorn
from random import randint
from fastapi.routing import APIRoute

from burrito.utils.config_reader import get_config
from burrito.containers import prepare_app
from burrito.utils.app_util import get_current_app, connect_app


if prepare_app():
    from burrito.apps.tickets.router import tickets_router
else:
    print("App preparation failed")


app = get_current_app(docs_url="/tickets/docs", openapi_url="/tickets/openapi.json")
connect_app(app, "/tickets", tickets_router)


if __name__ == "__main__":
    uvicorn.run(
        "burrito.apps.tickets.__main__:app",
        host="0.0.0.0",
        port=int(get_config().BURRITO_PORT_TICKETS),
        proxy_headers=bool(get_config().BURRITO_PROXY_HEADERS)
    )
