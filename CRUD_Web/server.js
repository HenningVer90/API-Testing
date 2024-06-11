const express = require('express');
const path = require('path');
const sqlite3 = require('sqlite3').verbose();

const app = express();
const port = 3000;

// Connect to the database
const db = new sqlite3.Database(':memory:');
db.serialize(() => {
    db.run('CREATE TABLE IF NOT EXISTS users (name TEXT, surname TEXT)');
});

// Middleware to parse JSON bodies
app.use(express.json());

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

// API endpoint to get all users
app.get('/api/users', (req, res) => {
    db.all('SELECT * FROM users', (err, rows) => {
        if (err) {
            res.status(500).send(err.message);
        } else {
            res.json(rows);
        }
    });
});

// API endpoint to create a new user
app.post('/api/users', (req, res) => {
    const { name, surname } = req.body;
    if (!name || !surname) {
        res.status(400).send('Name and surname are required');
    } else {
        db.run('INSERT INTO users (name, surname) VALUES (?, ?)', [name, surname], (err) => {
            if (err) {
                res.status(500).send(err.message);
            } else {
                res.sendStatus(201);
            }
        });
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
