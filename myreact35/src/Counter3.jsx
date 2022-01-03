const { useState, useReducer } = require('react/cjs/react.development');

function reducer(prevState, action) {
  const { type, amount, color } = action;
  if (type === 'COUNT') {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === 'CHANGE_COLOR') {
    return { ...prevState, color };
  }
  return prevState;
}

function Counter3() {
  //   const [value, setValue] = useState(0);
  //   const [color, setColor] = useState('red');
  //   const { value, color } = state;
  //   const [state, setState] = useState({ value: 0, color: 'red' });
  const [state, dispatch] = useReducer(reducer, { value: 0, color: 'red' });

  const handlePlus = () => {
    // const action = { type: 'PLUS', amount: 1 };
    dispatch({ type: 'COUNT', amount: 1 });
  };

  const handleMinus = () => {
    // const action = { type: 'MINUS', amount: 1 };
    dispatch({ type: 'COUNT', amount: -1 });
  };

  const changeRed = () => {
    // const action = { type: 'CHANGE_COLOR', color: 'red' };
    dispatch({ type: 'CHANGE_COLOR', color: 'red' });
  };

  const changeGreen = () => {
    // const action = { type: 'CHANGE_COLOR', color: 'green' };
    dispatch({ type: 'CHANGE_COLOR', color: 'green' });
  };

  const changeBlue = () => {
    // const action = { type: 'CHANGE_COLOR', color: 'blue' };
    dispatch({ type: 'CHANGE_COLOR', color: 'blue' });
  };

  return (
    <div>
      <h2>Counter3</h2>
      <div style={{ ...defaultStyle, backgroundColor: state.color }}>
        {state.value}
      </div>
      <hr />
      {/* <button onClick={() => setValue(value + 1)}>+</button>
      <button onClick={() => setValue(value - 1)}>-</button> */}
      <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button>
      <br />
      {/* <button onClick={() => setColor("red")}>red</button>
      <button onClick={() => setColor("green")}>green</button>
      <button onClick={() => setColor("blue")}>blue</button> */}
      <button onClick={changeRed}>red</button>
      <button onClick={changeGreen}>green</button>
      <button onClick={changeBlue}>blue</button>
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

export default Counter3;
