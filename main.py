import json
from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from db import DB

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def welcome(request: Request):
    categories = DB.get_categories()
    ctx = {
        "request": request,
        "categories": categories
    }
    return templates.TemplateResponse("index.html", ctx)

@app.get("/cart")
async def welcome(request: Request):
    categories = DB.get_categories()
    data = DB.get_menu()
    order = DB.get_current_order()
    a = list(order.keys())
    a = [int(x) for x in a]
    cart = []
    total = 0

    for item_list in data.values():
        for item in item_list:
            if item['id'] in a:
                item['count'] = order[str(item['id'])]
                cart.append(item)
                total += float(item['price']*item["count"])

    ctx = {
        "request": request,
        "categories": categories,
        "cart": cart,
        "total": total
    }
    return templates.TemplateResponse("cart.html", ctx)


@app.get("/menu/{category}")
async def list_category(request: Request, category: str):
    submenues = DB.get_items_by_category(category)
    categories = DB.get_categories()

    x = {
        "request": request,
        "submenues": submenues,
        "categories": categories
    }
    return templates.TemplateResponse("menu.html", x)


@app.put("/update_order")
async def update_order(request: Request):
    data = await request.json()
    item_id = data['item_id']
    count = data['count']

    order = DB.get_current_order()
    # Update order temp data
    order[item_id] = count
    if order[item_id] == 0:
        del order[item_id]
    DB.update_current_order(order)

    return {"OK": "ok"}

@app.delete("/clear_order")
async def clear_order(request: Request):
    order = DB.get_current_order()
    order = {}
    DB.update_current_order(order)
    return {"ok": "ok"}







