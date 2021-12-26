// 3항 연산자를 응용해서 볼 색깔 지정해보려 했는데
// 왜 안되는 걸까?

import { useState } from 'react';
// import Ball from './Balls';

function LottoNum4() {
  // 0. 초기값 지정
  const [numList, setNumList] = useState([]);
  const [color, setColor] = useState('white');
  // 1. 랜덤 번호를 뽑아서 리스트화
  const lottoNumber4 = () => {
    let lottoSet = new Set();
    while (lottoSet.size < 7) {
      let num = Math.floor(Math.random() * 45) + 1;
      lottoSet.add(num);
    }
    let RNList = Array.from(lottoSet);
    RNList.sort((a, b) => a - b);
    return RNList;
  };
  // 2. 버튼 클릭시 실행문 구현
  const handleClick = () => {
    setNumList(lottoNumber4);
  };

  const LottoBall = ({ number }) => {
    setColor(
      number <= 10
        ? 'red'
        : number <= 20
        ? 'orange'
        : number <= 30
        ? 'yellow'
        : number < 40
        ? 'green'
        : 'blue',
    );

    return (
      <div className="ball" style={{ ...style, backgroundColor: color }}>
        {number}
      </div>
    );
  };
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
  // 3. 보여질 페이지 구현
  return (
    <div>
      <button onClick={handleClick}>번호 뽑기!</button>
      <hr />
      {numList.map((number) => (
        <LottoBall number={number} />
      ))}
    </div>
  );
}

export default LottoNum4;

// {numList.map((number) => (
//     <div style={{ ...style, backgroundColor: color }}>{number}</div>
//   ))}
