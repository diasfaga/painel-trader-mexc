@echo off
REM Caminho do seu projeto local
set PROJETO_PATH=C:\Users\famil\OneDrive\Desktop\painel-trader

REM URL do repositório GitHub
set REPO_URL=https://github.com/diasfaga/painel-trader-mexc.git

cd %PROJETO_PATH%

git init
git add .
git commit -m "Painel trader inicial"
git branch -M main
git remote add origin %REPO_URL%
git push -u origin main

echo ==========================================
echo ✅ Projeto enviado ao GitHub com sucesso!
echo ==========================================
pause
