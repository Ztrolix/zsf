const express = require('express');
const multer  = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
const port = process.env.PORT || 3000;

const UPLOAD_FOLDER = 'uploads';

app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, UPLOAD_FOLDER);
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  }
});

const upload = multer({ storage: storage });

app.get('/', (req, res) => {
  const files = fs.readdirSync(UPLOAD_FOLDER);
  res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

app.post('/upload', upload.single('file'), (req, res) => {
  res.redirect('/');
});

app.get('/download/:filename', (req, res) => {
  const filename = req.params.filename;
  res.download(path.join(UPLOAD_FOLDER, filename));
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});