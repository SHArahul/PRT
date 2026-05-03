const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;
const ENV_COLOR = process.env.ENV_COLOR || 'blue';

app.get('/', (req, res) => {
    res.send(`
        <h1>Blue-Green Deployment Demo</h1>
        <p>Active Environment: <strong>${ENV_COLOR.toUpperCase()}</strong></p>
        <p>Version: 1.0</p>
    `);
});

app.get('/health', (req, res) => {
    res.status(200).json({
        status: 'healthy',
        environment: ENV_COLOR
    });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});