from fastapi.middleware.cors import CORSMiddleware
# 設定白名單 (允許的來源)
origins = [
    "http://localhost:5173",  # 允許的前端
    "http://localhost:8080",  # 可以有多個
]

def addMiddleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,    # 1. 允許誰來？ (白名單)
        allow_credentials=True,   # 2. 是否允許攜帶憑證 (如 Cookies)
        allow_methods=["*"],      # 3. 允許什麼動作？ (* 代表 GET, POST, PUT, DELETE 通通可以)
        allow_headers=["*"],      # 4. 允許什麼 Header？ (* 代表通通可以)
        )

