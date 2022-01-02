import { useState } from "react";

function PageLotto() {
  const [lottoNum, setLottoNum] = useState([10, 11, 12, 13, 14, 15, 16, 17]);

  const makeLottoNumbers = () => {
    const lottoSet = new Set();
    while (lottoSet.size < 7) {
      lottoSet.add(Math.floor(Math.random() * 45) + 1);
    }
    const lottoList = Array.from(lottoSet);
    lottoList.sort((a, b) => a - b);
    return lottoList;
  };

  const handleClick = () => {
    setLottoNum(makeLottoNumbers());
  };

  return (
    <>
      <h2>Lotto</h2>
      <button onClick={handleClick}>예상</button>
      {lottoNum.map((number) => {
        return <div style={style}>{number}</div>;
      })}
    </>
  );
}
const style = {
  display: "inline-block",
  width: "100px",
  height: "100px",
  fontAlign: "center",
  fontSize: "2rem",
};

export default PageLotto;
