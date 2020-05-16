function getMaxLessThanK(n, k) {
  let ans = 0
  for (let i = 1;i <= n; i++) {
      for (let j = i + 1; j <= n;j++) {
          let val = (i & j)
          if (val < k) ans = Math.max(ans, val)
      }
  }
  return ans
}
