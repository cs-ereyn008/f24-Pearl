const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req,res) => {
	res.send('Hello World from backend!');
});

app.listen(port, () => {
	console.log(`Backend server running on port ${port}`);
});
