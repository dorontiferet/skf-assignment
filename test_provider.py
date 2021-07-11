import pytest
from redis_provider import RedisProvider


@pytest.fixture
def redis_provider():
    return RedisProvider("redis", 6379)


def test_provider(redis_provider):
    redis_provider.publish("content1")
    message1 = redis_provider.get_last()
    assert message1["content"] == "content1"

    all_messages_with1 = redis_provider.get_by_time()

    redis_provider.publish("content2")
    message2 = redis_provider.get_last()
    assert message2["content"] == "content2"

    all_messages_with2 = redis_provider.get_by_time()

    assert message2["content"] == all_messages_with2[-1]["content"]

    assert len(all_messages_with2) == len(all_messages_with1) + 1

    assert len(redis_provider.get_by_time(message1["timestamp"], message2["timestamp"])) == 2
    assert len(redis_provider.get_by_time(message1["timestamp"], message1["timestamp"])) == 1
    assert len(redis_provider.get_by_time(message2["timestamp"], message2["timestamp"])) == 1
