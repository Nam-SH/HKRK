function reverseString(s) {
  if (typeof s === "string") {
      const res = s.split('').reverse().join('')
      console.log(res)
  } else {
      console.log("s.split is not a function")
      console.log(s)
  }
}