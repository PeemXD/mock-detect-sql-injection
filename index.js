const express = require("express");
const mysql = require("mysql");
const bodyParser = require("body-parser");
const cors = require("cors");
var process = require('process')

function measureUsage(req, res, next) {
  const start = process.hrtime();
  const memoryStart = process.memoryUsage();

  res.on('finish', () => {
    const end = process.hrtime(start);
    const elapsedTime = end[0] * 1000 + end[1] / 1000000;

    const memoryEnd = process.memoryUsage();
    const memoryUsage = (memoryEnd.rss - memoryStart.rss);

    if (req.method != "OPTIONS") {
      console.log(`\nTime taken for ${req.method} ${req.url}: ${elapsedTime}ms`);
      console.log(`The script uses approximately ${Math.round(memoryUsage * 100000) / 100000} B`);
    }
  });

  next();
}


const app = express();
app.use(measureUsage);
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
  // console.log(req.body.data.username);

  connection.query(
    `SELECT * FROM users WHERE username = '${req.body.data.username}' AND password = '${req.body.data.password}'`,
    (err, results) => {
      // console.log(results);
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
  // console.log(`SELECT * FROM service WHERE name = "${name}"`);

  if (!name) {
    connection.query(
      `SELECT * FROM service`,
      (err, results) => {
        // console.log(results);
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

    //!
    const pattern = /^[ก-๏a-zA-Z\d0-9]+$/;
    // console.log(name);
    const pass = pattern.test(name);
    // console.log(pass);
    if (!pass) {
      res.status(200).send({
        status: 'error',
        message: 'Input string does not match the pattern'
      });
      return ;
    }
    //!

    const sqll = `SELECT * FROM service WHERE name = "${name}"`
    // console.log(sqll);
    connection.query(sqll
      ,
      (err, results) => {
        // console.log(results);
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