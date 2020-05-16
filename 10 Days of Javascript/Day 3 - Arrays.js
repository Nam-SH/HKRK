function getSecondLargest(nums) {
  // Complete the function
  nums.sort(function(a, b) { 
              if ( b > a ) return 1 
              else if (b < a) return -1})
  
  const result = nums.find(num => num != nums[0]);

  return result
}   