const express = require("express");
const mysql = require("mysql");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
app.use(bodyParser.json());
app.use(cors());

// Connect to MySQL
const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  database: "mydb"
});

connection.connect();

app.get("/", (req, res) => {
  res.send({ success: true });
});

app.post("/login", (req, res) => {
  console.log(req.body.data.username);
  connection.query(
    `SELECT * FROM users WHERE username = '${req.body.data.username}' AND password = '${req.body.data.password}'`,
    (err, results) => {
      console.log(results);
      if (err) {
        res.status(500).send();
      } else if (!results.length) {
        res.status(401).send({ success: false });
      } else {
        res.send({ success: true });
      }
    }
  );
});

app.listen(3000, () => {
  console.log("Server started on http://localhost:3000");
});