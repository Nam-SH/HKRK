function getCount(objects) {
  let ans = 0
  for (let i of objects) {
      if (i.x === i.y ) {
          ans ++
      }
  }
  return ans
}