start:
	nohup uvicorn app.main:app --reload --port 8094 &
	echo "Uvicorn app started on port 8094."


stop:
	pkill -f 'uvicorn app.main:app'
	echo "Uvicorn app stopped."

restart: stop start
