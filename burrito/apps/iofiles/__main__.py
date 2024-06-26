import uvicorn

from burrito.containers import get_current_app_name
from burrito.apps.iofiles.router import iofiles_router
from burrito.utils.config_reader import get_config
from burrito.utils.app_util import get_current_app, connect_app


_APP_NAME = get_current_app_name()

app = get_current_app(docs_url=f"/{_APP_NAME}/", openapi_url=f"/{_APP_NAME}/openapi.json")

if __name__ == "__main__":
    connect_app(app, f"/{_APP_NAME}", iofiles_router)

    uvicorn.run(
        f"burrito.apps.{_APP_NAME}.__main__:app",
        host="0.0.0.0",
        port=int(get_config().BURRITO_PORT),
        proxy_headers=bool(get_config().BURRITO_PROXY_HEADERS)
    )
