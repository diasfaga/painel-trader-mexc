@echo off
REM Caminho do seu projeto local
set PROJETO_PATH=C:\Users\famil\OneDrive\Desktop\painel-trader

REM URL do repositório GitHub
set REPO_URL=https://github.com/diasfaga/painel-trader-mexc.git

cd %PROJETO_PATH%

git pull
git add .
git commit -m "Atualização do código e envio para produção"
git push origin main

echo ====================================================
echo ✅ Código enviado ao GitHub com sucesso!
echo ====================================================
pause
