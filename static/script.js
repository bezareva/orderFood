
    //menu.html
    function funMin(itemId){
        let value = parseInt(document.getElementById(itemId).value)
        if (value > 0){
            value -= 1
        }
        document.getElementById(itemId).value = value
        updateOrder(itemId, value)
    }
    function funPlus(itemId){
        let value = parseInt(document.getElementById(itemId).value)
        if (value >= 0){
            value += 1
        }
        document.getElementById(itemId).value = value
        updateOrder(itemId, value)

    }

    function updateOrder(itemID, count) {
        let data = {
            "item_id": itemID,
            "count": count
        }
        fetch('/update_order', {
            method: 'PUT',
            body: JSON.stringify(data),
        })
            .then(response => {
            if (response.status === 200) {
                console.log("Added item");
        }})
            .catch(error => {
                console.error(error);
            });
    }