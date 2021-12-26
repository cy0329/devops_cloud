import { useState } from 'react';

function LottoNum({ color }) {
  // 0. 초기값 지정
  const [numList, setNumList] = useState([]);
  // 1. 랜덤 번호를 뽑아서 리스트화
  const lottoNumber = () => {
    let LNList = [];

    for (let i = 0; i < 7; i++) {
      let randomNum = Math.floor(Math.random() * 44) + 1;

      for (const j in LNList) {
        if (randomNum == LNList[j]) {
          randomNum = Math.floor(Math.random() * 44) + 1;
        }
      }
      LNList.push(randomNum);
    }
    LNList.sort((a, b) => a - b);
    return LNList;
  };

  // 2. 버튼 클릭시 실행문 구현
  const handleClick = () => {
    setNumList(lottoNumber);
  };

  // 3. 보여질 페이지 구현
  return (
    <div>
      <button onClick={handleClick}>번호 뽑기!</button>
      <hr />
      {numList.map((number) => (
        <div style={{ ...style, backgroundColor: color }}>{number}</div>
      ))}
    </div>
  );
}

export default LottoNum;
