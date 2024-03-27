const express = require('express');
const path = require('path');
const PORT = process.env.PORT || 8080;
const app = express();

app.use(express.static(path.join(__dirname, 'dist'))); // Serve static files from `dist` directory
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist/index.html')); // Handle SPA routing by returning `index.html` for all routes
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
