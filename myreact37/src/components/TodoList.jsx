import useFieldValues from 'hooks/useFieldValues';
import { useState } from 'react';
import Todo from './Todo';
import TodoForm from './TodoForm';
import './TodoList.css';

const INITIAL_STATE = [
  { content: '좋은 몸 만들기', color: 'blue' },
  { content: '파이썬 마스터', color: 'red' },
  { content: '자바스크립트 마스터', color: 'red' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange, clearFieldvalues] = useFieldValues({
    content: '',
    color: 'blue',
  });

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  const appendTodo = () => {
    console.log('새로운 todo를 추가하겠습니다.');

    const todo = { ...fieldValues };
    // setter에 값 지정 방식
    // setTodoList([...todoList, todo]);
    //setter에 함수 지정 방식
    setTodoList((prevTodoList) => [...prevTodoList, todo]);
    clearFieldvalues();
  };

  //   const changedInputText = (e) => {
  //     console.log(e.target.value);
  //     setInputText(e.target.value);
  //   };

  //   const appendInputText = (e) => {
  //     console.log('e.key :', e.key);
  //     if (e.key === 'Enter') {
  //       console.log('inputText :', inputText);
  //       setTodoList(() => [...todoList, { content: inputText }]);
  //     }
  //     setInputText('');
  //   };

  return (
    <div className="todo-list">
      <h2>Todo List</h2>

      <TodoForm
        fieldValues={fieldValues}
        handleChange={handleChange}
        handleSubmit={appendTodo}
      />
      <hr />
      {JSON.stringify(fieldValues)}
      <button
        className="bg-red-500 text-gray-100 cursor-pointer"
        onClick={() => clearFieldvalues()}
      >
        clear
      </button>
      {/* <input
        type="text"
        value={inputText}
        onChange={changedInputText}
        onKeyPress={appendInputText}
      /> */}
      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)} />
      ))}
    </div>
  );
}
export default TodoList;
