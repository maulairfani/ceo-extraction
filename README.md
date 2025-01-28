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

**Schema**
- Buatlah schema / daftar variabel yang ingin di-crawl pada file scripts/schemas.py

**Prompt**
- Atur QUERY prompt yang ada pada file prompts.yml, selain query prompt tidak perlu diubah.

**Crawling**
- Pada file scripts/report_agent.py, adjust variabel di bawah ini
    ```
    json_dir = "data/JSON" # Merupakan direktori tempat json hasil parsing disimpan 
    output_dir = "results" # Merupakan target direktori untuk menyimpan hasil crawling
    files = glob.glob(os.path.join(json_dir, "*", "*.json")) # Merupakan daftar file path json, pastikan format glob sudah tepat.
    ```
- Bagian time.sleep(30) opsional, ini hanya memastikan tidak terjadi rate limit / menit
- Run `python scripts/report_agent.py` melalui terminal
- Hasil akan tersimpan dalam folder `output_dir`