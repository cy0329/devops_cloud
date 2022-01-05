function ReviewForm({ fieldValues, handleChange, handleSubmit, handleBorF }) {
  return (
    <div className="border-2 border-gray-500 p-3 rounded">
      <h2 className="text-lg">평점</h2>

      <select
        onChange={handleChange}
        name="score"
        value={fieldValues.score}
        className="block appearence-none w-full border border-gray-400 py-3 px-4 rounded"
      >
        <option>0</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
      </select>

      <hr />

      <h2 className="text-lg">리뷰</h2>
      <textarea
        type="text"
        className="shadow w-full border border-gray-400 rounded"
        onChange={handleChange}
        name="content"
        value={fieldValues.content}
      />

      <hr />

      <button
        onClick={() => {
          handleSubmit();
          handleBorF();
        }}
        className="border-2 bg-blue-100 hover:bg-blue-400"
      >
        저장하기
      </button>

      <hr />
    </div>
  );
}
export default ReviewForm;
