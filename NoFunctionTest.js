while (true) {
    let input = prompt("Enter a positive number (or a negative number to exit):");
    let num = parseFloat(input);

    if (isNaN(num)) {
        console.log("Invalid input. Please enter a valid number.");
        continue;
    }

    if (num < 0) {
        console.log("Exiting program.");
        break;
    }

    if (num === 0) {
        console.log("Please enter a number greater than zero.");
        continue;
    }

    let randomNum = Math.random() * num;
    console.log(`Random number between 0 and ${num}: ${randomNum}`);
}
