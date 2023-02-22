var dataSet = ['\\"; INSERT INTO service(price) VALUES(722)# '];

function fetchData(data) {
  fetch("http://localhost:3000/employee?id=" + data, {
    method: "GET",
    mode: "cors",
    headers: { "Content-Type": "application/json" },
  })
    .then((response) => response.json())
    .then((apiJsonData) => {
      console.log(apiJsonData);
    })
    .catch((error) => {
      console.error(error);
    });
}

dataSet.forEach(async (data) => {
  await fetchData(data);
});
