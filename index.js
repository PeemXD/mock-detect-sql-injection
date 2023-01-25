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
  database: "mockInjection",
  multipleStatements: true
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

app.get("/service", (req, res) => {
  const name = req.query?.name;
  console.log(`SELECT * FROM service WHERE name = "${name}"`);

  if (!name) {
    connection.query(
      `SELECT * FROM service`,
      (err, results) => {
        console.log(results);
        if (err) {
          res.status(500).send();
        } else if (!results.length) {
          res.status(401).send({ success: false });
        } else {
          res.status(200).send(results);
        }
      }
    );
  }else{
    const sqll = `SELECT * FROM service WHERE name = "${name}"`
    console.log(sqll);
    connection.query(sqll
      ,
      (err, results) => {
        console.log(results);
        if (err) {
          res.status(500).send();
        } else if (!results.length) {
          res.status(401).send({ success: false });
        } else {
          res.status(200).send(results);
        }
      }
    );
  }
});

app.listen(3000, () => {
  console.log("Server started on http://localhost:3000");
});