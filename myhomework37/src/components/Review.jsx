import './Review.css';
// import Stars from './ScoreStars';
import Stars2 from './ScoreStars2';

function Review({ review }) {
  return (
    <div className="m-1 p-1 rounded text-lg border-4">
      <Stars2 score={review.score} />
      {review.content.split('\n').map((letter) => (
        <>
          {letter}
          <br />
        </>
      ))}
    </div>
  );
}

export default Review;
