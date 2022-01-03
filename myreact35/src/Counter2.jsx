import { useState } from 'react';

function reducer(action, prevState) {
  const { type, amount } = action;
  if (type === 'PLUS') {
    return prevState + amount;
  } else if (type === 'MINUS') {
    return prevState - amount;
  }
  return prevState;
}

function reducer2(action, color) {
  const { type, amount } = action;
  if (type === 'CHANGE_COLOR') {
    return (color = amount);
  }
  return color;
}

function Counter2() {
  const [value, setValue] = useState(0);
  const [color, setColor] = useState('red');

  const handlePlus = () => {
    const action = { type: 'PLUS', amount: 1 };
    setValue((prevValue) => reducer(action, prevValue));
  };
  const handleMinus = () => {
    const action = { type: 'MINUS', amount: 1 };
    setValue((prevValue) => reducer(action, prevValue));
  };

  const handleColorR = () => {
    const action = { type: 'CHANGE_COLOR', amount: 'red' };
    setColor((color) => reducer2(action, color));
  };

  const handleColorG = () => {
    const action = { type: 'CHANGE_COLOR', amount: 'green' };
    setColor((color) => reducer2(action, color));
  };

  const handleColorB = () => {
    const action = { type: 'CHANGE_COLOR', amount: 'blue' };
    setColor((color) => reducer2(action, color));
  };

  return (
    <div>
      <h2>Counter2</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
      <button onClick={handleColorR}>빨강</button>
      <button onClick={handleColorG}>초록</button>
      <button onClick={handleColorB}>파랑</button>
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

export default Counter2;
