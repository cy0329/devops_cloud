import { useState } from 'react';
import Ball from './Balls';

function LottoNum3() {
  // 0. 초기값 지정
  const [numList, setNumList] = useState([]);
  // 1. 랜덤 번호를 뽑아서 리스트화
  const lottoNumber3 = () => {
    let lottoSet = new Set();
    while (lottoSet.size < 7) {
      let num = Math.floor(Math.random() * 44) + 1;
      lottoSet.add(num);
    }
    let RNList = Array.from(lottoSet);
    RNList.sort((a, b) => a - b);
    return RNList;
  };
  // 2. 버튼 클릭시 실행문 구현
  const handleClick = () => {
    setNumList(lottoNumber3);
  };
  // 3. 보여질 페이지 구현
  return (
    <div>
      <button onClick={handleClick}>번호 뽑기!</button>
      <hr />
      {numList.map((number) => (
        <Ball number={number} />
      ))}
    </div>
  );
}

const style = {
  width: '100px',
  height: '100px',
  borderRadius: '50px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  margin: '1rem',
  userSelect: 'none',
};

export default LottoNum3;
