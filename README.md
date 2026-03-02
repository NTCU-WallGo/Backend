## 啟動後端FastAPI方式
* 建立虛擬環境  
`python -m venv .venv`
* 啟動虛擬環境  
`.venv\Scripts\activate`
* 下載相關套件
` pip install -r requirements.txt`
* (optional) vscode 套件
    * SQLite (alexcvzz)
        * 查看資料庫表格
* 啟動 FastAPI  
`uvicorn app.main:app --reload`
    * 網址列打`localhost:8000/docs`可看有什麼api能用
* 結束虛擬環境  
`deactivate`

## 資料夾功能
* main.py
    * 程式的進入點
* requirements.txt  
    * 相關套件
* /app
    * /core  
        * 設定檔
    * /model  
        * 資料庫相關
    * /routers  
        * 使用者 API
* .gitignore
    * 不要上傳 .venv
* /.venv 
    * 由使用者自行建立
* /frontendTest
    * test.html
        * 登入及註冊測試網頁