task :install do
    if ! File.exists? './.venv/bin/activate'
        raise unless system("virtualenv .venv")
    end
    if ENV['VIRTUAL_ENV'] != File.join(Dir.pwd, '.venv')
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
end
