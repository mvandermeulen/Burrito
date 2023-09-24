from pydantic import BaseModel

from burrito.models.m_notifications_model import Notifications, CommentUpdate


class WebSocketMessage(BaseModel):
    type_: str
    data: Notifications | CommentUpdate
