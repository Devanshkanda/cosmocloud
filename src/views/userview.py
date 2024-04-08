from src.main import app

@app.get("/item/{item_idd}")
async def demo(item_idd):
    print("hello: ", item_idd)
    return {
        "success": "chal gaya fastapi",
        "id": item_idd
    }

# @app.get("/demo")
async def demo1():
    return {
        "success": "working",
        "Status": 200
    }