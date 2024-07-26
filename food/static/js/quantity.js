// General function to increment the quantity of an item
function incrementQuantity(itemId, type) {

    // Construct the ID based on the type
    const quantityInput = document.getElementById(`${type}-${itemId}`);
    if (quantityInput) {
        let currentValue = parseInt(quantityInput.value);
        if (!isNaN(currentValue) && currentValue < 999) {
            quantityInput.value = currentValue + 1;
        }
    }
}

// General function to decrement the quantity of an item
function decrementQuantity(itemId, type) {
    
    // Construct the ID based on the type
    const quantityInput = document.getElementById(`${type}-${itemId}`);
    if (quantityInput) {
        let currentValue = parseInt(quantityInput.value);
        if (!isNaN(currentValue) && currentValue > 1) {
            quantityInput.value = currentValue - 1;
        }
    }
}
