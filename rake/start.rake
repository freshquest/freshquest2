task :default => :start

task :start do
	exec("gunicorn --config gunicorn.ini.py project.wsgi")
end
