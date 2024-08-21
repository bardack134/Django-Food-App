// Function to increment the quantity of an item
function incrementQuantity(itemId) {

    // Get the input element by its ID
    const quantityInput = document.getElementById(`quantity-${itemId}`);

    // Parse the current value of the input
    let currentValue = parseInt(quantityInput.value);

    // If the value is a number and less than 999, increment the value
    if (!isNaN(currentValue) && currentValue < 999) {
        quantityInput.value = currentValue + 1;
    }
}


// Function to decrement the quantity of an item
function decrementQuantity(itemId) {

    // Get the input element by its ID
    const quantityInput = document.getElementById(`quantity-${itemId}`);

    // Parse the current value of the input
    let currentValue = parseInt(quantityInput.value);

    // If the value is a number and greater than 1, decrement the value
    if (!isNaN(currentValue) && currentValue > 1) {
        quantityInput.value = currentValue - 1;
    }
}

