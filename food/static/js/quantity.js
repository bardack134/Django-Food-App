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

// Function to incrementand decrement the quantity of an drinks items
function incrementQuantity2(itemId) {

    const quantityInput = document.getElementById(`quantity2-${itemId}`);

    let currentValue = parseInt(quantityInput.value);

    if (!isNaN(currentValue) && currentValue < 999) {
        quantityInput.value = currentValue + 1;
    }
}


function decrementQuantity2(itemId) {

    const quantityInput = document.getElementById(`quantity2-${itemId}`);
    
    let currentValue = parseInt(quantityInput.value);
    
    if (!isNaN(currentValue) && currentValue > 1) {
        quantityInput.value = currentValue - 1;
    }
}

// Function to incrementand decrement the quantity of an deseert items
function incrementQuantity3(itemId) {

    const quantityInput = document.getElementById(`quantity3-${itemId}`);

    let currentValue = parseInt(quantityInput.value);

    if (!isNaN(currentValue) && currentValue < 999) {
        quantityInput.value = currentValue + 1;
    }
}


function decrementQuantity3(itemId) {

    const quantityInput = document.getElementById(`quantity3-${itemId}`);
    
    let currentValue = parseInt(quantityInput.value);
    
    if (!isNaN(currentValue) && currentValue > 1) {
        quantityInput.value = currentValue - 1;
    }
}

// Function to incrementand decrement the quantity of an Sides items
function incrementQuantity4(itemId) {

    const quantityInput = document.getElementById(`quantity4-${itemId}`);

    let currentValue = parseInt(quantityInput.value);

    if (!isNaN(currentValue) && currentValue < 999) {
        quantityInput.value = currentValue + 1;
    }
}


function decrementQuantity4(itemId) {

    const quantityInput = document.getElementById(`quantity4-${itemId}`);
    
    let currentValue = parseInt(quantityInput.value);
    
    if (!isNaN(currentValue) && currentValue > 1) {
        quantityInput.value = currentValue - 1;
    }
}
