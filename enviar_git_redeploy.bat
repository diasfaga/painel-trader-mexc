@echo off
cd C:\Users\famil\OneDrive\Desktop\painel-trader-mexc

echo ================================
echo Enviando código ao GitHub...
git add .
git commit -m "Atualização automática"
git push origin main

echo ================================
echo Chamando redeploy no Railway...

curl -X POST "https://backboard.railway.app/project/0e4e956f-18cd-4bdc-bc1d-a8f7d8ae323e/deploy" -H "Authorization: e1f211bd-cda2-453b-88ff-fbeb778f9fb1"

echo ================================
echo Redeploy Railway chamado!

pause
