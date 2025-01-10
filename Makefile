start:
	nohup uvicorn app.main:app --reload --port 3094 &
	echo "Uvicorn app started on port 3094."


stop:
	pkill -f 'uvicorn app.main:app'
	echo "Uvicorn app stopped."

restart: stop start
