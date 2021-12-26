import { useState } from 'react';
import Ball from './Balls';

function LottoNum4() {
  // 0. 초기값 지정
  const [numList, setNumList] = useState([]);
  const [bonus, setBonus] = useState([]);
  // 1. 랜덤 번호를 뽑아서 리스트화
  const lottoNumber4 = () => {
    let lottoSet = new Set();
    while (lottoSet.size < 6) {
      let num = Math.floor(Math.random() * 45) + 1;
      lottoSet.add(num);
    }
    let RNList = Array.from(lottoSet);
    RNList.sort((a, b) => a - b);
    return RNList;
  };
  const bonusNum = () => {
    let bonus = Math.floor(Math.random() * 45) + 1;
    let bonusList = new Array();
    if (bonus in lottoNumber4) {
      let bonus = Math.floor(Math.random() * 45) + 1;
    } else {
      bonusList.push(bonus);
    }
    return bonusList;
  };

  // 2. 버튼 클릭시 실행문 구현
  const handleClick = () => {
    setNumList(lottoNumber4);
    setBonus(bonusNum);
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
