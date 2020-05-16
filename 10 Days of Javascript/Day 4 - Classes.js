class Polygon {
  constructor(arr) {
      this.arr = arr
  }
  
  perimeter() {
      const res = this.arr.reduce(function (accumulator, currentValue) { return accumulator + currentValue})
      return res
  }
}