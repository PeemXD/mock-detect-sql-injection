const express = require("express");
const mysql = require("mysql");
const bodyParser = require("body-parser");
const cors = require("cors");
var process = require("process");

function measureUsage(req, res, next) {
  const start = process.hrtime();
  const memoryStart = process.memoryUsage();

  res.on("finish", () => {
    const end = process.hrtime(start);
    const elapsedTime = end[0] * 1000 + end[1] / 1000000;

    const memoryEnd = process.memoryUsage();
    const memoryUsage = memoryEnd.rss - memoryStart.rss;

    if (req.method != "OPTIONS") {
      console.log(
        `\nTime taken for ${req.method} ${req.url}: ${elapsedTime}ms`
      );
      console.log(
        `The script uses approximately ${
          Math.round(memoryUsage * 100000) / 100000
        } B`
      );
    }
  });

  next();
}

function haveBlackListWord(input) {
  const blacklist = [
    "UNION",
    "INSERT",
    "UPDATE",
    "DELETE",
    "SHOW",
    "users",
    "customer",
    "work_background",
    "graduation_certificate",
    "address",
    "id_card",
    "house_registration",
  ];
  // i -> case-insensitive -> not care upper/lower case
  // blacklist.join("|") --> 'badword1|badword2|badword3'
  // return true if input docs not caontain Black List Word
  const regex = new RegExp(`\\b(${blacklist.join("|")})\\b`, "i");
  return !regex.test(input);
}

function validPattern(input) {
  const pattern = /^[ก-๏a-zA-Z\d0-9]+$/;
  return !pattern.test(id);
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
  // multipleStatements: true
});

connection.connect();

app.get("/", (req, res) => {
  res.send({ success: true });
});

app.post("/login", (req, res) => {
  if (
    haveBlackListWord(req.body.data.username) ||
    haveBlackListWord(req.body.data.password) ||
    validPattern(req.body.data.username) ||
    validPattern(req.body.data.password)
  ) {
    res.status(200).send({
      status: "error",
      message: "Input string does not match the pattern",
    });
    return;
  }

  connection.query(
    `SELECT * FROM users WHERE username = '${req.body.data.username}' AND password = '${req.body.data.password}'`,
    (err, results) => {
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

app.get("/employee", (req, res) => {
  const id = req.query?.id;

  if (!id) {
    connection.query(
      `SELECT employee_id, prefixname, fname, lname, nickname, email, tel FROM employee`,
      (err, results) => {
        // console.log(results);
        if (err) {
          res.status(500).send();
          // res.status(500).send(err); //! error base
        } else if (!results.length) {
          res.status(401).send({ success: false });
        } else {
          res.status(200).send(results);
        }
      }
    );
  } else {
    if (haveBlackListWord(id) || validPattern(id)) {
      res.status(200).send({
        status: "error",
        message: "Input string does not match the pattern",
      });
      return;
    }

    const sqll = `SELECT employee_id, prefixname, fname, lname, nickname, email, tel FROM employee WHERE employee_id = "${id}"`;
    // console.log(sqll);
    connection.query(sqll, (err, results) => {
      // console.log(results);
      if (err) {
        res.status(500).send();
      } else if (!results.length) {
        res.status(401).send({ success: false });
      } else {
        res.status(200).send(results);
      }
    });
  }
});

app.listen(3000, () => {
  console.log("Server started on http://localhost:3000");
});
