import { useState } from "react";

const makeLottoNumbers = () => {
  const numSet = new Set();
  while (numSet.size < 7) {
    let randomNum = Math.floor(Math.random() * 45) + 1;
    numSet.add(randomNum);
  }
  const numList = Array.from(numSet);
  numList.sort((a, b) => a - b);
  return numList;
};

function PageLotto() {
  const [value, setValue] = useState([10, 11, 12, 13, 14, 15, 16, 17]);

  const handleClick = () => setValue(makeLottoNumbers);

  return (
    <>
      <h2>Lotto</h2>
      <button onClick={handleClick}>예지</button>
      <div>
        {value.map((num) => {
          return <div style={style}>{num}</div>;
        })}
      </div>
    </>
  );
}

const style = {
  display: "inline-block",
  width: "100px",
  height: "100px",
  textAlign: "center",
  fontSize: "2rem",
  margin: "1rem",
};

export default PageLotto;
