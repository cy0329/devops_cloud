function TodoForm({ fieldValues, handleChange, handleSubmit }) {
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <div className="border-2 border-red-500 p-3">
      <h2 className="text-lg underline">TodoForm</h2>

      <select onChange={handleChange} name="color" value={fieldValues.color}>
        <option>blue</option>
        <option>red</option>
        {/* <option>yellow</option> */}
      </select>

      <input
        type="text"
        className="border-2 border-gray-400"
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
