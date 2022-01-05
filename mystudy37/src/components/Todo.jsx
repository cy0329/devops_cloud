import './Todo.css';

function Todo({ todo, onClick }) {
  return <div onClick={onClick}>{todo.content}</div>;
}

export default Todo;
