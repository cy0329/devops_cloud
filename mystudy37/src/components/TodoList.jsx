import { useState } from 'react';
import Todo from './Todo';

const INITIAL_STATE = [
  { content: '체중감량 - 목표 80kg' },
  { content: '파이썬 마스터' },
  { content: '자바스크립트 마스터' },
];

function TodoList() {
  const [state, setState] = useState(INITIAL_STATE);
  const removeTodo = (clickedIndex) => {
    setState((prevState) =>
      prevState.filter((_, index) => index !== clickedIndex),
    );
  };

  return (
    <div>
      <h2>Todo List</h2>
      {state.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)} />
      ))}
    </div>
  );
}
export default TodoList;
