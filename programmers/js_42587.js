function solution(priorities, location) {
  var answer = 0;
  let queue = [];
  
  for (let i=0; i<priorities.length; i++) {
      queue.push(i+10);
  }
  while (queue.length > 0) {
      let now = priorities[0]
      let max_val = Math.max(...priorities)
      if (now >= max_val) {
          priorities.shift();
          answer++;
          if (queue[0] === (location+10)) {
              return answer
          } else {
              queue.shift();
          }
      } else {
          priorities.push(priorities.shift());
          queue.push(queue.shift());
      }
  }
  
  return answer;
}