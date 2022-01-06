function TodoForm({ fieldValues, handleChange, handleSubmit }) {
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <div className="border-2 border-gray-500 p-3 rounded">
      <h2 className="text-lg underline">TodoForm</h2>

      <select onChange={handleChange} name="color" value={fieldValues.color}>
        <option>red</option>
        <option>orange</option>
        <option>yellow</option>
        <option>green</option>
        <option>blue</option>
        <option>navy</option>
        <option>purple</option>
        <option>pink</option>
        <option>coral</option>
      </select>

      <input
        type="text"
        className="border-2 border-gray-400 rounded"
        onChange={handleChange}
        name="content"
        value={fieldValues.content}
        onKeyPress={handleKeyPress}
      />
      <button onClick={() => handleSubmit()}>저장</button>
      <hr />
    </div>
  );
}
export default TodoForm;
