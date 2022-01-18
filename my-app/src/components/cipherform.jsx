import React from 'react'
import Button from "react-bootstrap/Button";
import { useState } from 'react'
import { encAlgoNames, encAlgos } from "../utils/encryption";

function Cipherform() {
  const [text, setText] = useState("");
  const [result, setresult] = useState("");
  const encryptionUsed = "Atbash";

  const EncipherHandler = () => {
    let encFunction = (t) => t;
    if (encryptionUsed in encAlgos) {
      if ("encrypt" in encAlgos[encryptionUsed]) {
        encFunction = encAlgos[encryptionUsed].encrypt;
      }
    }
    setresult(encFunction(text));
  }
  const DecipherHandler = () => {
let decFunction = (t) => t;
if (encryptionUsed in encAlgos) {
  if ("decrypt" in encAlgos[encryptionUsed]) {
    decFunction = encAlgos[encryptionUsed].decrypt;
  }
}
    setresult(decFunction(text));
  };

    
    return (
      <div>
        <hr />
        <p>
          To Encipher and Decipher any string please enter below press
          respective buttons !
        </p>
        <div>
          <input type="text" onChange={(e) => setText(e.target.value)}></input>
          <Button variant="primary" onClick={EncipherHandler}>
            {" "}
            Encipher
          </Button>
          <Button variant="secondary" onClick={DecipherHandler}>
            {" "}
            Decipher
          </Button>
        </div>
        <hr />
        <h4>Result : </h4>
        <p>{result.length !=0 ? result : "Nothing Done yet "}</p>
      </div>
    );
}

export default Cipherform
