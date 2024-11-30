const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const path = require('path');
const fs = require('fs');
const app = express();
const port = process.env.PORT || 3000;

const { spawn } = require('child_process');

//Middleware for parsing form data (stores searched violation code)
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(express.urlencoded({ extended: true })); // For parsing application/x-www-form-urlencoded
app.use(express.json()); // For parsing application/json

//Serve static files (HTML, CSS, JS, Images)
app.use(express.static(path.join(__dirname, '../../frontend/public')));

//Runs web scraper on backend start
//You must issue the commands 'pip install beautifulsoup' and 'pip install schedule' in your terminal
const scraper = spawn('python', ['../database/webscraper_new.py']);

scraper.stdout.on('data', (data) => {
	console.log(`Scraper Output: ${data}`);
});

scraper.stderr.on('data', (data) => {
	console.error(`Scraper Error: ${data}`);
});

scraper.on('close', (code) => {
	console.log(`Scraper process exited with code ${code}`);
});
//End of web scraper code

app.get('/get-law', (req, res) => {
	const lawCode = req.query.law; // Get the law code from the query string
	if (!lawCode) {
		res.status(400).send('Error: No law code provided.');
		return;
	}

	// Format the file name
	const formattedCode = lawCode.replace(/\./g, '_'); // Replace dots with underscores
	const filePath = path.join(__dirname, '../traffic_laws', `${formattedCode}_.txt`);

	console.log('Resolved file path:', filePath);

	// Check if the file exists and send its content
	if (fs.existsSync(filePath)) {
		const fileContent = fs.readFileSync(filePath, 'utf-8');
		res.send(fileContent);
	} else {
		res.status(404).send(`Error: File not found for law code ${lawCode}.`);
	}
});


//Home route
app.get('/', (req, res) => {
	//res.send('Hello World from backend!');
	res.sendFile(path.join(__dirname, '../../frontend/public/index.html'));
});

app.get('/api/users', async (req, res) => {
	try {
		const response = await axios.get('http://127.0.0.1:8000/users/');
		res.json(response.data);
	} catch (error) {
		console.error(error);
		res.status(500).send('server Error');
	}
});

app.get('/api/trafficlaws', async (req, res) => {
	try {
		const response = await axios.get('http://127.0.0.1:8000/trafficlaws/');
		res.json(response.data);
	} catch (error) {
		console.error(error);
		res.status(500).send('server Error');
	}
});

app.get('/api/violations', async (req, res) => {
	try {
		const response = await axios.get('http://127.0.0.1:8000/violations/');
		res.json(response.data);
	} catch (error) {
		console.error(error);
		res.status(500).send('server Error');
	}
});

//User routes
app.get('/user', (req, res) => {
	console.log('Create New User');
	res.send('Create New User');
});

app.delete('/user', (req, res) => {
	console.log('Delete User');
	res.send('Delete user');
});

//Frequently asked questions route
app.get('/faqs', (req, res) => {
	//res.send('Frequently Asked Questions about traffic laws');
	res.sendFile(path.join(__dirname, '../../frontend/public/FAQ.html'));
});

//login route
app.get('/login', (req, res) => {
	//res.send('Login into Traffic Tamer');
	res.sendFile(path.join(__dirname, '../../frontend/public/Login.html'));
});

//sign up route
app.get('/signUp', (req, res) => {
	//res.send('Sign Up for Traffic Tamer');
	res.sendFile(path.join(__dirname, '../../frontend/public/SignUp.html'));
});

///state-specifc traffic law route
/*app.get('/laws/:state', (req, res) => {
	const state = req.params.state;
	res.send(`Traffic laws for ${state}`);
});*/

//search route
/*app.get('/searchResults', (req, res) => {
	const query = req.query.q;
	res.send(`Search results for: ${query}`);
});

//Bookmark route
/*app.get('/bookmarks', (req, res) => {
	res.send('Your bookmarked traffic laws');
});*/

//user feedback route
/*app.post('/feedback', (req, res) => {
	res.send('Thank you for your feedback!');
});*/

//How it works route
app.get('/howItWorks', (req, res) => {
	//res.send('How it works');
	res.sendFile(path.join(__dirname, '../../frontend/public/HowItWorks.html'));
});

//contact route
app.get('/contact', (req, res) => {
	//res.send('Contact us for more information or assistance');
	res.sendFile(path.join(__dirname, '../../frontend/public/ContactUs.html'));
});

//terms route
app.get('/terms', (req, res) => {
	//res.send('Terms for Traffic Tamer');
	res.sendFile(path.join(__dirname, '../../frontend/public/Terms.html'));
});

//legal updates route
/*app.get('/updates', (req, res) => {
	res.send('Recent updates in traffic laws');
});*/

app.listen(port, () => {
	console.log(`Backend server running on port ${port}`);
});
