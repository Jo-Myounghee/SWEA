function solution(records) {
  var answer = [];
  let name = new Object()
  let temp = [];
  for (let i=0; i<records.length; i++) {
      let record = records[i].split(' ')
      let command = record[0]
      let uid = record[1]
      if (command === 'Enter') {
          name[uid] = record[2]
          temp.push(uid, 'enter')
      } else {
          if (command === 'Leave') {
              temp.push(uid, 'exit')
          } else {
              name[uid] = record[2]
          }
      }
  }
  for (let i=0; i<temp.length; i+=2) {
      let uid = temp[i]
      let command = temp[i+1]
      if (command === 'enter') {
          answer.push([name[uid], '님이 들어왔습니다.'].join(''))
      } else {
          answer.push([name[uid], '님이 나갔습니다.'].join(''))
      }
  }
  return answer;
}