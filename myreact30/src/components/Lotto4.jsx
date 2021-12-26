import { useState } from 'react';
import Ball from './Balls';

function LottoNum4() {
  // 0. 초기값 지정
  const [numList, setNumList] = useState([]);
  const [bonus, setBonus] = useState([]);
  // 1. 랜덤 번호를 뽑아서 리스트화
  const lottoNumber4 = () => {
    let lottoSet = new Set();
    while (lottoSet.size < 7) {
      let num = Math.floor(Math.random() * 45) + 1;
      lottoSet.add(num);
    }
    let RNList = Array.from(lottoSet);
    RNList.sort((a, b) => a - b);
    // let bonusNum = Math.floor(Math.random() * 45) + 1;
    // if (bonusNum in RNList) {
    //   bonusNum = Math.floor(Math.random() * 45) + 1;
    // }
    return RNList;
  };
  // Try1: 7개를 다 뽑고 그중 하나를 랜덤으로 보너스 번호로 지정
  // [i] 인자를 랜덤으로 Math.floor(Math.random() * 7) + 1;
  // Fail
  // Try2: 6개 뽑고 한 개를 그 함수 안에서 중복 없이 새로 뽑기.
  // const lottoNumber4의 밖에서 새로운 함수 지정해 하는 방식으로는 중복 문제 해결 못함

  // 2. 버튼 클릭시 실행문 구현
  const handleClick = () => {
    setNumList(lottoNumber4);
    // setBonus(lottoNumber4.bonusNum);
  };
  // 3. 보여질 페이지 구현
  return (
    <div>
      <button onClick={handleClick}>번호 뽑기!</button>
      <hr />
      {numList.map((number) => (
        <Ball number={number} />
      ))}
      <h3>보너스 번호</h3>
      {bonus.map((bonus) => (
        <Ball number={bonus} />
      ))}
    </div>
  );
}

export default LottoNum4;
