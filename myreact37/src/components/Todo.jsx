import './Todo.css';

function Todo({ todo, onClick }) {
  return (
    <div
      className={`bg-${todo.color}-200 hover:bg-${todo.color}-400 m-1 p-1 rounded-lg text-lg border-${todo.color}-200 border-4 hover:border-${todo.color}-500 hover:scale-105 cursor-pointer`}
      onClick={onClick}
    >
      {todo.color}
      {todo.content}
    </div>
  );
}

export default Todo;
