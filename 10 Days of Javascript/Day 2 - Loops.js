function vowelsAndConsonants(s) {

  for (let i of s) {
      if ('aeiou'.includes(i))
          console.log(i)
  }
  for (let i of s) {
      if (!'aeiou'.includes(i))
          console.log(i)
  }
}