start:
	nohup uvicorn app.main:app --reload --port 3001 &
	echo "Uvicorn app started on port 3001."


stop:
	pkill -f 'uvicorn app.main:app'
	echo "Uvicorn app stopped."

restart: stop start
