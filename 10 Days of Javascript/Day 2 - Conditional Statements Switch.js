function getLetter(s) {
  let letter;
  const head = s[0]

  switch (head){
      case ("a" || "e" || "i" || "o" || "u"):
          letter = 'A'
          break
      case ("b" || "c" || "d" || "f" || "g"):
          letter = 'B'
          break
      case ("h" || "j" || "k" || "l" || "m"):
          letter = 'C'
          break
      default:
          letter = 'D'
  }
  return letter
}