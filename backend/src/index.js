const express = require('express');
const axios = require('axios');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req,res) => {
	res.send('Hello World from backend!');
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

//Home route
/*app.get('/', (req,res) => {
	res.send('Welcome to Traffic Tamer - Your Guide about Traffic Laws!');
});

///state-specifc traffic law route
app.get('/laws/:state', (req, res) => {
	const state = req.params.state;
	res.send(`Traffic laws for ${state}`);
});

//search route
app.get('/search', (req, res) => {
	const query = req.query.q;
	res.send(`Search results for: ${query}`);
});

//Frequently asked questions route
app.get('/faqs', (req, res) => {
	res.send('Frequently Asked Questions about traffic laws');
});

//Bookmark route
app.get('/bookmarks', (req, res) => {
	res.send('Your bookmarked traffic laws');
});

//user feedback route
app.post('/feedback', (req, res) => {
	res.send('Thank you for your feedback!');
});

//contact route
app.get('/contact', (req, res) => {
	res.send('Contact us for more information or assistance');
});

//legal updates route
app.get('/updates', (req, res) => {
    res.send('Recent updates in traffic laws');
});*/

app.listen(port, () => {
	console.log(`Backend server running on port ${port}`);
});
