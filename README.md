# Single Turn ESGCrawling

**Preparation**
- Clone repository
- Create virtual environment dan aktifkan
- Install semua library yang ada pada requirements.txt

**Indexing**
- Buat index di pinecone dengan dimension size 3072 menggunakan google cloud
- Ubah .env PINECONE_INDEX sesuai dengan nama index yang telah dibuat

- Buka 01. parsing.ipynb, sesuaikan adjustable. Pengguna dapat memilih menggunakan input berupa filepath atau url
- Run file 01. parsing.ipynb

- Buka 02. vectordb.ipynb, sesuaikan adjustable yakni direktori file json (hasil pdf parsing)
- Run file 02. vectordb.ipynb
- Bersambung... di file 03. crawling.ipynb