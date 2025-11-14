@echo off

cd C:\Users\skanc\PycharmProjects\ExamProject

start cmd /k "python main.py"

timeout /t 5 /nobreak

curl -X POST http://127.0.0.1:5000/media ^
-H "Content-Type: application/json" ^
-d "{\"type\": \"book\", \"title\": \"FourthWing\", \"genre\": \"Fantasy\", \"year\": 2023, \"extra\": \"Rebecca Yarros\"}"

curl -X POST http://127.0.0.1:5000/media ^
-H "Content-Type: application/json" ^
-d "{\"type\": \"movie\", \"title\": \"Avengers\", \"genre\": \"Fantasy\", \"year\": 2018, \"extra\": \"Anthony Russo\"}"

curl -X POST http://127.0.0.1:5000/media ^
-H "Content-Type: application/json" ^
-d "{\"type\": \"music\", \"title\": \"Popular\", \"genre\": \"RnB\", \"year\": 2021, \"extra\": \"The Weekend\"}"

curl -X POST http://127.0.0.1:5000/media/FourthWing/rating ^
-H "Content-Type: application/json" ^
-d "{\"rating\": 5}"

curl -X POST http://127.0.0.1:5000/media/Avengers/rating ^
-H "Content-Type: application/json" ^
-d "{\"rating\": 5}"

curl -X POST http://127.0.0.1:5000/media/Popular/rating ^
-H "Content-Type: application/json" ^
-d "{\"rating\": 4}"

curl http://127.0.0.1:5000/media

curl http://127.0.0.1:5000/media/genre/Fantasy

curl -X DELETE http://127.0.0.1:5000/media/Avengers

curl http://127.0.0.1:5000/media

pause
