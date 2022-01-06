import useFieldValues from 'hooks/useFieldValues';
import { useState } from 'react';
import Review from './Review';
import ReviewForm from './ReviewForm';
import './ReviewList.css';

const INITIAL_STATE = [
  { id: 1, content: '재밌어요~', score: 4 },
  { id: 2, content: '스파이더맨 중 역대급', score: 5 },
  { id: 3, content: '진짜 전설의 레전드', score: 5 },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange, clearFieldvalues] = useFieldValues({
    content: '',
    score: 0,
  });

  const appendReview = () => {
    // review는 데이터베이스에 저장하면 id를 할당해줍니다.
    const reviewId = new Date().getTime();

    const review = { ...fieldValues, id: reviewId };
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
