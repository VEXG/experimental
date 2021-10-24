const express = require('express');
const path = require('path');
const client = express();

client.set('view engine', 'ejs');

client.use(express.json());
client.use(
    express.urlencoded({
        extended: true,
    }),
);

client.use('/public', express.static(path.join(__dirname, './public')));

client.get('/', async (req, res) => {
    res.render(path.join(__dirname, './public/index'));
});

client.post('/result', async (req, res) => {
    res.render(path.join(__dirname, './public/result'), req.body);
});

client.listen(3000);
