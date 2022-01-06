import './Counter.css';

const { useState, useReducer } = require('react');

const ACTION_TYPES = {
  PLUS: 'PLUS',
  MINUS: 'MINUS',
};

function reducer(prevState, action) {
  const { type } = action;
  if (type === ACTION_TYPES.PLUS) {
    return prevState + 1;
  } else if (type === ACTION_TYPES.MINUS) {
    return prevState - 1;
  }
  return prevState;
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, 0);
  const handlePlus = () => {
    const action = { type: ACTION_TYPES.PLUS };
    dispatch(action);
  };

  const handleMinus = () => {
    const action = { type: ACTION_TYPES.MINUS };
    dispatch(action);
  };

  return (
    <div
      className="counter"
      onClick={handlePlus}
      style={{ backgroundColor: 'red' }}
      onContextMenu={(e) => {
        e.preventDefault();
        handleMinus();
      }}
    >
      {state}
    </div>
  );
}

export default Counter;
