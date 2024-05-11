cd "C:\Program Files\stargaze-wiki"
python copy_files.py
start chrome http://localhost:8080/
cmd /k npx quartz build --serve
