import { useState } from 'react';

function LottoNum2({ color }) {
  const [numList, setNumList] = useState([]);
  // 1. 랜덤 번호를 뽑아서 리스트화
  const lottoNumber2 = () => {
    let lottoList = [];

    let i = 0;

    while (i < 6) {
      let num = Math.floor(Math.random() * 44) + 1;
      if (!sameNum(num)) {
        lottoList.push(num);
        i++;
      }
    }

    function sameNum(num) {
      for (let j = 0; j < lottoList.length; j++) {
        if (num === lottoList[j]) {
          return true;
        }
      }
      return false;
    }
    lottoList.sort((a, b) => a - b);
    return lottoList;
  };

  const handleClick = () => {
    setNumList(lottoNumber2);
  };
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

export default LottoNum2;
