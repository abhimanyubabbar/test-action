from md5 import get_md5


def transformEvent(event, metadata):
    hash = get_md5(event["event"])
    event["event_md5"] = f"{hash}"
    return event
