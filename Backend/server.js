const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const session = require('express-session');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({
    secret: 'secret',
    resave: true,
    saveUninitialized: true
}));

// Connexion à la base de données
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'gestion_taches'
});

connection.connect();

// Page de connexion
app.get('/login', (req, res) => {
    res.send(`
        <h2>Login</h2>
        <form action="/auth" method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    `);
});

// Authentification
app.post('/auth', (req, res) => {
    let username = req.body.username;
    let password = req.body.password;
    if (username && password) {
        // ATTENTION: Vulnérable à l'injection SQL
        connection.query('SELECT * FROM users WHERE username = ? AND password = ?', [username, password], (error, results, fields) => {
            if (results.length > 0) {
                req.session.loggedin = true;
                req.session.username = username;
                res.redirect('/tasks');
            } else {
                res.send('Incorrect Username and/or Password!');
            }           
            res.end();
        });
    } else {
        res.send('Please enter Username and Password!');
        res.end();
    }
});

// Affichage des tâches pour l'utilisateur connecté
app.get('/tasks', (req, res) => {
    if (req.session.loggedin) {
        // ATTENTION: Utilisation de concaténation directe, vulnérable à l'injection SQL
        let query = `SELECT * FROM tasks WHERE user_id = (SELECT id FROM users WHERE username = '${req.session.username}')`;
        connection.query(query, (error, tasks) => {
            if (error) throw error;
            let content = tasks.map(task => `<p>${task.description} - ${task.completed ? 'Complété' : 'À faire'}</p>`).join('');
            res.send(content);
        });
    } else {
        res.send('Please login to view this page!');
    }
    res.end();
});

// Autres routes pour l'ajout, la modification, la suppression de tâches ici...

app.listen(port, () => {
    console.log(`Serveur démarré sur le port ${port}`);
});
