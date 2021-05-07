function solution(s) {
  var answer = s.length;
  
  if (s.length === 1) {
      return 1;
  }
  
  for (let i=1; i<s.length; i++) {
      let temp = ''
      let cnt = 1;
      let prev = s.slice(0, i)
      for (let j=i; j<s.length; j+=i) {
          var now
          if (j+i >= s.length) {
              now = s.slice(j, s.length)
          } else {
              now = s.slice(j, j+i)   
          }
          if (prev === now) {
              cnt ++;
          } else {
              if (cnt > 1) {
                  temp += `${cnt}${prev}`
              } else {
                  temp += prev
              }
              prev = now
              cnt = 1
          }
          if (temp.length >= answer) {
              break
          }
      }
      if (cnt > 1) {
          temp += `${cnt}${now}`
      } else {
          temp += now
      }
      if (temp.length < answer) {
          answer = temp.length
      }
  }
  return answer;
}