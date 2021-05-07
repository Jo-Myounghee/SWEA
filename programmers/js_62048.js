function solution(w, h) {
  var answer = 0;
  const [a, b] = [Math.min(w, h), Math.max(w, h)]
  for (let i=1; i<b; i++) {
      answer += Math.floor((a / b) * i)
  }
  return answer*2;
}