import { useState } from 'react';

function SevenNumbers() {
  const [state, setState] = useState({
    numbers: [0, 0, 0, 0, 0, 0, 0],
    colors: [
      '#1B62BF',
      '#1755A6',
      '#37A647',
      '#F29F05',
      '#F23838',
      'purple',
      'pink',
    ],
  });
  return (
    <div>
      <h2>7개의 숫자</h2>
    </div>
  );
}
export default SevenNumbers;
