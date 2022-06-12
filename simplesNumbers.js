console.time();

function checkPrime(number) {
    for (let digit = 2; digit <= number ** 0.5; digit++) {
        if (number % digit == 0) {
            return false;
        }
    }
    return true;
}

function quantityPrimeNumbers(primeQuantity) {
	let quantity = 0;
	let prime = 2;
	while(quantity != primeQuantity) {
		if(checkPrime(prime)) {
			console.log(prime);
			quantity++;
		} 
    prime++;
	}
}

quantityPrimeNumbers(process.argv[2]);
console.timeEnd();
