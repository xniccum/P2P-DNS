import json

def json_to_bytes(js):
    return json.dumps(js).encode('utf-8')
def bytes_to_json(bts):
    return json.loads(bts.decode('utf-8'))