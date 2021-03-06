// useState 버전

import Circle from 'Circle';
import { useReducer, useState } from 'react';
import { shuffle_array, zip } from 'utils';

const INITIAL_STATE = {
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
};

const get_lotto_numbers = () =>
  [...Array(45).keys()]
    .map((index) => index + 1)
    .sort(() => Math.random() - Math.random())
    .slice(0, 7)
    .sort((number1, number2) => number1 - number2);

const get_ball_colors = () => {
  const ballColors = new Array();
  while (ballColors.length < 7) {
    ballColors.push('#' + Math.round(Math.random() * 0xffffff).toString(16));
  }
  return ballColors;
};

const ACTION_TYPES = {
  GENERATE_NUMBERS: 'GENERATE_NUMBERS',
  SHUFFLE_NUMBERS: 'SHUFFLE_NUMBERS',
  SHUFFLE_COLORS: 'SHUFFLE_COLORS',
  CHANGE_COLOR: 'CHANGE_COLOR',
  DELETE_CIRCLE: 'DELETE_CIRCLE',
  CLEAR_ALL: 'CLEAR_ALL',
};

// 순수 함수
function reducer(prevState, action) {
  // 새로운 상탯값을 계산해서 리턴합니다.

  const { type, index } = action;

  if (type === ACTION_TYPES.GENERATE_NUMBERS) {
    return {
      // ...prevState,
      numbers: get_lotto_numbers(),
      colors: get_ball_colors(),
    };
  } else if (type === ACTION_TYPES.SHUFFLE_NUMBERS) {
    return {
      ...prevState,
      numbers: shuffle_array(prevState.numbers),
    };
  } else if (type === ACTION_TYPES.SHUFFLE_COLORS) {
    return {
      ...prevState,
      colors: shuffle_array(prevState.colors),
    };
  } else if (type === ACTION_TYPES.CHANGE_COLOR) {
    return {
      ...prevState,
      colors: prevState.colors.map((color, index) => {
        if (index === action.index) {
          return '#' + Math.round(Math.random() * 0xffffff).toString(16);
        }
        return color;
      }),
    };
  } else if (type === ACTION_TYPES.DELETE_CIRCLE) {
    const ballList = zip(prevState.numbers, prevState.colors).filter(
      ([number, color], index) => index !== action.index,
    );
    const numList = ballList.map(([number, color]) => number);
    const colList = ballList.map(([number, color]) => color);
    return {
      numbers: numList,
      colors: colList,
    };
    // return {
    //   numbers: prevState.numbers.filter(
    //     (number, index) => index !== action.index,
    //   ),
    //   colors: prevState.colors.filter((color, index) => index !== action.index),
    // };
  } else if (type === ACTION_TYPES.CLEAR_ALL) {
    return {
      numbers: [],
      colors: [],
    };
  }

  return prevState;
}

function SevenNumbers2({ title }) {
  // const [state, setState] = useState(INITIAL_STATE);
  const [state, dispatch] = useReducer(reducer, INITIAL_STATE);

  const generateNumbers = () => {
    // 의도 : numbers 항목을 새로운 배열로 변경하겠다.
    const action = { type: ACTION_TYPES.GENERATE_NUMBERS };
    // setState((prevState) => reducer(prevState, action));
    dispatch(action);
  };

  const shuffleNumbers = () => {
    const action = { type: ACTION_TYPES.SHUFFLE_NUMBERS };
    // setState((prevState) => reducer(prevState, action));
    dispatch(action);
  };

  const shuffleColors = () => {
    const action = { type: ACTION_TYPES.SHUFFLE_COLORS };
    // setState((prevState) => reducer(prevState, action));
    dispatch(action);
  };

  const changeColor = (circleIndex) => {
    const action = { type: ACTION_TYPES.CHANGE_COLOR, index: circleIndex };
    // setState((prevState) => reducer(prevState, action));
    dispatch(action);
  };

  const removeCircle = (circleIndex) => {
    const action = { type: ACTION_TYPES.DELETE_CIRCLE, index: circleIndex };
    // setState((prevState) => reducer(prevState, action));
    dispatch(action);
  };

  const clearAll = () => {
    const action = { type: ACTION_TYPES.CLEAR_ALL };
    dispatch(action);
  };

  return (
    <div>
      {title && <h2>{title}</h2>}
      {zip(state.numbers, state.colors).map(([number, color], index) => (
        <Circle
          number={number}
          backgroundColor={color}
          onClick={() => changeColor(index)}
          onContextMenu={(e) => {
            e.preventDefault();
            removeCircle(index);
          }}
        />
      ))}
      <hr />
      <button onClick={generateNumbers}>공 뽑기</button>
      <button onClick={shuffleNumbers}>숫자만 섞기</button>
      <button onClick={shuffleColors}>색깔만 섞기</button>
      <button onClick={clearAll}>초기화</button>
      <hr />
      <pre>{JSON.stringify(state, null, 4)}</pre>
    </div>
  );
}

export default SevenNumbers2;
