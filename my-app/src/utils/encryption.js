import atBash from "./atbashcode";

// Add additional enc algos here

// Add the name of the algo in the encAlgoNames array

// Define encrypt and decrypt function,
// for every name you add in the array.

const encAlgoNames = [
  "Atbash",
  // "New Enc Algorithm"
];

const encAlgos = {
  Atbash: {
    encrypt: (text) => atBash(text),
    decrypt: (text) => atBash(text),
  },
};

export { encAlgos, encAlgoNames };
