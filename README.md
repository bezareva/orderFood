# orderFood
Food ordering app using FastAPI (REST + Jinja templates) and JSON as DB.

Website enables user to go through the different menu
pages, add items to the cart and create order/receipt.

### API
- `GET /` returns available food categories (template response)
- `GET /cart` returns current order information (template response)
- `GET /menu/{category}` returns items for chosen category (template response)
- `PUT /update_order` async update of the current order 
- `DELETE /clear_order` async call used to cancel (and confirm) order

### Sreenshots
Home page:
![home.png](https://raw.githubusercontent.com/bezareva/static/master/orderFood_images/home.png)

Menu selection:
![menu.png](https://raw.githubusercontent.com/bezareva/static/master/orderFood_images/menu.png)

Order:
![order.png](https://raw.githubusercontent.com/bezareva/static/master/orderFood_images/order.png)