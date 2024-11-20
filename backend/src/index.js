const express = require('express');
const axios = require('axios');
const app = express();
const port = process.env.PORT || 3000;
const path = require('path');

//Serve static files (HTML, CSS, JS, Images)
app.use(express.static(path.join(__dirname, '../../frontend/public')));

//Home route
app.get('/', (req,res) => {
	res.send('Hello World from backend!');
	res.sendFile(path.join(__dirname, '../../frontend/public/index.html'));
});

app.get('/api/users', async (req, res) => {
	try {
		const response = await axios.get('http://127.0.0.1:8000/users/');
		res.json(response.data);
	} catch (error){
		console.error(error);
		res.status(500).send('server Error');
	}
});

app.get('/api/trafficlaws', async (req, res) => {
	try {
		const response = await axios.get('http://127.0.0.1:8000/trafficlaws/');
		res.json(response.data);
	} catch (error){
		console.error(error);
		res.status(500).send('server Error');
	}
});

app.get('/api/violations', async (req, res) => {
	try {
		const response = await axios.get('http://127.0.0.1:8000/violations/');
		res.json(response.data);
	} catch (error){
		console.error(error);
		res.status(500).send('server Error');
	}
});

//Frequently asked questions route
app.get('/faqs', (req, res) => {
	res.send('Frequently Asked Questions about traffic laws');
	res.sendFile(path.join(__dirname, '../../frontend/public/FAQ.html'));
});

//login route
app.get('/login', (req, res) => {
	res.send('Login into Traffic Tamer');
	res.sendFile(path.join(__dirname, '../../frontend/public/Login.html'));
});

//sign up route
app.get('/signUp', (req, res) => {
	res.send('Sign Up for Traffic Tamer');
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
	res.send('How it works');
	res.sendFile(path.join(__dirname, '../../frontend/public/HowItWorks.html'));
});

//contact route
app.get('/contact', (req, res) => {
	res.send('Contact us for more information or assistance');
	res.sendFile(path.join(__dirname, '../../frontend/public/ContactUs.html'));
});

//terms route
app.get('/terms', (req, res) => {
	res.send('Terms for Traffic Tamer');
	res.sendFile(path.join(__dirname, '../../frontend/public/Terms.html'));
});

//legal updates route
/*app.get('/updates', (req, res) => {
    res.send('Recent updates in traffic laws');
});*/

app.listen(port, () => {
	console.log(`Backend server running on port ${port}`);
});
