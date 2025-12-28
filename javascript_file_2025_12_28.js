You can use the following JavaScript code to display a random fun fact in the console:

```javascript
// Array of fun facts
const funFacts = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
    "Bananas are berries, but strawberries are not.",
    "A group of flamingos is called a 'flamboyance'.",
    "Octopuses have three hearts.",
    "Wombat poop is cube-shaped.",
    "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
    "The longest wedding veil was longer than 63 football fields.",
    "Some cats are allergic to humans.",
    "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
    "Scotland's national animal is the unicorn."
];

// Function to display a random fun fact
function displayRandomFunFact() {
    const randomIndex = Math.floor(Math.random() * funFacts.length);
    console.log(funFacts[randomIndex]);
}

// Call the function to display a random fun fact
displayRandomFunFact();
```

### How It Works:
1. An array `funFacts` is created, consisting of various interesting facts.
2. The function `displayRandomFunFact` is defined to randomly select a fact from the array.
3. It generates a random index using `Math.random()` and `Math.floor()`, then logs the selected fun fact to the console.
4. Finally, the function is called to display a random fun fact.

You can run this code in a JavaScript environment (like a web browser console or Node.js) to see the result. Each time you run the script, it will display a different fact.