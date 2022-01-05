import useFieldValues from 'hooks/useFieldValues';
import { useState } from 'react';
import Review from './Review';
import ReviewForm from './ReviewForm';
import './ReviewList.css';

const INITIAL_STATE = [
  { content: '재밌어요~', score: 4 },
  { content: '스파이더맨 중 역대급', score: 5 },
  { content: '진짜 전설의 레전드', score: 5 },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange, clearFieldvalues] = useFieldValues({
    content: '',
    score: '0',
  });

  const appendReview = () => {
    console.log('새로운 todo를 추가하겠습니다.');

    const review = { ...fieldValues };
    // setter에 값 지정 방식
    // setTodoList([...todoList, todo]);
    // setter에 함수 지정 방식
    setReviewList((prevReviewList) => [...prevReviewList, review]);
    clearFieldvalues();
  };

  const [borf, setBorf] = useState('b');
  const handleBorF = () => {
    setBorf(() => {
      if (borf === 'b') {
        return 'f';
      } else if (borf === 'f') {
        return 'b';
      }
      return borf;
    });
  };

  return (
    <div className="review-list">
      <h2 className="text-lg">Review List</h2>
      <hr className="mb-2 border-2 border-orange-400" />
      {borf === 'b' && (
        <button onClick={handleBorF} className="block w-full border py-4">
          리뷰 작성
        </button>
      )}
      {borf === 'f' && (
        <ReviewForm
          fieldValues={fieldValues}
          handleChange={handleChange}
          handleSubmit={appendReview}
          handleBorF={handleBorF}
        />
      )}

      <hr />

      {reviewList.map((review) => (
        <Review review={review} />
      ))}
      {JSON.stringify(fieldValues)}
      <button
        className="border border-gray-200 bg-red-500 text-gray-100 cursor-pointer rounded"
        onClick={() => clearFieldvalues()}
      >
        clear
      </button>
    </div>
  );
}
export default ReviewList;
