import { useReducer } from 'react';

function lottoNum() {
  const numSet = new Set();
  while (numSet.size < 7) {
    const randomNum = Math.floor(Math.random() * 45) + 1;
    numSet.add(randomNum);
  }
  const numList = Array.from(numSet);
  return numList;
}

function reducer(prevState, action) {
  const { type } = action;
  if (type === 'GENERATE_NUMBERS') {
    return { ...prevState, numbers: lottoNum() };
  } else if (type === 'SHUFFLE_NUMBERS ') {
    return {
      ...prevState,
      numbers: prevState.numbers.sort(() => Math.random() - Math.random()),
    };
  } else if (type === 'SHUFFLE_COLORS ') {
    return {
      ...prevState,
      colors: prevState.colors.sort(() => Math.random() - Math.random()),
    };
  }
  return prevState;
}

function SevenNumbers() {
  const [state, dispatch] = useReducer(reducer, {
    numbers: [0, 0, 0, 0, 0, 0, 0],
    colors: [
      '#1B62BF',
      '#1755A6',
      '#37A647',
      '#F29F05',
      '#F23838',
      'purple',
      'pink',
    ],
  });

  const handleNum = () => {
    dispatch({ type: 'GENERATE_NUMBERS' });
  };
  const handleShuffle = () => {
    dispatch({ type: 'SHUFFLE_NUMBERS ' });
  };
  const handleColor = () => {
    dispatch({ type: 'SHUFFLE_COLORS ' });
  };

  return (
    <div>
      <h2>7개의 숫자</h2>
      {state.numbers.map((number, index) => (
        <div style={{ ...defaultStyle, backgroundColor: state.colors[index] }}>
          {number}
        </div>
      ))}
      <hr />
      <button onClick={handleNum}>숫자 뽑기</button>
      <button onClick={handleShuffle}>숫자 섞기</button>
      <button onClick={handleColor}>색깔 섞기</button>
    </div>
  );
}

const defaultStyle = {
  width: '100px',
  height: '100px',
  borderRadius: '50px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  userSelect: 'none',
};
export default SevenNumbers;
