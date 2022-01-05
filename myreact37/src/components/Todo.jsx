import './Todo.css';

function Todo({ todo, onClick }) {
  return (
    <div
      className={`m-1 p-1 rounded-lg text-lg border-4 hover:scale-105 cursor-pointer`}
      style={{ backgroundColor: todo.color }}
      onClick={onClick}
    >
      {todo.color}
      {todo.content}
    </div>
  );
}

export default Todo;
