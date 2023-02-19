const dataSet = ['"; SELECT * FROM customer-- '];

async function fetchData(data) {
  try {
    const response = await fetch(`http://localhost:3000/employee?id=${data}`);
    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.error(error);
  }
}

dataSet.forEach((data) => {
  fetchData(data);
});
