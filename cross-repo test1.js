function SquareRoot() {
    const number1 = 2.25;
    const number2 = -4;
    const number3 = 'hello';

    const result1 = Math.sqrt(number1);
    const result2 = Math.sqrt(number2);
    const result3 = Math.sqrt(number3);

    console.log(`The square root of ${number1} is ${result1}`);
    console.log(`The square root of ${number2} is ${result2}`);
    console.log(`The square root of ${number3} is ${result3}`);
}

function RandomNumxxxxxxber123() {
    // generating  a random number
    const a = Math.random();
    console.log(a);
}

function PrimeNumbers() {
    // program to print prime numbers between the two numbers

// take input from the user
    const lowerNumber = parseInt(prompt('Enter lower number: '));
    const higherNumber = parseInt(prompt('Enter higher number: '));

    console.log(`The prime numbers between ${lowerNumber} and ${higherNumber} are:`);

// looping from lowerNumber to higherNumber
    for (let i = lowerNumber; i <= higherNumber; i++) {
        let flag = 0;

        // looping through 2 to user input number
        for (let j = 2; j < i; j++) {
            if (i % j == 0) {
                flag = 1;
                break;
            }
        }

        // if number greater than 1 and not divisible by other numbers
        if (i > 1 && flag == 0) {
            console.log(i);
        }
    }
}
