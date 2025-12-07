import pytest
from nonebug import App

from .fake import fake_group_message_event_v11


@pytest.mark.asyncio
async def test_matchers_registered(app: App):
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter

    from nonebot_plugin_mcserver_status import cmd_list, mcmotd

    # Ensure adapters are available and matchers are registered.
    adapter = nonebot.get_adapter(OnebotV11Adapter)
    assert adapter is not None

    # Fake event to assert matcher exists without hitting network.
    _ = fake_group_message_event_v11(message="查服 example.com")

    assert mcmotd is not None
    assert cmd_list is not None
