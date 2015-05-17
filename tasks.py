import invoke


@invoke.task
def build():
    invoke.run('jekyll build --config _config.yml')


@invoke.task
def serve():
    invoke.run('jekyll serve --config _config.yml --watch --force_polling')
