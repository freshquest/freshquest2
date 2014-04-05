task :install do
    if ! File.exists? './.venv/bin/activate'
        raise unless system("virtualenv .venv")
    end
    if ! ENV['VIRTUAL_ENV']
        puts
        puts "Please run:"
        puts
        puts "\tsource .venv/bin/activate"
        puts
        raise
    end
    raise unless system("npm prune")
    raise unless system("npm install")
    raise unless system("bower install")
    raise unless system("pip install -r requirements.txt")
    unless system("psql -c '\\q' 2>/dev/null")
        puts
        puts "Please run Postgres.app"
        puts
        raise
    end
    unless system("psql freshquest2 -c '\\q' 2>/dev/null")
        raise unless system("psql -c 'create database freshquest2'")
    end
end

