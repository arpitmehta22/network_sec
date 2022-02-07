const charNum_a = "a".charCodeAt(0);
const charNum_z = "z".charCodeAt(0);
const charNum_A = "A".charCodeAt(0);
const charNum_Z = "Z".charCodeAt(0);
const AtbashKeyMap = {};
for (let i = charNum_a, j = 0; i <= charNum_z; i++, j++) {
  AtbashKeyMap[String.fromCharCode(i)] = String.fromCharCode(charNum_z - j);
}
for (let i = charNum_A, j = 0; i <= charNum_Z; i++, j++) {
  AtbashKeyMap[String.fromCharCode(i)] = String.fromCharCode(charNum_Z - j);
}



const atBash = (text) => {
  if (typeof text != "string") return "";

  let result = "";

  for (let i = 0; i < text.length; i++) {
    if (text[i] in AtbashKeyMap) {
      result += AtbashKeyMap[text[i]];
    } else {
      result += text[i];
    }
  }
  return result;
};

export default atBash;
