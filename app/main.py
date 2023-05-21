
import json
from fastapi import FastAPI, HTTPException
import uvicorn
import logging
import etcd3

from app.model.storage import ReqKVModel, ResKVModel
from app.core.config import settings

_log = logging.getLogger(__name__)
_log.setLevel(logging.DEBUG)

try:
    etcd = etcd3.client(host=settings.ETCD_HOST, port=settings.ETCD_PORT)
except KeyError:
    _log.fatal("ETCD_HOST or ETCD_PORT not configured!")
    exit(1)

app = FastAPI()

@app.get("/get_value_from_key", response_model=ResKVModel)
async def get_value_from_key(key: str):
    value, metadata = etcd.get(key)
    if not metadata:
        raise HTTPException(status_code=404, detail="Key not found")
    value = json.loads(value.decode('utf-8'))
    return ResKVModel(key=key, value=value)


@app.post("/add_key_and_value")
async def add_key_value_(
    req_model: ReqKVModel
):
    value = json.dumps(req_model.value)
    res = etcd.put(req_model.key, value)
    if not res:
        raise HTTPException(status_code=500, detail="Could not add value")
    return {"result": "Successfully added"}


@app.delete("/delete_key_value")
async def delete_key_and_value(key: str):
    _, metadata = etcd.get(key)
    if not metadata:
        raise HTTPException(status_code=404, detail="Key not found")
    is_deleted = etcd.delete(key)
    if not is_deleted:
        raise HTTPException(status_code=500, detail="Could not delete the key")

    return {"result": "Successfully Deleted"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=80,
        reload=True,
        log_level="INFO"
    )
