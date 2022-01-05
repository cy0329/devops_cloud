import { useState } from 'react';

function useFieldValues(initialFieldValues) {
  const [fieldValues, setFieldValues] = useState(initialFieldValues);

  const handleChange = (e) => {
    const { name, value } = e.target;
    console.log('changed', name, value);

    // 함수 안 쓰고, 값 지정
    setFieldValues((prevFieldValues) => ({
      ...prevFieldValues,
      [name]: value,
    }));
  };

  const clearFieldvalues = () => setFieldValues(initialFieldValues);

  return [fieldValues, handleChange, clearFieldvalues];
}

export default useFieldValues;
