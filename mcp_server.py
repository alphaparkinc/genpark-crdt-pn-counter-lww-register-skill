from client import PNCounter
import json

def handle_request(req):
    c = PNCounter(req.get("node_id", "local"))
    action = req.get("action")
    if action == "inc":
        c.inc(req.get("step", 1))
        return {"status": "ok", "value": c.value()}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "inc", "step": 10})))
